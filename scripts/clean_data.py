import os
import pandas as pd

RAW_DIR = "data/raw"
PROC_DIR = "data/processed"

def clean_permits(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()

    # Convert dates
    if "issue_date" in df.columns:
        df["issue_date"] = pd.to_datetime(df["issue_date"], errors="coerce")

    # Normalize street names if present
    if "street_name" in df.columns:
        df["street_name"] = (
            df["street_name"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    return df

def clean_violations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()

    if "violation_date" in df.columns:
        df["violation_date"] = pd.to_datetime(df["violation_date"], errors="coerce")

    if "street_name" in df.columns:
        df["street_name"] = (
            df["street_name"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    return df

def main():
    os.makedirs(PROC_DIR, exist_ok=True)

    permits = pd.read_csv(os.path.join(RAW_DIR, "permits_raw.csv"))
    violations = pd.read_csv(os.path.join(RAW_DIR, "violations_raw.csv"))

    permits_clean = clean_permits(permits)
    violations_clean = clean_violations(violations)

    permits_clean.to_csv(os.path.join(PROC_DIR, "permits_clean.csv"), index=False)
    violations_clean.to_csv(os.path.join(PROC_DIR, "violations_clean.csv"), index=False)

    print("Cleaned files saved to data/processed/")

if __name__ == "__main__":
    main()
