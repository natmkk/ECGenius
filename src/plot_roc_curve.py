import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split


def main() -> None:
    df = pd.read_csv("results/feature_table_1000.csv")

    X = df.drop(columns=["ecg_id", "binary_label"])
    y = (df["binary_label"] == "abnormal").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )
    model.fit(X_train, y_train)

    y_score = model.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6, 6))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0, 1], [0, 1], linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Baseline Random Forest")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("figures/roc_curve_baseline.png", dpi=300)
    plt.show()

    print("Saved figure to: figures/roc_curve_baseline.png")
    print(f"ROC AUC: {roc_auc:.3f}")


if __name__ == "__main__":
    main()