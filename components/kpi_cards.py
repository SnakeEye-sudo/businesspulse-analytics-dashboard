"""
BusinessPulse - KPI Cards Component
Renders the 6 key performance indicator metric cards.
"""

import streamlit as st
from utils.helpers import format_value


def render_kpi_cards(kpi_data: dict) -> None:
    """Renders 6 KPI metric cards in a 3-column layout."""
    keys = list(kpi_data.keys())
    row1, row2 = keys[:3], keys[3:]

    # Row 1
    cols = st.columns(3)
    for col, key in zip(cols, row1):
        kpi = kpi_data[key]
        with col:
            delta_color = "normal" if kpi["delta_positive"] else "inverse"
            st.metric(
                label=f"{kpi['icon']}  {kpi['label']}",
                value=format_value(kpi["value"], kpi["format"]),
                delta=kpi["delta"],
                delta_color=delta_color,
            )

    st.write("")

    # Row 2
    cols = st.columns(3)
    for col, key in zip(cols, row2):
        kpi = kpi_data[key]
        with col:
            delta_color = "normal" if kpi["delta_positive"] else "inverse"
            st.metric(
                label=f"{kpi['icon']}  {kpi['label']}",
                value=format_value(kpi["value"], kpi["format"]),
                delta=kpi["delta"],
                delta_color=delta_color,
            )
