import numpy as np
import pandas as pd
import wfdb

from src.config import PTBXL_DIR, PTBXL_METADATA_CSV, PROJECT_ROOT


def extract_basic_features(signal: np.ndarray) -> dict[str, float]:
    features = {}

    for lead_idx in range(signal.shape[1]):
        lead = signal[:, lead_idx]
        features[f"lead_{lead_idx+1}_mean"] = float(np.mean(lead))
        features[f"lead_{lead_idx+1}_std"] = float(np.std(lead))
        features[f"lead_{lead_idx+1}_min"] = float(np.min(lead))
        features[f"lead_{lead_idx+1}_max"] = float(np.max(lead))
        features[f"lead_{lead_idx+1}_rms"] = float(np.sqrt(np.mean(lead**2)))

    return features


def main() -> None:
    df = pd.read_csv(PTBXL_METADATA_CSV, index_col="ecg_id")
    first_path = df.iloc[0]["filename_lr"]
    full_record_path = PTBXL_DIR / first_path

    signal, _ = wfdb.rdsamp(str(full_record_path))
    features = extract_basic_features(signal)

    features_df = pd.DataFrame([features])

    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    output_path = results_dir / "sample_features.csv"

    features_df.to_csv(output_path, index=False)

    print(features_df.head())
    print("Saved features to:", output_path)


if __name__ == "__main__":
    main()