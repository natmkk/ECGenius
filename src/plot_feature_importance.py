import joblib
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def main() -> None:
    df = pd.read_csv("results/feature_table_1000.csv")
    model = joblib.load("models/random_forest_baseline.joblib")

    X = df.drop(columns=["ecg_id", "binary_label"])
    importances = model.feature_importances_

    importance_df = pd.DataFrame(
        {
            "feature": X.columns,
            "importance": importances,
        }
    ).sort_values("importance", ascending=False)

    top_features = importance_df.head(15)

    Path("results").mkdir(parents=True, exist_ok=True)
    importance_df.to_csv("results/feature_importance_baseline.csv", index=False)

    plt.figure(figsize=(10, 6))
    plt.barh(top_features["feature"][::-1], top_features["importance"][::-1])
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Top 15 Random Forest Feature Importances")
    plt.tight_layout()
    plt.savefig("figures/feature_importance_baseline.png", dpi=300)
    plt.show()

    print("Saved figure to: figures/feature_importance_baseline.png")
    print("Saved table to: results/feature_importance_baseline.csv")


if __name__ == "__main__":
    main()