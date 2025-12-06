import requests
from pathlib import Path

def download_csv(url, path, limit=1000):
    params = {"$limit": limit}
    response = requests.get(url, params=params)
    response.raise_for_status()

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(response.content)
    print(f"Saved → {path}")

def main():
    violations_url = "https://data.cityofchicago.org/api/views/22u3-xenr/rows.csv"
    permits_url = "https://data.cityofchicago.org/api/views/ydr8-5enu/rows.csv"

    download_csv(violations_url, "data/raw/violations.csv")
    download_csv(permits_url, "data/raw/permits.csv")

    # community areas GeoJSON will download later directly in clean_data
    print("Data acquisition complete.")

if __name__ == "__main__":
    main()
