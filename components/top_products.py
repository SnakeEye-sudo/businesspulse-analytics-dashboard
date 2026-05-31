"""
BusinessPulse - Top Products Component
Sortable, filterable product performance table with bar chart.
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from config import CHART_COLORS


def render_top_products(df: pd.DataFrame, expanded: bool = False) -> None:
    """Renders top products table and horizontal bar chart."""
    if expanded:
        col_filter, col_sort = st.columns([2, 1])
        with col_filter:
            categories = ["All"] + sorted(df["category"].unique().tolist())
            cat_filter = st.selectbox("Filter by Category", categories)
        with col_sort:
            sort_by = st.selectbox("Sort by", ["revenue", "orders", "rating", "growth_pct"])

        if cat_filter != "All":
            df = df[df["category"] == cat_filter]
        df = df.sort_values(sort_by, ascending=False)
    else:
        df = df.head(5)

    # Horizontal bar chart
    fig = px.bar(
        df,
        x="revenue",
        y="product",
        orientation="h",
        color="category",
        color_discrete_sequence=CHART_COLORS,
        text=df["revenue"].apply(lambda x: f"${x:,.0f}"),
        labels={"revenue": "Revenue ($)", "product": ""},
    )
    fig.update_layout(
        height=300 if not expanded else 450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8"),
        yaxis=dict(autorange="reversed"),
        xaxis=dict(showgrid=True, gridcolor="#1e293b", tickprefix="$"),
        margin=dict(l=10, r=10, t=20, b=10),
        showlegend=expanded,
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    if expanded:
        # Full data table
        display_df = df[["product", "category", "revenue", "orders", "rating", "growth_pct", "avg_price"]].copy()
        display_df.columns = ["Product", "Category", "Revenue ($)", "Orders", "Rating", "Growth (%)", "Avg Price ($)"]
        display_df["Revenue ($)"] = display_df["Revenue ($)"].apply(lambda x: f"${x:,.0f}")
        display_df["Avg Price ($)"] = display_df["Avg Price ($)"].apply(lambda x: f"${x:.2f}")
        st.dataframe(display_df, use_container_width=True, hide_index=True)
