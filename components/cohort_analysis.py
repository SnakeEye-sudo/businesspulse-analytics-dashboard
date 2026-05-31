"""
BusinessPulse - Cohort Retention Analysis Component
Heatmap showing user retention across monthly cohorts.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def render_cohort_heatmap(df: pd.DataFrame) -> None:
    """Renders cohort retention heatmap with percentage labels."""
    # Build annotation text
    text_matrix = []
    for i in range(len(df)):
        row_text = []
        for j in range(len(df.columns)):
            val = df.iloc[i, j]
            row_text.append(f"{val:.0f}%" if pd.notna(val) else "")
        text_matrix.append(row_text)

    # Color scale: dark red (low) to teal (high)
    colorscale = [
        [0.0, "#7f1d1d"],
        [0.3, "#b91c1c"],
        [0.5, "#d97706"],
        [0.7, "#059669"],
        [1.0, "#0ea5e9"],
    ]

    fig = go.Figure(data=go.Heatmap(
        z=df.values,
        x=df.columns.tolist(),
        y=df.index.tolist(),
        text=text_matrix,
        texttemplate="%{text}",
        textfont=dict(size=12, color="white"),
        colorscale=colorscale,
        showscale=True,
        zmin=0,
        zmax=100,
        colorbar=dict(
            title="Retention %",
            ticksuffix="%",
            titlefont=dict(color="#94a3b8"),
            tickfont=dict(color="#94a3b8"),
        ),
        hoverongaps=False,
        hovertemplate="<b>%{y}</b><br>%{x}<br>Retention: %{z:.1f}%<extra></extra>",
    ))

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8"),
        xaxis=dict(side="top", color="#64748b"),
        yaxis=dict(color="#64748b"),
        margin=dict(l=20, r=20, t=60, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Retention summary
    st.markdown("#### Retention Summary")
    col1, col2, col3 = st.columns(3)
    month1_avg = df.iloc[:, 1].dropna().mean()
    month3_avg = df.iloc[:, 3].dropna().mean() if len(df.columns) > 3 else None
    month5_avg = df.iloc[:, 5].dropna().mean() if len(df.columns) > 5 else None

    col1.metric("Month 1 Avg Retention", f"{month1_avg:.1f}%")
    if month3_avg:
        col2.metric("Month 3 Avg Retention", f"{month3_avg:.1f}%")
    if month5_avg:
        col3.metric("Month 5 Avg Retention", f"{month5_avg:.1f}%")
