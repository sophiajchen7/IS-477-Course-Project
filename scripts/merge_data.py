import pandas as pd
from pathlib import Path

def main():
    viol = pd.read_csv("data/processed/violations_with_ca.csv")
    perm = pd.read_csv("data/processed/permits_with_ca.csv")

    # Convert dates + extract years
    viol["VIOLATION DATE"] = pd.to_datetime(viol["VIOLATION DATE"], errors="coerce")
    perm["ISSUE_DATE"] = pd.to_datetime(perm["ISSUE_DATE"], errors="coerce")

    viol["year"] = viol["VIOLATION DATE"].dt.year
    perm["year"] = perm["ISSUE_DATE"].dt.year

    # Group counts
    viol_counts = (
        viol.groupby(["community_area", "year"])
        .size()
        .reset_index(name="violations")
    )
    perm_counts = (
        perm.groupby(["community_area", "year"])
        .size()
        .reset_index(name="permits")
    )

    merged = perm_counts.merge(viol_counts, on=["community_area", "year"], how="inner")

    Path("data/processed").mkdir(exist_ok=True)
    merged.to_csv("data/processed/merged_counts.csv", index=False)
    print("Merged dataset saved → data/processed/merged_counts.csv")

if __name__ == "__main__":
    main()
