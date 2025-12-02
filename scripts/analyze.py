import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROC_DIR = "data/processed"
PLOTS_DIR = "results/plots"

def save_plot(fig, path):
    os.makedirs(PLOTS_DIR, exist_ok=True)
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

def main():
    os.makedirs(PLOTS_DIR, exist_ok=True)

    merged_path = os.path.join(PROC_DIR, "merged.csv")
    df = pd.read_csv(merged_path)

    df["issue_date"] = pd.to_datetime(df["issue_date"], errors="coerce")
    df["violation_date"] = pd.to_datetime(df["violation_date"], errors="coerce")

    df["issue_year"] = df["issue_date"].dt.year
    df["violation_year"] = df["violation_date"].dt.year

    # line plot of permits per year
    permits_year = df.groupby("issue_year").size()
    fig1 = plt.figure()
    permits_year.plot(kind="line", marker="o")
    plt.title("Number of Permits per Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    save_plot(fig1, f"{PLOTS_DIR}/permits_per_year.png")

    # line plot of violations per year 
    violations_year = df.groupby("violation_year").size()
    fig2 = plt.figure()
    violations_year.plot(kind="line", marker="o", color="red")
    plt.title("Number of Violations per Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    save_plot(fig2, f"{PLOTS_DIR}/violations_per_year.png")

    # top 20 streets with most permits & violations
    top_permits = df["street_name"].value_counts().head(20)
    top_violations = df["street_name"].value_counts().head(20)

    fig3, ax = plt.subplots(figsize=(10, 6))
    top_permits.plot(kind="bar", ax=ax, color="blue", alpha=0.7)
    plt.title("Top 20 Streets by Number of Permits")
    plt.xlabel("Street")
    plt.ylabel("Count")
    plt.xticks(rotation=75)
    save_plot(fig3, f"{PLOTS_DIR}/top20_permits_streets.png")

    fig4, ax = plt.subplots(figsize=(10, 6))
    top_violations.plot(kind="bar", ax=ax, color="orange", alpha=0.7)
    plt.title("Top 20 Streets by Number of Violations")
    plt.xlabel("Street")
    plt.ylabel("Count")
    plt.xticks(rotation=75)
    save_plot(fig4, f"{PLOTS_DIR}/top20_violations_streets.png")

    # scatterplot of permits vs violations by year
    combined = pd.DataFrame({
        "permits": permits_year,
        "violations": violations_year
    }).dropna()

    fig5 = plt.figure()
    sns.scatterplot(x="permits", y="violations", data=combined)
    plt.title("Scatter Plot: Permits vs Violations by Year")
    save_plot(fig5, f"{PLOTS_DIR}/scatter_permits_violations.png")

    # Heatmap 
    fig6 = plt.figure()
    sns.heatmap(combined.corr(), annot=True)
    plt.title("Correlation Between Permits and Violations")
    save_plot(fig6, f"{PLOTS_DIR}/correlation_heatmap.png")

    # combined top 20 streets 
    permits_counts = df["street_name"].value_counts()
    violations_counts = df["street_name"].value_counts()

    combined_streets = pd.DataFrame({
        "permits": permits_counts,
        "violations": violations_counts
    }).fillna(0)

    combined_streets["total"] = combined_streets["permits"] + combined_streets["violations"]
    top20_combined = combined_streets.sort_values("total", ascending=False).head(20)

    fig7, ax = plt.subplots(figsize=(12, 7))
    width = 0.4
    x = range(len(top20_combined))

    ax.bar(
        [p - width/2 for p in x],
        top20_combined["permits"],
        width=width,
        label="Permits",
        color="steelblue"
    )
    ax.bar(
        [p + width/2 for p in x],
        top20_combined["violations"],
        width=width,
        label="Violations",
        color="orange"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(top20_combined.index, rotation=75, ha="right")
    ax.set_ylabel("Count")
    ax.set_title("Top 20 Streets by Combined Permits + Violations")
    ax.legend()

    save_plot(fig7, f"{PLOTS_DIR}/top20_combined_permits_violations.png")

if __name__ == "__main__":
    main()
