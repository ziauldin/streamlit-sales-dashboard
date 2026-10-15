
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard - Streamlit")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="Data")

    # Data Cleaning
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date", "Sales", "Cost", "Units sold", "Category", "Product"], inplace=True)
    df["Month-Year"] = df["Date"].dt.to_period("M").astype(str)
    df["Profit"] = df["Sales"] - df["Cost"]

    # KPIs
    total_sales = df["Sales"].sum()
    total_cost = df["Cost"].sum()
    total_profit = total_sales - total_cost
    total_units = df["Units sold"].sum()

    # KPI Display
    st.markdown("### Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"£{total_sales/1e6:.2f} M")
    col2.metric("Total Cost", f"£{total_cost/1e6:.2f} M")
    col3.metric("Total Profit", f"£{total_profit/1e6:.2f} M")
    col4.metric("Units Sold", f"{total_units/1e6:.2f} M Units")

    st.markdown("---")

    # Data Aggregation
    sales_trend = df.groupby("Month-Year")[["Sales", "Cost", "Profit"]].sum().reset_index()
    top_categories = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()
    top_subcategories = df.groupby("Subcategory")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
    country_sales = df.groupby("Country")["Sales"].sum().reset_index()
    top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
    top_salesreps = df.groupby("Salesrep")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()

    # Charts
    st.markdown("### 📈 Sales Trend Over Time")
    fig1 = px.line(sales_trend, x="Month-Year", y=["Sales", "Cost", "Profit"], title="Sales, Cost & Profit Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### 📊 Top Categories by Sales")
        fig2 = px.bar(top_categories, x="Sales", y="Category", orientation="h")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 🧺 Top 10 Best Selling Products")
        fig5 = px.bar(top_products, x="Product", y="Sales")
        st.plotly_chart(fig5, use_container_width=True)

    with col_b:
        st.markdown("### 🔍 Top 10 Subcategories")
        fig3 = px.bar(top_subcategories, x="Sales", y="Subcategory", orientation="h")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 🌍 Sales by Country")
        fig4 = px.pie(country_sales, values="Sales", names="Country")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("### 🧑‍💼 Top 10 Sales Representatives")
    fig6 = px.bar(top_salesreps, x="Sales", y="Salesrep", orientation="h")
    st.plotly_chart(fig6, use_container_width=True)

else:
    st.info("Please upload a valid Excel file with a 'Data' sheet to begin analysis.")
