"""
get_data.py -- download the dataset
Downloads the real Sample Superstore dataset (9,994 order lines, 2014-2017)
from a public, no-login GitHub mirror.
"""
import pandas as pd
from pathlib import Path

Path("data").mkdir(exist_ok=True)

url = ("https://raw.githubusercontent.com/Ayon-coder/FUTURE_ML_01/"
       "main/Sample%20-%20Superstore.csv")

print("Downloading Superstore data...")
df = pd.read_csv(url, encoding="latin-1", parse_dates=["Order Date", "Ship Date"])

cols = ["Order Date", "Region", "Category", "Sub-Category", "Segment",
        "Sales", "Quantity", "Discount", "Profit"]
df = df[cols].sort_values("Order Date").reset_index(drop=True)

df.to_csv("data/superstore.csv", index=False)

print("Done. Saved to data/superstore.csv")
print("Number of rows:", len(df))
print("Date range:", df["Order Date"].min().date(), "to", df["Order Date"].max().date())