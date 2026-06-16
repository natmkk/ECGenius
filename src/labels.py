import pandas as pd


def _is_normal_record(scp_codes: dict) -> bool:
    if not isinstance(scp_codes, dict) or not scp_codes:
        return False
    return "NORM" in scp_codes


def add_binary_normal_abnormal_label(df: pd.DataFrame) -> pd.DataFrame:
    labeled_df = df.copy()
    labeled_df["binary_label"] = df["scp_codes"].apply(
        lambda codes: "normal" if _is_normal_record(codes) else "abnormal"
    )
    return labeled_df