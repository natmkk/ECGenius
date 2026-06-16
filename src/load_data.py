import ast
from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DIR, PTBXL_METADATA_CSV, PTBXL_SCP_CSV


def _validate_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")


def load_ptbxl_metadata() -> tuple[pd.DataFrame, pd.DataFrame]:
    _validate_file_exists(PTBXL_METADATA_CSV)
    _validate_file_exists(PTBXL_SCP_CSV)

    df = pd.read_csv(PTBXL_METADATA_CSV, index_col="ecg_id")
    scp_df = pd.read_csv(PTBXL_SCP_CSV, index_col=0)

    if "scp_codes" not in df.columns:
        raise ValueError("Expected 'scp_codes' column not found in PTB-XL metadata.")

    df["scp_codes"] = df["scp_codes"].apply(ast.literal_eval)
    return df, scp_df


def inspect_dataset(df: pd.DataFrame, scp_df: pd.DataFrame) -> None:
    print("Metadata shape:", df.shape)
    print("SCP statements shape:", scp_df.shape)
    print("\nMetadata columns:")
    print(list(df.columns))

    print("\nFirst 3 rows:")
    print(df.head(3))

    print("\nExample scp_codes:")
    print(df["scp_codes"].iloc[0])


def save_processed_metadata(df: pd.DataFrame) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "ptbxl_binary_labels.csv")