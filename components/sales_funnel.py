"""
BusinessPulse - Sales Funnel Component
Vertical funnel chart showing lead-to-conversion pipeline.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from config import CHART_COLORS


def render_sales_funnel(df: pd.DataFrame) -> None:
    """Renders an interactive funnel chart."""
    # Calculate conversion rates between stages
    conversions = []
    for i in range(1, len(df)):
        rate = (df["count"].iloc[i] / df["count"].iloc[i - 1] * 100)
        conversions.append(f"{rate:.1f}%")
    conversions.insert(0, "100%")

    fig = go.Figure(go.Funnel(
        y=df["stage"],
        x=df["count"],
        textposition="inside",
        textinfo="value+percent initial",
        marker=dict(
            color=CHART_COLORS[:len(df)],
            line=dict(width=1, color="#0f172a"),
        ),
        connector=dict(line=dict(color="#334155", width=1)),
        hovertemplate="<b>%{y}</b><br>Count: %{x:,.0f}<br>%{percentInitial:.1%} of total<extra></extra>",
    ))

    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8", size=11),
        margin=dict(l=10, r=10, t=20, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Overall conversion rate
    overall = df["count"].iloc[-1] / df["count"].iloc[0] * 100
    st.metric("Overall Conversion", f"{overall:.2f}%")
