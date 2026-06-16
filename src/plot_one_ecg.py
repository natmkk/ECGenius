import matplotlib.pyplot as plt
import pandas as pd
import wfdb

from src.config import PTBXL_DIR, PTBXL_METADATA_CSV, PROJECT_ROOT


def main() -> None:
    df = pd.read_csv(PTBXL_METADATA_CSV, index_col="ecg_id")
    first_path = df.iloc[0]["filename_lr"]
    full_record_path = PTBXL_DIR / first_path

    signal, meta = wfdb.rdsamp(str(full_record_path))

    figures_dir = PROJECT_ROOT / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    output_path = figures_dir / "example_ecg_lead1.png"

    plt.figure(figsize=(12, 6))
    plt.plot(signal[:, 0])
    plt.title(f"Example ECG - Lead {meta['sig_name'][0]}")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()

    print("Saved figure to:", output_path)


if __name__ == "__main__":
    main()