import matplotlib.pyplot as plt
import pandas as pd
import wfdb

from src.config import PTBXL_DIR, PTBXL_METADATA_CSV, PROJECT_ROOT


def main() -> None:
    df = pd.read_csv(PTBXL_METADATA_CSV, index_col="ecg_id")
    first_path = df.iloc[0]["filename_lr"]
    full_record_path = PTBXL_DIR / first_path

    signal, meta = wfdb.rdsamp(str(full_record_path))
    lead_names = meta["sig_name"]

    figures_dir = PROJECT_ROOT / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    output_path = figures_dir / "example_ecg_12lead.png"

    fig, axes = plt.subplots(12, 1, figsize=(12, 18), sharex=True)

    for i in range(12):
        axes[i].plot(signal[:, i])
        axes[i].set_ylabel(lead_names[i], rotation=0, labelpad=20)
        axes[i].grid(True)

    axes[-1].set_xlabel("Sample")
    fig.suptitle("Example 12-Lead ECG", fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()

    print("Saved figure to:", output_path)


if __name__ == "__main__":
    main()