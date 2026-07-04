import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists_and_valid_json():
    """report.json must exist and be parseable JSON."""
    assert REPORT_PATH.exists(), "no report.json found"
    text = REPORT_PATH.read_text()
    try:
        json.loads(text)
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")


def test_total_requests():
    """total_requests should equal 6 (the number of lines in access.log)."""
    report = json.loads(REPORT_PATH.read_text())
    assert "total_requests" in report, "missing key: total_requests"
    assert report["total_requests"] == 6, (
        f"expected total_requests=6, got {report['total_requests']}"
    )


def test_unique_ips():
    """unique_ips should be 3 (192.168.0.1, 192.168.0.2, 10.0.0.5)."""
    report = json.loads(REPORT_PATH.read_text())
    assert "unique_ips" in report, "missing key: unique_ips"
    assert report["unique_ips"] == 3, (
        f"expected unique_ips=3, got {report['unique_ips']}"
    )


def test_top_path():
    """top_path should be /index.html (3 hits vs 2 for /about.html)."""
    report = json.loads(REPORT_PATH.read_text())
    assert "top_path" in report, "missing key: top_path"
    assert report["top_path"] == "/index.html", (
        f"expected top_path='/index.html', got {report['top_path']!r}"
    )
