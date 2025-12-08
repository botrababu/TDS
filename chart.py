import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic marketing data
def generate_data(n=400, seed=42):
    np.random.seed(seed)

    channels = ["Email", "Social", "Search", "Display"]
    channel = np.random.choice(channels, size=n, p=[0.25, 0.35, 0.25, 0.15])

    spend = np.random.normal(20, 8, n).clip(1)    # ad spend in thousands
    impressions = np.random.normal(150, 60, n).clip(10)  # impressions in thousands

    base_conv = {"Email": 0.03, "Social": 0.02, "Search": 0.04, "Display": 0.015}
    conv_rate = np.array([base_conv[c] for c in channel]) + 0.002 * np.log1p(spend) + np.random.normal(0, 0.003, n)
    conv_rate = conv_rate.clip(0.001, 0.15)

    df = pd.DataFrame({
        "channel": channel,
        "ad_spend_k": spend,
        "impressions_k": impressions,
        "conversion_rate": conv_rate
    })

    return df

# Create scatterplot
def create_chart():
    sns.set_style("whitegrid")
    sns.set_context("talk")

    df = generate_data()

    plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px
    sns.scatterplot(
        data=df,
        x="ad_spend_k",
        y="conversion_rate",
        hue="channel",
        size="impressions_k",
        sizes=(40, 300),
        alpha=0.85,
        palette="deep"
    )

    plt.title("Marketing Effectiveness: Ad Spend vs Conversion Rate")
    plt.xlabel("Ad Spend (in thousands USD)")
    plt.ylabel("Conversion Rate")

    plt.tight_layout()
    plt.savefig("chart.png", dpi=64, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    create_chart()
