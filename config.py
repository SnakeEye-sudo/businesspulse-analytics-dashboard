"""
BusinessPulse Analytics Dashboard - Configuration
"""

# Page Configuration
PAGE_CONFIG = {
    "title": "BusinessPulse Analytics",
    "icon": "📊",
    "layout": "wide",
}

# Color Theme
THEME = {
    "primary": "#38bdf8",
    "secondary": "#818cf8",
    "success": "#4ade80",
    "danger": "#f87171",
    "warning": "#fbbf24",
    "background": "#0f172a",
    "surface": "#1e293b",
    "border": "#334155",
    "text": "#e2e8f0",
    "muted": "#94a3b8",
}

# Chart color palette
CHART_COLORS = [
    "#38bdf8", "#818cf8", "#4ade80",
    "#fbbf24", "#f87171", "#34d399",
    "#a78bfa", "#fb923c", "#60a5fa",
    "#f472b6",
]

# KPI targets for trend calculation
KPI_TARGETS = {
    "revenue": 1_500_000,
    "users": 50_000,
    "orders": 12_000,
    "conversion_rate": 4.5,
    "avg_order_value": 120,
    "churn_rate": 2.5,
}

# Regions
REGIONS = ["North", "South", "East", "West", "International"]

# Date settings
DEFAULT_YEAR = 2024
AVAILABLE_YEARS = [2024, 2023, 2022]
MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Anomaly detection settings
ANOMALY_CONFIG = {
    "z_score_threshold": 2.5,
    "rolling_window": 3,
    "iqr_multiplier": 1.5,
}

# Forecasting settings
FORECAST_CONFIG = {
    "periods": 6,  # months to forecast
    "seasonality_mode": "multiplicative",
    "interval_width": 0.80,
}
