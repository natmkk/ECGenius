from src.load_data import inspect_dataset, load_ptbxl_metadata, save_processed_metadata
from src.labels import add_binary_normal_abnormal_label


def main() -> None:
    df, scp_df = load_ptbxl_metadata()
    inspect_dataset(df, scp_df)

    labeled_df = add_binary_normal_abnormal_label(df)
    print("\nBinary class counts:")
    print(labeled_df["binary_label"].value_counts(dropna=False))

    save_processed_metadata(labeled_df)
    print("\nSaved processed metadata for the next step.")


if __name__ == "__main__":
    main()