import os
import pandas as pd
from sodapy import Socrata

PERMITS_ID = "ydr8-5enu"
VIOLATIONS_ID = "22u3-xenr"

LIMIT = 200000 

def get_client():
    """
    Creates a Socrata client using an environment variable for the APP TOKEN.
    """
    app_token = os.environ.get("CHICAGO_APP_TOKEN") 
    return Socrata("data.cityofchicago.org", app_token)

def download_dataset(dataset_id: str, path: str):
    """
    Downloads a dataset from Chicago Data Portal and saves it as CSV.
    """
    client = get_client()
    print(f"Downloading {dataset_id} .. .")
    results = client.get(dataset_id, limit=LIMIT)
    df = pd.DataFrame.from_records(results)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved → {path}")

def main():
    download_dataset(PERMITS_ID, "data/raw/permits_raw.csv")
    download_dataset(VIOLATIONS_ID, "data/raw/violations_raw.csv")

if __name__ == "__main__":
    main()
