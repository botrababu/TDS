# equipment_efficiency_analysis - Q4 2024
# Author: Generated for user; contact: 24f3000719@ds.study.iitm.ac.in
# Purpose: process quarterly equipment efficiency data, visualize trend, compare to benchmark,
# and provide a simple projection and recommendation (predictive maintenance).

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

quarters = ['Q1','Q2','Q3','Q4']
efficiency = np.array([73.11, 72.67, 78.3, 79.14])
industry_target = 90.0
avg = efficiency.mean()

df = pd.DataFrame({'Quarter': quarters, 'Efficiency': efficiency})

def save_plot(path='figures/efficiency_trend.png'):
    fig, ax = plt.subplots(figsize=(8,4.5))
    ax.plot(df['Quarter'], df['Efficiency'], marker='o')
    ax.axhline(industry_target, linestyle='--', linewidth=1)
    for i,r in df.iterrows():
        ax.annotate(f"{r['Efficiency']:.2f}", (r['Quarter'], r['Efficiency']), textcoords="offset points", xytext=(0,6), ha='center')
    ax.set_ylim(min(60, df['Efficiency'].min()-5), max(95, industry_target+5))
    ax.set_title('Equipment Efficiency Rate - 2024 Quarterly Data')
    ax.set_ylabel('Efficiency (%)')
    ax.set_xlabel('Quarter')
    ax.grid(True, linestyle=':', linewidth=0.5)
    fig.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=200)
    plt.close(fig)
    print(f"Saved plot to {path}")

def simple_projection():
    # Use quarter index as X (0..3) to fit a linear model and project forward
    X = np.arange(len(efficiency)).reshape(-1,1)
    y = efficiency
    model = LinearRegression()
    model.fit(X,y)
    # predict how many additional quarters needed to reach target (project line)
    # Solve for x where model.predict(x) = industry_target
    coef = model.coef_[0]
    intercept = model.intercept_
    if coef <= 0:
        return None, coef, intercept
    x_needed = (industry_target - intercept) / coef
    quarters_needed_from_start = x_needed
    additional_quarters = quarters_needed_from_start - (len(efficiency)-1)
    return max(additional_quarters, 0), coef, intercept

if __name__ == '__main__':
    print('Dataframe:')
    print(df.to_string(index=False))
    print(f'Computed average: {avg:.2f}')
    save_plot()
    proj, coef, intercept = simple_projection()
    if proj is None:
        print('Projection indicates no positive trend; targeted improvement requires interventions.')
    else:
        print(f'Linear trend coef={coef:.4f}, intercept={intercept:.2f}')
        print(f'Estimated additional quarters to reach {industry_target}% (if trend continues): {proj:.2f}')
