import pandas as pd
import geopandas as gpd
from pathlib import Path
from shapely.geometry import Point

def assign_community_area(df, community_gdf, lat_col, lon_col):
    df = df.dropna(subset=[lat_col, lon_col])
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
        crs="EPSG:4326"
    )
    joined = gpd.sjoin(gdf, community_gdf, how="left", predicate="within")
    return joined.drop(columns=["index_right"])

def main():
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    # Load raw datasets
    violations = pd.read_csv("data/raw/violations.csv")
    permits = pd.read_csv("data/raw/permits.csv")

    # Load community area boundaries
    community_url = "https://data.cityofchicago.org/resource/igwz-8jzy.geojson"
    community_gdf = gpd.read_file(community_url)[["community", "area_numbe", "geometry"]]
    community_gdf = community_gdf.rename(columns={
        "community": "community_name",
        "area_numbe": "community_area"
    })

    # Assign community areas
    viol_ca = assign_community_area(
        violations, community_gdf, lat_col="LATITUDE", lon_col="LONGITUDE"
    )
    perm_ca = assign_community_area(
        permits, community_gdf, lat_col="LATITUDE", lon_col="LONGITUDE"
    )

    # Save intermediate
    viol_ca.to_csv("data/processed/violations_with_ca.csv", index=False)
    perm_ca.to_csv("data/processed/permits_with_ca.csv", index=False)
    print("Cleaned data with community areas saved.")

if __name__ == "__main__":
    main()
