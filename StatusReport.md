from sodapy import Socrata
import pandas as pd

client = Socrata("data.cityofchicago.org", app_token="5ah8bJgzgJRVbFDfj4VUGVz0s")

violations_results = client.get(
    "22u3-xenr",
    where="inspection_category='PERMIT'",
    limit=50000 
)

violations_df = pd.DataFrame.from_records(violations_results)
print("Violations loaded:", violations_df.shape)

permits_results = client.get(
    "ydr8-5enu",
    limit=50000
)

permits_df = pd.DataFrame.from_records(permits_results)
print("Permits loaded:", permits_df.shape)

violations_df.columns = violations_df.columns.str.lower().str.strip().str.replace(" ", "_")
permits_df.columns = permits_df.columns.str.lower().str.strip().str.replace(" ", "_")
violations_df["violation_date"] = pd.to_datetime(violations_df["violation_date"], errors="coerce")
permits_df["issue_date"] = pd.to_datetime(permits_df["issue_date"], errors="coerce")

violations_df["year"] = violations_df["violation_date"].dt.year
permits_df["year"] = permits_df["issue_date"].dt.year

violations_df = violations_df[violations_df["year"] >= 2015]
permits_df = permits_df[permits_df["year"] >= 2015]


for col in ["latitude", "longitude", "community_area"]:
    if col in permits_df.columns:
        permits_df[col] = pd.to_numeric(permits_df[col], errors="coerce")
    if col in violations_df.columns:
        violations_df[col] = pd.to_numeric(violations_df[col], errors="coerce")

permits_summary = (
    permits_df.groupby("year")
    .size()
    .reset_index(name="num_permits")
)

violations_summary = (
    violations_df.groupby("year")
    .size()
    .reset_index(name="num_violations")
)

merged_df = pd.merge(permits_summary, violations_summary, on="year", how="inner")
print("\nMerged data (first few rows):")
print(merged_df.head())
