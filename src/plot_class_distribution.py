import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def main() -> None:
    df = pd.read_csv("results/feature_table_1000.csv")

    counts = df["binary_label"].value_counts()

    Path("figures").mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.title("Class Distribution in Feature Table")
    plt.tight_layout()
    plt.savefig("figures/class_distribution_1000.png", dpi=300)
    plt.show()

    print("Saved figure to: figures/class_distribution_1000.png")


if __name__ == "__main__":
    main()