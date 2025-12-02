import os
import pandas as pd

PROC_DIR = "data/processed"

def main():
    permits_path = os.path.join(PROC_DIR, "permits_clean.csv")
    violations_path = os.path.join(PROC_DIR, "violations_clean.csv")

    permits = pd.read_csv(permits_path)
    violations = pd.read_csv(violations_path)

    if "street_name" not in permits.columns or "street_name" not in violations.columns:
        raise ValueError("street_name column missing in one of the datasets.")

    merged = permits.merge(
        violations,
        on="street_name",
        how="inner",
        suffixes=("_permit", "_violation")
    )

    out_path = os.path.join(PROC_DIR, "merged.csv")
    merged.to_csv(out_path, index=False)
    print(f"Merged dataset saved to {out_path}")

if __name__ == "__main__":
    main()
