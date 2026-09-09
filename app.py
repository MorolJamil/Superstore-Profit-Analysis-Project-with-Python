from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "superstore.csv"
st.set_page_config(page_title="Superstore Profit Lens", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH, parse_dates=["Order Date"])
    data["Year"] = data["Order Date"].dt.year
    data["Month"] = data["Order Date"].dt.to_period("M").dt.to_timestamp()
    return data

df = load_data()
st.title("Superstore Profit Lens")
min_date, max_date = df["Order Date"].min(), df["Order Date"].max()

with st.sidebar:
    st.header("Filters")
    date_range = st.date_input("Order date", (min_date, max_date))
    regions = st.multiselect("Region", sorted(df["Region"].unique()))
    categories = st.multiselect("Category", sorted(df["Category"].unique()))
    segments = st.multiselect("Segment", sorted(df["Segment"].unique()))

filtered = df[(df["Order Date"] >= pd.to_datetime(date_range[0])) &
              (df["Order Date"] <= pd.to_datetime(date_range[1]))]
if regions:
    filtered = filtered[filtered["Region"].isin(regions)]
if categories:
    filtered = filtered[filtered["Category"].isin(categories)]
if segments:
    filtered = filtered[filtered["Segment"].isin(segments)]

def money(x):
    return f"${x:,.0f}"

sales = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
margin = (profit / sales * 100) if sales else 0
avg_discount = filtered["Discount"].mean() * 100 if len(filtered) else 0

kpi_one, kpi_two, kpi_three, kpi_four = st.columns(4)
kpi_one.metric("Sales", money(sales))
kpi_two.metric("Profit", money(profit))
kpi_three.metric("Profit margin", f"{margin:.1f}%")
kpi_four.metric("Avg discount", f"{avg_discount:.1f}%")

trend_tab, discount_tab, comparison_tab = st.tabs(
    ["Sales trend", "Discount vs. profit", "Region and category"]
)

with trend_tab:
    monthly = filtered.groupby("Month", as_index=False)["Sales"].sum()
    st.line_chart(monthly.set_index("Month"), y="Sales")

with discount_tab:
    st.scatter_chart(filtered, x="Discount", y="Profit", color="Category")

wit