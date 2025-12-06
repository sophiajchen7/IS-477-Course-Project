import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

def save_plot(fig, filename):
    Path("results/plots").mkdir(parents=True, exist_ok=True)
    fig.savefig(f"results/plots/{filename}", dpi=300, bbox_inches="tight")
    plt.close(fig)

def main():
    merged = pd.read_csv("data/processed/merged_counts.csv")

    violations = pd.read_csv("data/processed/violations_with_ca.csv")
    permits = pd.read_csv("data/processed/permits_with_ca.csv")

    violations["VIOLATION DATE"] = pd.to_datetime(violations["VIOLATION DATE"], errors="coerce")
    permits["ISSUE_DATE"] = pd.to_datetime(permits["ISSUE_DATE"], errors="coerce")

    violations["year"] = violations["VIOLATION DATE"].dt.year
    permits["year"] = permits["ISSUE_DATE"].dt.year

    viol_counts = (
        violations.groupby(["community_area", "year"])
        .size()
        .reset_index(name="violations")
    )
    permit_counts = (
        permits.groupby(["community_area", "year"])
        .size()
        .reset_index(name="permits")
    )

    # Heatmap of Violations (Community Area × Year)
    pivot_viol = viol_counts.pivot(index="community_area", columns="year", values="violations")

    fig1 = plt.figure(figsize=(14, 8))
    sns.heatmap(pivot_viol, cmap="viridis")
    plt.title("Heatmap of Violations by Community Area and Year")
    plt.xlabel("Year")
    plt.ylabel("Community Area")
    save_plot(fig1, "violations_heatmap.png")

    # Line Plot – Top 10 Community Areas by Violations
    top10_viol = viol_counts.groupby("community_area")["violations"].sum().nlargest(10).index

    fig2 = plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=viol_counts[viol_counts["community_area"].isin(top10_viol)],
        x="year", y="violations", hue="community_area", marker="o"
    )
    plt.title("Violations Over Time for Top 10 Community Areas")
    plt.xlabel("Year")
    plt.ylabel("Violations")
    save_plot(fig2, "top10_violations_trend.png")

    # Line Plot – Top 10 Community Areas by Permits
    top10_perm = permit_counts.groupby("community_area")["permits"].sum().nlargest(10).index

    fig3 = plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=permit_counts[permit_counts["community_area"].isin(top10_perm)],
        x="year", y="permits", hue="community_area", marker="o"
    )
    plt.title("Permits Over Time for Top 10 Community Areas")
    plt.xlabel("Year")
    plt.ylabel("Permits")
    save_plot(fig3, "top10_permits_trend.png")

    # Correlation Heatmap (Year, Permits, Violations)
    fig4 = plt.figure(figsize=(6, 4))
    sns.heatmap(
        merged[["year", "permits", "violations"]].corr(),
        annot=True, cmap="coolwarm"
    )
    plt.title("Correlation Matrix: Year, Permits, Violations")
    save_plot(fig4, "correlation_matrix.png")

    # Side-by-Side Maps (Violations, Permits)
    community_url = "https://data.cityofchicago.org/resource/igwz-8jzy.geojson"
    community_gdf = gpd.read_file(community_url)[["community", "area_numbe", "geometry"]]
    community_gdf = community_gdf.rename(columns={
        "community": "community_name",
        "area_numbe": "community_area"
    })

    viol_total = viol_counts.groupby("community_area")["violations"].sum().reset_index()
    perm_total = permit_counts.groupby("community_area")["permits"].sum().reset_index()

    community_gdf["community_area"] = community_gdf["community_area"].astype(int)
    viol_total["community_area"] = viol_total["community_area"].astype(int)
    perm_total["community_area"] = perm_total["community_area"].astype(int)

    viol_map = community_gdf.merge(viol_total, on="community_area", how="left").fillna(0)
    perm_map = community_gdf.merge(perm_total, on="community_area", how="left").fillna(0)

    fig5, axes = plt.subplots(1, 2, figsize=(20, 10))

    viol_map.plot(column="violations", cmap="Reds", linewidth=0.5, edgecolor="black",
                  legend=True, ax=axes[0])
    axes[0].set_title("Violations by Community Area")
    axes[0].axis("off")

    perm_map.plot(column="permits", cmap="Blues", linewidth=0.5, edgecolor="black",
                  legend=True, ax=axes[1])
    axes[1].set_title("Permits by Community Area")
    axes[1].axis("off")

    save_plot(fig5, "violations_vs_permits_map.png")

    # Boxplot – Violations by Year
    fig6 = plt.figure(figsize=(10, 5))
    sns.boxplot(data=viol_counts, x="year", y="violations")
    plt.title("Distribution of Violations by Year")
    plt.xticks(rotation=45)
    save_plot(fig6, "violations_boxplot.png")

    print("Analysis complete! All plots saved to results/plots/")

if __name__ == "__main__":
    main()
