"""
BusinessPulse Analytics Dashboard
Main Streamlit Application Entry Point
Author: Er. Sangam Krishna (@SnakeEye-sudo)
"""

import streamlit as st
import pandas as pd
from config import PAGE_CONFIG, THEME
from data.mock_data import get_kpi_data, get_revenue_data, get_product_data, get_funnel_data, get_cohort_data
from components.kpi_cards import render_kpi_cards
from components.revenue_chart import render_revenue_chart
from components.sales_funnel import render_sales_funnel
from components.top_products import render_top_products
from components.anomaly_detection import render_anomaly_section
from components.cohort_analysis import render_cohort_heatmap
from utils.forecasting import render_forecast_section

# ── Page Configuration ──────────────────────────────────────────────────────
st.set_page_config(
    page_title=PAGE_CONFIG["title"],
    page_icon=PAGE_CONFIG["icon"],
    layout=PAGE_CONFIG["layout"],
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Sidebar */
    [data-testid="stSidebar"] { background: #0f172a; }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }

    /* KPI card hover effect */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
        transition: transform 0.2s;
    }
    div[data-testid="metric-container"]:hover { transform: translateY(-2px); }

    /* Header */
    .main-header {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 0.5rem;
    }
    .section-header {
        color: #94a3b8;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## BusinessPulse")
    st.markdown("*Advanced Analytics Dashboard*")
    st.divider()

    st.markdown("### Navigation")
    page = st.radio(
        label="",
        options=["Overview", "Revenue & Forecasting", "Products", "Cohort Analysis", "Anomaly Detection"],
        label_visibility="collapsed",
    )
    st.divider()

    st.markdown("### Filters")
    year_filter = st.selectbox("Year", options=[2024, 2023, 2022], index=0)
    region_filter = st.multiselect(
        "Region",
        options=["North", "South", "East", "West", "International"],
        default=["North", "South", "East", "West", "International"],
    )
    st.divider()
    st.caption("Built by Er. Sangam Krishna")
    st.caption("v1.0.0 | May 2026")

# ── Load Data ────────────────────────────────────────────────────────────────
kpi_data = get_kpi_data(year=year_filter)
revenue_df = get_revenue_data(year=year_filter)
product_df = get_product_data()
funnel_df = get_funnel_data()
cohort_df = get_cohort_data()

# ── Page Router ──────────────────────────────────────────────────────────────
if page == "Overview":
    st.markdown('<p class="main-header">BusinessPulse Analytics</p>', unsafe_allow_html=True)
    st.markdown(f"**Year:** {year_filter} &nbsp;|&nbsp; **Regions:** {', '.join(region_filter)}")
    st.divider()

    # KPI Cards
    st.markdown('<p class="section-header">Key Performance Indicators</p>', unsafe_allow_html=True)
    render_kpi_cards(kpi_data)
    st.divider()

    # Revenue + Funnel side by side
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="section-header">Monthly Revenue</p>', unsafe_allow_html=True)
        render_revenue_chart(revenue_df)
    with col2:
        st.markdown('<p class="section-header">Sales Funnel</p>', unsafe_allow_html=True)
        render_sales_funnel(funnel_df)
    st.divider()

    # Top Products
    st.markdown('<p class="section-header">Top Products Performance</p>', unsafe_allow_html=True)
    render_top_products(product_df)

elif page == "Revenue & Forecasting":
    st.markdown('<p class="main-header">Revenue & Forecasting</p>', unsafe_allow_html=True)
    st.divider()
    render_revenue_chart(revenue_df, expanded=True)
    st.divider()
    render_forecast_section(revenue_df)

elif page == "Products":
    st.markdown('<p class="main-header">Product Performance</p>', unsafe_allow_html=True)
    st.divider()
    render_top_products(product_df, expanded=True)

elif page == "Cohort Analysis":
    st.markdown('<p class="main-header">Cohort Retention Analysis</p>', unsafe_allow_html=True)
    st.divider()
    render_cohort_heatmap(cohort_df)

elif page == "Anomaly Detection":
    st.markdown('<p class="main-header">Anomaly Detection</p>', unsafe_allow_html=True)
    st.divider()
    render_anomaly_section(revenue_df)
