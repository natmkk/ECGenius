import pandas as pd


def main() -> None:
    df = pd.read_csv("data/processed/ptbxl_binary_labels.csv", index_col="ecg_id")

    normal_examples = df[df["binary_label"] == "normal"].head(3)
    abnormal_examples = df[df["binary_label"] == "abnormal"].head(3)

    print("Normal example ECG IDs:")
    print(normal_examples.index.tolist())

    print("\nAbnormal example ECG IDs:")
    print(abnormal_examples.index.tolist())


if __name__ == "__main__":
    main()