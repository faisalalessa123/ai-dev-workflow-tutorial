import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("data/sales-data.csv")


try:
    df = load_data()
except Exception:
    st.error("Unable to load sales data. Please ensure data/sales-data.csv is present.")
    st.stop()

st.title("ShopSmart Sales Dashboard")

total_sales = df["total_amount"].sum()
total_orders = len(df)

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")

df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").dt.to_timestamp()
monthly = df.groupby("month")["total_amount"].sum().reset_index()

fig_trend = px.line(
    monthly,
    x="month",
    y="total_amount",
    title="Sales Trend",
    labels={"month": "Month", "total_amount": "Total Sales ($)"},
)
st.plotly_chart(fig_trend, use_container_width=True)

cat_df = (
    df.groupby("category")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)

fig_cat = px.bar(
    cat_df,
    x="category",
    y="total_amount",
    title="Sales by Category",
    labels={"category": "Category", "total_amount": "Total Sales ($)"},
)

reg_df = (
    df.groupby("region")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)

fig_reg = px.bar(
    reg_df,
    x="region",
    y="total_amount",
    title="Sales by Region",
    labels={"region": "Region", "total_amount": "Total Sales ($)"},
)

col1, col2 = st.columns(2)
col1.plotly_chart(fig_cat, use_container_width=True)
col2.plotly_chart(fig_reg, use_container_width=True)
