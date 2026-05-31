"""
BusinessPulse - Revenue Chart Component
Bar + Line chart showing monthly revenue vs previous year.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from config import CHART_COLORS


def render_revenue_chart(df: pd.DataFrame, expanded: bool = False) -> None:
    """Renders a grouped bar chart with revenue and previous year comparison."""
    fig = go.Figure()

    # Current year bars
    fig.add_trace(go.Bar(
        x=df["month"],
        y=df["revenue"],
        name="Current Year",
        marker_color=CHART_COLORS[0],
        opacity=0.9,
        hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
    ))

    # Previous year line
    fig.add_trace(go.Scatter(
        x=df["month"],
        y=df["prev_revenue"],
        name="Previous Year",
        mode="lines+markers",
        line=dict(color=CHART_COLORS[1], width=2, dash="dot"),
        marker=dict(size=6),
        hovertemplate="<b>%{x}</b><br>Prev Year: $%{y:,.0f}<extra></extra>",
    ))

    height = 500 if expanded else 350
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(showgrid=False, color="#64748b"),
        yaxis=dict(showgrid=True, gridcolor="#1e293b", tickprefix="$", color="#64748b"),
        margin=dict(l=20, r=20, t=30, b=20),
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)

    if expanded:
        # Summary stats
        col1, col2, col3 = st.columns(3)
        total = df["revenue"].sum()
        prev_total = df["prev_revenue"].sum()
        growth = ((total - prev_total) / prev_total * 100) if prev_total else 0
        col1.metric("Annual Revenue", f"${total:,.0f}")
        col2.metric("Previous Year", f"${prev_total:,.0f}")
        col3.metric("YoY Growth", f"{growth:.1f}%", delta=f"{growth:.1f}%")
