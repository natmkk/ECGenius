import joblib
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import train_test_split


def main() -> None:
    df = pd.read_csv("results/feature_table_1000.csv")

    X = df.drop(columns=["ecg_id", "binary_label"])
    y = df["binary_label"]

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

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)

    print(report)

    Path("figures").mkdir(parents=True, exist_ok=True)
    Path("models").mkdir(parents=True, exist_ok=True)
    Path("results").mkdir(parents=True, exist_ok=True)

    disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.title("Baseline Random Forest Confusion Matrix")
    plt.tight_layout()
    plt.savefig("figures/confusion_matrix_baseline.png", dpi=300)
    plt.show()

    joblib.dump(model, "models/random_forest_baseline.joblib")

    with open("results/classification_report_baseline.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Saved figure to: figures/confusion_matrix_baseline.png")
    print("Saved model to: models/random_forest_baseline.joblib")
    print("Saved report to: results/classification_report_baseline.txt")


if __name__ == "__main__":
    main()