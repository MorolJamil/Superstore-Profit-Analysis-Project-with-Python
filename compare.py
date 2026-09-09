"""
compare.py -- Q3: Region & category performance
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path("charts").mkdir(exist_ok=True)
df = pd.read_csv("data/superstore.csv", parse_dates=["Order Date"])

def margin_table(df, by):
    t = df.groupby(by).agg(total_sales=("Sales", "sum"), total_profit=("Profit", "sum"))
    t["profit_margin_pct"] = t["total_profit"] / t["total_sales"] * 100
    return t.sort_values("total_sales", ascending=False)

by_region = margin_table(df, "Region")
by_category = margin_table(df, "Category")
print(by_region.round(2))
print(by_category.round(2))
print("Best region by margin:", by_region["profit_margin_pct"].idxmax())
print("Worst region by margin:", by_region["profit_margin_pct"].idxmin())

fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.barh(by_region.index, by_region["profit_margin_pct"])
fig1.savefig("charts/profit_by_region.png", dpi=150)

fig2, ax2 = plt.subplots(figsize=(7.5, 5.5))
for cat, row in by_category.iterrows():
    ax2.scatter(row["total_sales"], row["profit_margin_pct"], s=300, label=cat)
ax2.legend()
fig2.savefig("charts/profit_by_category.png", dpi=150)