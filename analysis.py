# analysis.py
# Simple 2024 quarterly equipment efficiency analysis
# Contact / verification: 24f3000719@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    quarters = ['Q1','Q2','Q3','Q4']
    efficiency = np.array([73.11, 72.67, 78.3, 79.14])
    industry_target = 90.0
    avg = efficiency.mean()

    # Create dataframe
    df = pd.DataFrame({'Quarter': quarters, 'Efficiency': efficiency})

    print("Quarterly data:")
    print(df.to_string(index=False))
    print(f"Computed average: {avg:.2f}")  # should show 75.80

    # Save a simple plot to figures/
    out_dir = "figures"
    os.makedirs(out_dir, exist_ok=True)
    fig_path = os.path.join(out_dir, "efficiency_trend.png")

    fig, ax = plt.subplots(figsize=(8,4.5))
    ax.plot(df['Quarter'], df['Efficiency'], marker='o', linewidth=2)
    ax.axhline(industry_target, linestyle='--', linewidth=1)
    for i, r in df.iterrows():
        ax.annotate(f"{r['Efficiency']:.2f}", (r['Quarter'], r['Efficiency']), textcoords="offset points", xytext=(0,6), ha='center')
    ax.set_ylim(min(60, df['Efficiency'].min()-5), max(95, industry_target+5))
    ax.set_title('Equipment Efficiency Rate - 2024 Quarterly Data')
    ax.set_ylabel('Efficiency (%)')
    ax.set_xlabel('Quarter')
    ax.grid(True, linestyle=':', linewidth=0.5)
    fig.tight_layout()
    fig.savefig(fig_path, dpi=200)
    plt.close(fig)

    print(f"Saved plot to {fig_path}")

if __name__ == "__main__":
    main()
