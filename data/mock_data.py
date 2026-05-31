"""
BusinessPulse Analytics - Mock Data Generator
Generates realistic business metrics data for the dashboard.
"""

import pandas as pd
import numpy as np
from config import MONTHS

np.random.seed(42)


def get_kpi_data(year: int = 2024) -> dict:
    """Returns KPI metrics dict with current value, delta, and trend."""
    base = {2024: 1, 2023: 0.88, 2022: 0.74}
    m = base.get(year, 1)
    return {
        "revenue": {
            "label": "Total Revenue",
            "value": round(1_342_800 * m),
            "delta": "+12.4%" if year == 2024 else "+9.1%",
            "delta_positive": True,
            "icon": "💰",
            "format": "currency",
        },
        "users": {
            "label": "Active Users",
            "value": round(42_580 * m),
            "delta": "+8.7%" if year == 2024 else "+5.2%",
            "delta_positive": True,
            "icon": "👥",
            "format": "number",
        },
        "orders": {
            "label": "Total Orders",
            "value": round(11_234 * m),
            "delta": "+6.3%" if year == 2024 else "+4.8%",
            "delta_positive": True,
            "icon": "📦",
            "format": "number",
        },
        "conversion_rate": {
            "label": "Conversion Rate",
            "value": round(3.84 * m, 2),
            "delta": "-0.2%" if year == 2024 else "+0.3%",
            "delta_positive": False,
            "icon": "🎯",
            "format": "percent",
        },
        "avg_order_value": {
            "label": "Avg Order Value",
            "value": round(119.6 * m, 2),
            "delta": "+3.1%",
            "delta_positive": True,
            "icon": "💳",
            "format": "currency",
        },
        "churn_rate": {
            "label": "Churn Rate",
            "value": round(2.8 * m, 2),
            "delta": "+0.3%",
            "delta_positive": False,
            "icon": "🔄",
            "format": "percent",
        },
    }


def get_revenue_data(year: int = 2024) -> pd.DataFrame:
    """Returns monthly revenue DataFrame."""
    base_revenue = [
        85000, 92000, 108000, 115000, 122000, 134000,
        118000, 125000, 138000, 145000, 158000, 162800,
    ]
    prev_revenue = [int(v * 0.88) for v in base_revenue]
    noise = np.random.normal(0, 3000, 12)
    if year == 2024:
        revenue = [max(0, int(v + n)) for v, n in zip(base_revenue, noise)]
        prev = prev_revenue
    elif year == 2023:
        revenue = [max(0, int(v + n)) for v, n in zip(prev_revenue, noise)]
        prev = [int(v * 0.88) for v in prev_revenue]
    else:
        y2022 = [int(v * 0.74) for v in base_revenue]
        revenue = [max(0, int(v + n)) for v, n in zip(y2022, noise)]
        prev = [int(v * 0.88) for v in y2022]

    return pd.DataFrame({
        "month": MONTHS,
        "revenue": revenue,
        "prev_revenue": prev,
        "orders": [max(1, int(r / 119.6)) for r in revenue],
    })


def get_product_data() -> pd.DataFrame:
    """Returns top products performance DataFrame."""
    products = [
        ("Analytics Pro Suite", "Software", 48200, 4.8, 312, 0.89),
        ("DataVault Storage", "Infrastructure", 39800, 4.6, 287, 0.72),
        ("PulseInsight API", "API", 34600, 4.9, 198, 0.95),
        ("ReportBuilder Cloud", "Software", 28900, 4.5, 245, 0.81),
        ("SmartDash Lite", "Software", 24300, 4.3, 189, 0.67),
        ("ConnectHub Integration", "Integration", 19800, 4.7, 156, 0.78),
        ("AuditTrail Pro", "Compliance", 17600, 4.4, 132, 0.91),
        ("ForecasterAI Module", "AI/ML", 15200, 4.8, 98, 0.88),
        ("TeamSync Dashboard", "Collaboration", 13400, 4.2, 112, 0.62),
        ("ExportMaster Suite", "Utility", 11800, 4.1, 97, 0.55),
    ]
    df = pd.DataFrame(products, columns=["product", "category", "revenue", "rating", "orders", "growth_rate"])
    df["growth_pct"] = (df["growth_rate"] * 100).round(1)
    df["avg_price"] = (df["revenue"] / df["orders"]).round(2)
    return df


def get_funnel_data() -> pd.DataFrame:
    """Returns sales funnel conversion data."""
    stages = ["Website Visits", "Sign-ups", "Free Trial", "Demo Request", "Paid Conversion"]
    values = [120000, 34200, 12800, 5400, 1632]
    return pd.DataFrame({"stage": stages, "count": values})


def get_cohort_data() -> pd.DataFrame:
    """Returns cohort retention matrix."""
    cohort_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    retention_matrix = [
        [100, 72, 61, 54, 48, 44],
        [100, 68, 58, 51, 46, None],
        [100, 74, 63, 55, None, None],
        [100, 70, 60, None, None, None],
        [100, 75, None, None, None, None],
        [100, None, None, None, None, None],
    ]
    df = pd.DataFrame(
        retention_matrix,
        index=[f"{m} Cohort" for m in cohort_months],
        columns=[f"Month {i}" for i in range(6)],
    )
    return df
