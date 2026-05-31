"""
BusinessPulse - Anomaly Detection Component
Detects revenue anomalies using Z-score and IQR methods.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from config import ANOMALY_CONFIG, CHART_COLORS


def detect_anomalies(series: pd.Series) -> pd.Series:
    """Returns boolean mask of anomalies using Z-score."""
    z_scores = np.abs((series - series.mean()) / series.std())
    return z_scores > ANOMALY_CONFIG["z_score_threshold"]


def render_anomaly_section(df: pd.DataFrame) -> None:
    """Renders anomaly detection chart with highlighted outlier points."""
    anomaly_mask = detect_anomalies(df["revenue"])
    anomaly_count = anomaly_mask.sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Anomalies Detected", anomaly_count)
    col2.metric("Revenue Mean", f"${df['revenue'].mean():,.0f}")
    col3.metric("Revenue Std Dev", f"${df['revenue'].std():,.0f}")

    st.write("")

    fig = go.Figure()

    # Normal revenue line
    fig.add_trace(go.Scatter(
        x=df["month"],
        y=df["revenue"],
        mode="lines+markers",
        name="Revenue",
        line=dict(color=CHART_COLORS[0], width=2),
        marker=dict(size=8),
    ))

    # Anomaly points highlighted in red
    anomaly_df = df[anomaly_mask]
    if not anomaly_df.empty:
        fig.add_trace(go.Scatter(
            x=anomaly_df["month"],
            y=anomaly_df["revenue"],
            mode="markers",
            name="Anomaly",
            marker=dict(color="#f87171", size=14, symbol="x", line=dict(width=2, color="#fff")),
            hovertemplate="<b>ANOMALY: %{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
        ))

    # Mean line
    mean_val = df["revenue"].mean()
    fig.add_hline(
        y=mean_val,
        line_dash="dot",
        line_color="#fbbf24",
        annotation_text=f"Mean: ${mean_val:,.0f}",
        annotation_position="top right",
    )

    # Control limits (mean +/- 2.5 std)
    std_val = df["revenue"].std()
    upper = mean_val + ANOMALY_CONFIG["z_score_threshold"] * std_val
    lower = max(0, mean_val - ANOMALY_CONFIG["z_score_threshold"] * std_val)
    fig.add_hrect(y0=lower, y1=upper, fillcolor="#1e293b", opacity=0.3,
                  annotation_text="Normal Range", annotation_position="bottom right")

    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8"),
        xaxis=dict(showgrid=False, color="#64748b"),
        yaxis=dict(showgrid=True, gridcolor="#1e293b", tickprefix="$", color="#64748b"),
        margin=dict(l=20, r=20, t=30, b=20),
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)

    if anomaly_count > 0:
        st.warning(f"⚠️ {anomaly_count} anomalous revenue month(s) detected. Review pricing and campaign strategy.")
    else:
        st.success("✅ No anomalies detected. Revenue trend is within normal range.")
