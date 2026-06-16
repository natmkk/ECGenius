import matplotlib.pyplot as plt
import pandas as pd
import wfdb

from src.config import PTBXL_DIR, PROJECT_ROOT


def load_signal(ecg_id: int, metadata: pd.DataFrame):
    record_path = PTBXL_DIR / metadata.loc[ecg_id, "filename_lr"]
    signal, meta = wfdb.rdsamp(str(record_path))
    return signal, meta


def main() -> None:
    metadata = pd.read_csv("data/processed/ptbxl_binary_labels.csv", index_col="ecg_id")

    normal_id = 1
    abnormal_id = 8

    normal_signal, normal_meta = load_signal(normal_id, metadata)
    abnormal_signal, abnormal_meta = load_signal(abnormal_id, metadata)

    figures_dir = PROJECT_ROOT / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    output_path = figures_dir / "normal_vs_abnormal_lead1.png"

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(normal_signal[:, 0])
    plt.title(f"Normal ECG Example - ID {normal_id} - Lead {normal_meta['sig_name'][0]}")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(abnormal_signal[:, 0])
    plt.title(f"Abnormal ECG Example - ID {abnormal_id} - Lead {abnormal_meta['sig_name'][0]}")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()

    print("Saved figure to:", output_path)


if __name__ == "__main__":
    main()