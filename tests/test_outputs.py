import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "missing /app/report.json"
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_schema():
    """Criterion 1: /app/report.json is valid JSON with the exact required object keys."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Criterion 2: total_requests is the count of non-empty access-log lines."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips is the count of distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
