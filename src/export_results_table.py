import json
import pandas as pd


def main() -> None:
    with open("results/metrics_summary.json", "r", encoding="utf-8") as f:
        metrics = json.load(f)

    results_df = pd.DataFrame(
        [
            {"metric": "Accuracy", "value": metrics["accuracy"]},
            {"metric": "Precision (abnormal)", "value": metrics["precision_abnormal"]},
            {"metric": "Recall (abnormal)", "value": metrics["recall_abnormal"]},
            {"metric": "F1-score (abnormal)", "value": metrics["f1_abnormal"]},
            {"metric": "ROC-AUC", "value": metrics["roc_auc"]},
            {"metric": "Number of samples", "value": metrics["n_samples"]},
            {"metric": "Number of features", "value": metrics["n_features"]},
        ]
    )

    results_df.to_csv("results/results_summary_table.csv", index=False)

    print(results_df.to_string(index=False))
    print("Saved table to: results/results_summary_table.csv")


if __name__ == "__main__":
    main()