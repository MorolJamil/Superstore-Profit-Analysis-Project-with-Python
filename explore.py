import pandas as pd

df = pd.read_csv("data/superstore.csv", parse_dates=["Order Date"])

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print(f"Total Sales:  ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Overall Profit Margin: {total_profit / total_sales * 100:.1f}%")
print(f"Average Discount: {df['Discount'].mean()*100:.1f}%")

def margin_table(df, by):
    t = df.groupby(by).agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        avg_discount=("Discount", "mean"),
        orders=("Sales", "count"),
    )
    t["profit_margin_pct"] = t["total_profit"] / t["total_sales"] * 100
    return t.sort_values("total_sales", ascending=False).round(2)

print(margin_table(df, "Category"))
print(margin_table(df, "Region"))
print(margin_table(df, "Segment"))