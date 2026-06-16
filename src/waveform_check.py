import wfdb

from src.config import PTBXL_DIR, PTBXL_METADATA_CSV
import pandas as pd


def main() -> None:
    df = pd.read_csv(PTBXL_METADATA_CSV, index_col="ecg_id")
    first_path = df.iloc[0]["filename_lr"]
    full_record_path = PTBXL_DIR / first_path

    record = wfdb.rdsamp(str(full_record_path))
    signal, meta = record

    print("Record path:", full_record_path)
    print("Signal shape:", signal.shape)
    print("Lead names:", meta["sig_name"])
    print("Sampling rate:", meta["fs"])


if __name__ == "__main__":
    main()