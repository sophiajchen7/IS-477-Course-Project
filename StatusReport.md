import requests
import pandas as pd
from pathlib import Path

Path("data").mkdir(exist_ok=True)

violations_url = "https://data.cityofchicago.org/api/views/22u3-xenr/rows.csv"
permits_url = "https://data.cityofchicago.org/api/views/ydr8-5enu/rows.csv"

params = {"$limit": 10000}

violations_response = requests.get(violations_url, params=params)
violations_path = Path("data/violations.csv")
with open(violations_path, "wb") as f:
    f.write(violations_response.content)

permits_response = requests.get(permits_url, params=params)
permits_path = Path("data/permits.csv")
with open(permits_path, "wb") as f:
    f.write(permits_response.content)

violations_df = pd.read_csv(violations_path)
permits_df = pd.read_csv(permits_path)

print("Violations shape:", violations_df.shape)
print("Permits shape:", permits_df.shape)

