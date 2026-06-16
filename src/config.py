from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

PTBXL_DIR = RAW_DIR / "ptbxl"
PTBXL_METADATA_CSV = PTBXL_DIR / "ptbxl_database.csv"
PTBXL_SCP_CSV = PTBXL_DIR / "scp_statements.csv"