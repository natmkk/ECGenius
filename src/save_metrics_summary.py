import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split


def main() -> None:
    df = pd.read_csv("results/feature_table_1000.csv")

    X = df.drop(columns=["ecg_id", "binary_label"])
    y_text = df["binary_label"]
    y = (y_text == "abnormal").astype(int)

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
    y_score = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision_abnormal": round(float(precision_score(y_test, y_pred)), 4),
        "recall_abnormal": round(float(recall_score(y_test, y_pred)), 4),
        "f1_abnormal": round(float(f1_score(y_test, y_pred)), 4),
        "roc_auc": round(float(roc_auc_score(y_test, y_score)), 4),
        "n_samples": int(len(df)),
        "n_features": int(X.shape[1]),
    }

    with open("results/metrics_summary.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(metrics)
    print("Saved metrics to: results/metrics_summary.json")


if __name__ == "__main__":
    main()