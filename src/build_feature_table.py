import numpy as np
import pandas as pd
import wfdb

from src.config import PTBXL_DIR, PROJECT_ROOT


def extract_basic_features(signal: np.ndarray) -> dict[str, float]:
    features = {}

    for lead_idx in range(signal.shape[1]):
        lead = signal[:, lead_idx]
        lead_num = lead_idx + 1
        features[f"lead_{lead_num}_mean"] = float(np.mean(lead))
        features[f"lead_{lead_num}_std"] = float(np.std(lead))
        features[f"lead_{lead_num}_min"] = float(np.min(lead))
        features[f"lead_{lead_num}_max"] = float(np.max(lead))
        features[f"lead_{lead_num}_rms"] = float(np.sqrt(np.mean(lead ** 2)))

    return features


def main() -> None:
    metadata = pd.read_csv("data/processed/ptbxl_binary_labels.csv", index_col="ecg_id")
    subset = metadata.head(1000).copy()

    rows = []

    for ecg_id, row in subset.iterrows():
        record_path = PTBXL_DIR / row["filename_lr"]
        signal, _ = wfdb.rdsamp(str(record_path))

        features = extract_basic_features(signal)
        features["ecg_id"] = ecg_id
        features["binary_label"] = row["binary_label"]
        rows.append(features)

    feature_df = pd.DataFrame(rows)

    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    output_path = results_dir / "feature_table_1000.csv"
    
    feature_df.to_csv(output_path, index=False)

    print(feature_df.head())
    print("Feature table shape:", feature_df.shape)
    print("Saved feature table to:", output_path)


if __name__ == "__main__":
    main()