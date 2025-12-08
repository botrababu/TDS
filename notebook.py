# analysis.py
# 24f3000719@ds.study.iitm.ac.in
# Marimo interactive notebook with slider, dependencies, and dynamic markdown

import marimo

app = marimo.App()

# -------------------------------------------------------
# Cell 1: Load and generate data (used by later cells)
# -------------------------------------------------------
@app.cell
def generate_data():
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    n = 200
    departments = ["Finance", "Operations", "HR", "Marketing", "R&D", "Sales"]
    regions = ["Asia Pacific", "Latin America", "Middle East", "Europe", "North America"]

    df = pd.DataFrame({
        "employee_id": [f"EMP{i:03d}" for i in range(1, n+1)],
        "department": np.random.choice(departments, size=n),
        "region": np.random.choice(regions, size=n),
        "performance_score": np.round(np.random.normal(75, 10, n), 2),
        "years_experience": np.abs(np.round(np.random.normal(6, 4, n))).astype(int),
        "satisfaction_rating": np.round(np.clip(np.random.normal(4.0, 0.6, n), 1, 5), 2)
    })

    return df


# -------------------------------------------------------
# Cell 2: Define interactive slider widget (Marimo slider)
# -------------------------------------------------------
@app.cell
def slider_widget(mo):
    years_slider = mo.ui.slider(start=0, stop=20, value=5, step=1, label="Minimum Years Experience")
    return years_slider


# -------------------------------------------------------
# Cell 3: Reactive filtering based on slider value
# -------------------------------------------------------
@app.cell
def filtered_data(df, years_slider):
    filtered = df[df["years_experience"] >= years_slider.value]
    return filtered


# -------------------------------------------------------
# Cell 4: Dynamic markdown output based on slider state
# -------------------------------------------------------
@app.cell
def summary_markdown(filtered, years_slider, mo):
    md = f"""
    ### Dynamic Summary

    - **Minimum years selected:** {years_slider.value}  
    - **Filtered rows:** {len(filtered)}  
    - **Mean Performance Score:** {filtered['performance_score'].mean():.2f}  
    - **Median Satisfaction Rating:** {filtered['satisfaction_rating'].median():.2f}  
    """
    return mo.md(md)


# -------------------------------------------------------
# Cell 5: Plot depending on filtered data
# -------------------------------------------------------
@app.cell
def plot(filtered, mo):
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(filtered["performance_score"], kde=True, ax=ax)
    ax.set_title("Performance Score Distribution (Filtered)")
    mo.figure(fig)
    return


app.run()
