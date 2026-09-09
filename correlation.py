"""
correlation.py -- Q2: Does discount help or hurt profit?
Pearson r, then a discount-bucket breakdown to find where profit turns negative.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path("charts").mkdir(exist_ok=True)
df = pd.read_csv("data/superstore.csv", parse_dates=["Order Date"])

r = df["Discount"].corr(df["Profit"])
print(f"Pearson r(discount, profit) = {r:.3f}")

bins = [-0.01, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.81]
labels = ["0%","10%","20%","30%","40%","50%","60%","70%","80%"]
df["Discount_Bucket"] = pd.cut(df["Discount"], bins=bins, labels=labels)

by_bucket = df.groupby("Discount_Bucket", observed=True).agg(
    avg_profit=("Profit", "mean"),
    orders=("Profit", "count"),
)
sales_by_bucket = df.groupby("Discount_Bucket", observed=True)["Sales"].sum()
profit_by_bucket = df.groupby("Discount_Bucket", observed=True)["Profit"].sum()
by_bucket["margin_pct"] = (profit_by_bucket / sales_by_bucket * 100).round(1)
print(by_bucket.round(2))

fig, ax = plt.subplots(figsize=(9, 5.5))
for cat, group in df.groupby("Category"):
    ax.scatter(group["Discount"], group["Profit"], s=10, alpha=0.5, label=cat)
ax.axhline(0, color="black", linewidth=0.8)
ax.set_xlabel("Discount")
ax.set_ylabel("Profit ($)")
ax.legend()
fig.tight_layout()
fig.savefig("charts/discount_vs_profit.png", dpi=150)