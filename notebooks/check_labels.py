import pandas as pd

df = pd.read_csv("data/processed/ptbxl_binary_labels.csv")

print(df["binary_label"].value_counts(dropna=False))
print()
print(df[df["scp_codes"].str.contains("NORM", na=False)]["scp_codes"].head(20).to_string(index=False))