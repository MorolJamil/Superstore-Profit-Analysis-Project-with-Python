import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path("charts").mkdir(exist_ok=True)
df = pd.read_csv("data/superstore.csv", parse_dates=["Order Date"])

df["Year"] = df["Order Date"].dt.year
yearly = df.groupby("Year")["Sales"].sum().reset_index()
yearly["growth_pct"] = yearly["Sales"].pct_change() * 100
first, last = yearly.iloc[0], yearly.iloc[-1]
overall_growth = (last["Sales"] - first["Sales"]) / first["Sales"] * 100
print(f"Overall sales growth {first['Year']}->{last['Year']}: {overall_growth:.1f}%")
print(yearly)

df["Month"] = df["Order Date"].dt.to_period("M")
monthly = df.groupby("Month")["Sales"].sum().reset_index()
monthly["Month_ts"] = monthly["Month"].dt.to_timestamp()

# Seasonality: peak by TOTAL sales per calendar month (not average order size)
df["Cal_Month"] = df["Order Date"].dt.month
seasonal_total = df.groupby("Cal_Month")["Sales"].sum()
peak_month = seasonal_total.idxmax()
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
print(f"Peak calendar month (total sales): {month_names[peak_month-1]}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
ax1.bar(yearly["Year"].astype(str), yearly["Sales"])
ax2.plot(monthly["Month_ts"], monthly["Sales"], marker="o")
fig.tight_layout()
fig.savefig("charts/sales_trend.png", dpi=150)