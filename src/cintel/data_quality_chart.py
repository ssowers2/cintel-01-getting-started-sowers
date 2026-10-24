"""Create a bar chart showing missing values in fictional healthcare department records."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt

# Locate the CSV file and output folder
ROOT_DIR = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT_DIR / "data" / "department_records.csv"
OUTPUT_DIR = ROOT_DIR / "docs" / "images"

# Read the fictional department records
with CSV_PATH.open(newline="", encoding="utf-8") as file:
    records = list(csv.DictReader(file))

# Count missing values in each field
fields = ["RecordID", "Department", "Status"]
missing_counts = [sum(record[field] == "" for record in records) for field in fields]

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(
    fields,
    missing_counts,
    color="#40C9C6",  # Turquoise
    edgecolor="#176B70",  # Dark teal outline
    linewidth=1.5,
    width=0.55,
)

ax.set_title("Missing Values by Field", fontsize=15, fontweight="bold", pad=18)
ax.set_xlabel("CSV Field", fontsize=11)
ax.set_ylabel("Number of Missing Values", fontsize=11)
ax.set_ylim(0, 3)
ax.set_yticks([0, 1, 2, 3])

ax.bar_label(bars, padding=4, fontsize=11, fontweight="bold")

# Remove unnecessary chart borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Save the chart
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_path = OUTPUT_DIR / "missing_values_chart.png"

fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Chart saved to: {output_path}")
