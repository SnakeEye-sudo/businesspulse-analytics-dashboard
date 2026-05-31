"""
BusinessPulse - Utility Helpers
Formatting and utility functions used across components.
"""


def format_value(value: float, fmt: str) -> str:
    """Format a numeric value based on display type."""
    if fmt == "currency":
        if value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        elif value >= 1_000:
            return f"${value / 1_000:.1f}K"
        return f"${value:,.2f}"
    elif fmt == "percent":
        return f"{value:.2f}%"
    elif fmt == "number":
        if value >= 1_000_000:
            return f"{value / 1_000_000:.1f}M"
        elif value >= 1_000:
            return f"{value / 1_000:.1f}K"
        return f"{int(value):,}"
    return str(value)


def format_delta(current: float, previous: float) -> tuple[str, bool]:
    """Returns (delta_string, is_positive) from two values."""
    if previous == 0:
        return "N/A", True
    change = ((current - previous) / previous) * 100
    is_positive = change >= 0
    sign = "+" if is_positive else ""
    return f"{sign}{change:.1f}%", is_positive


def get_trend_color(value: float, threshold_up: float = 0, threshold_down: float = 0) -> str:
    """Returns a CSS color based on value vs thresholds."""
    if value > threshold_up:
        return "#4ade80"   # green
    elif value < threshold_down:
        return "#f87171"   # red
    return "#fbbf24"       # yellow


def truncate_label(label: str, max_len: int = 20) -> str:
    """Truncate long labels for chart display."""
    return label if len(label) <= max_len else label[:max_len - 3] + "..."


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safe division that returns default on zero denominator."""
    return numerator / denominator if denominator != 0 else default
