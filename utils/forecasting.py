"""
BusinessPulse - Revenue Forecasting Module
Linear trend + seasonal forecasting using statsmodels.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from config import CHART_COLORS, FORECAST_CONFIG, MONTHS


def simple_forecast(revenue: list, periods: int = 6) -> tuple:
    """Linear regression-based revenue forecast."""
    x = np.arange(len(revenue))
    coeffs = np.polyfit(x, revenue, 1)  # linear fit
    trend = np.poly1d(coeffs)

    future_x = np.arange(len(revenue), len(revenue) + periods)
    forecasted = [max(0, int(trend(xi))) for xi in future_x]

    # Confidence interval (simple std-based)
    residuals = [revenue[i] - trend(x[i]) for i in range(len(revenue))]
    std = np.std(residuals)
    upper = [f + int(1.645 * std) for f in forecasted]
    lower = [max(0, f - int(1.645 * std)) for f in forecasted]

    return forecasted, upper, lower


def render_forecast_section(df: pd.DataFrame) -> None:
    """Renders the revenue forecasting chart with confidence bands."""
    st.markdown("#### 6-Month Revenue Forecast (Linear Trend)")

    periods = FORECAST_CONFIG["periods"]
    revenue = df["revenue"].tolist()

    forecasted, upper, lower = simple_forecast(revenue, periods)

    # Generate forecast month labels
    all_months = MONTHS + [f"M+{i+1}" for i in range(periods)]
    hist_months = df["month"].tolist()
    fore_months = [f"M+{i+1}" for i in range(periods)]

    fig = go.Figure()

    # Historical revenue
    fig.add_trace(go.Scatter(
        x=hist_months,
        y=revenue,
        name="Historical",
        mode="lines+markers",
        line=dict(color=CHART_COLORS[0], width=2),
        marker=dict(size=7),
    ))

    # Forecast line
    fig.add_trace(go.Scatter(
        x=fore_months,
        y=forecasted,
        name="Forecast",
        mode="lines+markers",
        line=dict(color=CHART_COLORS[2], width=2, dash="dash"),
        marker=dict(size=7, symbol="diamond"),
    ))

    # Confidence band (upper)
    fig.add_trace(go.Scatter(
        x=fore_months + fore_months[::-1],
        y=upper + lower[::-1],
        fill="toself",
        fillcolor="rgba(52, 211, 153, 0.1)",
        line=dict(color="rgba(0,0,0,0)"),
        name="90% Confidence Interval",
        hoverinfo="skip",
    ))

    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8"),
        xaxis=dict(showgrid=False, color="#64748b"),
        yaxis=dict(showgrid=True, gridcolor="#1e293b", tickprefix="$", color="#64748b"),
        margin=dict(l=20, r=20, t=30, b=20),
        hovermode="x unified",
        legend=dict(orientation="h", y=1.1),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Forecast summary table
    st.markdown("#### Forecast Details")
    forecast_df = pd.DataFrame({
        "Period": fore_months,
        "Forecast Revenue": [f"${v:,.0f}" for v in forecasted],
        "Lower Bound (90%)": [f"${v:,.0f}" for v in lower],
        "Upper Bound (90%)": [f"${v:,.0f}" for v in upper],
    })
    st.dataframe(forecast_df, use_container_width=True, hide_index=True)
