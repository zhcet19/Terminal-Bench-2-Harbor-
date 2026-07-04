import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists_and_valid_json():
    """Criterion 1: The file /app/report.json exists and is valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found"
    text = REPORT_PATH.read_text()
    try:
        json.loads(text)
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")


def test_total_requests():
    """Criterion 2: total_requests equals the actual number of requests in the log."""
    report = json.loads(REPORT_PATH.read_text())
    assert "total_requests" in report, "missing key: total_requests"
    assert report["total_requests"] == 6, (
        f"expected total_requests=6, got {report['total_requests']}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals the actual number of distinct source IPs."""
    report = json.loads(REPORT_PATH.read_text())
    assert "unique_ips" in report, "missing key: unique_ips"
    assert report["unique_ips"] == 3, (
        f"expected unique_ips=3, got {report['unique_ips']}"
    )


def test_top_path():
    """Criterion 4: top_path equals the path with the highest request count."""
    report = json.loads(REPORT_PATH.read_text())
    assert "top_path" in report, "missing key: top_path"
    assert report["top_path"] == "/index.html", (
        f"expected top_path='/index.html', got {report['top_path']!r}"
    )
