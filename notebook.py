# 24f3000719@ds.study.iitm.ac.in
# Marimo/Jupyter-style interactive analysis script
#
# This script is written as a multi-cell ("# %%") Python file so it can be opened
# in VS Code's Interactive window, Jupyter, or any runner that supports cell markers.
#
# Requirements satisfied:
# - Email included above
# - At least two cells with variable dependencies
# - Interactive slider widget (ipywidgets)
# - Dynamic markdown output updated based on widget state
# - Comments document data flow between cells

# %%
# Cell 1 — Dependencies: data generation
# Data flow: This cell creates `df` (pandas DataFrame) and summary statistics.
# Subsequent cells read `df` to build visualizations and calculations.
import numpy as np
import pandas as pd

# For interactive display
from IPython.display import display, Markdown, clear_output

# Create a reproducible synthetic dataset for the demo
np.random.seed(42)
n = 200
departments = ["Finance", "Operations", "HR", "Marketing", "R&D", "Sales"]
regions = ["Asia Pacific", "Latin America", "Middle East", "Europe", "North America"]

df = pd.DataFrame({
    "employee_id": [f"EMP{i:03d}" for i in range(1, n+1)],
    "department": np.random.choice(departments, size=n, p=[0.15, 0.25, 0.12, 0.18, 0.12, 0.18]),
    "region": np.random.choice(regions, size=n),
    "performance_score": np.round(np.random.normal(75, 10, size=n), 2),
    "years_experience": np.abs(np.round(np.random.normal(6, 4, size=n))).astype(int),
    "satisfaction_rating": np.round(np.clip(np.random.normal(4.0, 0.6, size=n), 1.0, 5.0), 2)
})

# Basic summary used by later cells
department_counts = df["department"].value_counts().sort_index()
overall_mean_perf = df["performance_score"].mean()

# Display a quick summary so the user knows the data is loaded
display(Markdown("### Dataset summary (from Cell 1)"))
display(Markdown(f"- Rows: **{len(df)}**"))
display(Markdown(f"- Departments: **{', '.join(sorted(df['department'].unique()))}**"))
display(Markdown(f"- Overall mean performance score: **{overall_mean_perf:.2f}**"))

# %%
# Cell 2 — Dependencies: uses `df`, `department_counts` from Cell 1
# Data flow: This cell defines an interactive UI that depends on the dataset produced above.
# When the slider changes, the function reads `df` and recomputes summaries and dynamic markdown.
import ipywidgets as widgets
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("talk")

# Create an IntSlider to filter by minimum years of experience
years_slider = widgets.IntSlider(
    value=0,
    min=0,
    max=int(df["years_experience"].max()),
    step=1,
    description="Min Years:",
    continuous_update=False
)

# A dropdown for department selection that depends on department list from df
dept_dropdown = widgets.Dropdown(
    options=["All"] + sorted(df["department"].unique().tolist()),
    value="All",
    description="Department:"
)

# Output widget to display dynamic markdown and plots
out = widgets.Output()

def update_visualization(min_years, department):
    """
    This function is triggered when the slider or dropdown changes.
    It reads the global `df` (created in Cell 1), filters according to the inputs,
    computes summary metrics, and renders a markdown summary and a matplotlib plot.
    """
    # Clear previous output
    out.clear_output()
    # Filter the dataframe based on widget state (dependency on df)
    filtered = df[df["years_experience"] >= min_years]
    if department != "All":
        filtered = filtered[filtered["department"] == department]
    # Compute derived metrics
    count = len(filtered)
    mean_perf = filtered["performance_score"].mean() if count > 0 else float("nan")
    median_sat = filtered["satisfaction_rating"].median() if count > 0 else float("nan")

    # With the Output widget, produce dynamic markdown and a plot
    with out:
        clear_output(wait=True)
        display(Markdown(f"## Dynamic Summary (Min Years = **{min_years}**, Department = **{department}**)"))
        display(Markdown(f"- Filtered rows: **{count}**"))
        if count > 0:
            display(Markdown(f"- Mean performance score: **{mean_perf:.2f}**"))
            display(Markdown(f"- Median satisfaction rating: **{median_sat:.2f}**"))
        else:
            display(Markdown("- No data after filtering."))

        # Create a small figure showing distribution of performance_score in the filtered sample
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.histplot(filtered["performance_score"], kde=True, ax=ax, color="#2b8cbe", edgecolor="white")
        ax.set_xlabel("Performance Score")
        ax.set_ylabel("Count")
        ax.set_title("Performance Distribution (filtered)")
        plt.tight_layout()
        display(fig)
        plt.close(fig)

# Connect widgets to the callback. This ensures variable dependency and dynamic output.
controls = widgets.HBox([years_slider, dept_dropdown])
ui = widgets.VBox([controls, out])

# Wire up observers so the UI updates whenever widget state changes
def _on_change(change):
    update_visualization(years_slider.value, dept_dropdown.value)

years_slider.observe(_on_change, names="value")
dept_dropdown.observe(_on_change, names="value")

# Initialize with default parameters
update_visualization(years_slider.value, dept_dropdown.value)

# Display the UI in notebook environments
display(Markdown("### Interactive controls (Cell 2)"))
display(ui)

# %%
# Cell 3 — Dependencies: demonstrates saving a small CSV subset based on last widget state
# Data flow: reads `years_slider` and `dept_dropdown` values to produce a downloadable CSV
from IPython.display import FileLink

def save_filtered_csv(min_years=years_slider.value, department=dept_dropdown.value, filename="filtered_sample.csv"):
    """
    Saves the current filtered dataset to a CSV file (for sharing / reproducibility).
    This cell depends on the widget state (so it should be run after the widgets are created/used).
    """
    filtered = df[df["years_experience"] >= min_years]
    if department != "All":
        filtered = filtered[filtered["department"] == department]
    filtered.to_csv(filename, index=False)
    return filename

# Provide a simple one-click button to save the CSV (works in notebook)
save_button = widgets.Button(description="Save filtered CSV", button_style="success")
save_out = widgets.Output()

def on_save_clicked(b):
    save_out.clear_output()
    filename = save_filtered_csv()
    with save_out:
        display(Markdown(f"- Saved filtered CSV to **{filename}**."))
        display(FileLink(filename))

save_button.on_click(on_save_clicked)

display(Markdown("### Save current filtered selection (Cell 3)"))
display(widgets.HBox([save_button, save_out]))

# End of notebook
