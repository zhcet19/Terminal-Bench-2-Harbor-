Parse the Apache-style access log at `/app/access.log` and produce a JSON summary report at `/app/report.json`.

The report must be a JSON object with exactly these keys:

1. `total_requests` — integer count of all log lines (requests).
2. `unique_ips` — integer count of distinct client IP addresses.
3. `top_path` — string: the request path (e.g. `/index.html`) that appears most often.

Success criteria:

1. The file `/app/report.json` exists and is valid JSON.
2. `total_requests` equals the actual number of requests in the log.
3. `unique_ips` equals the actual number of distinct source IPs.
4. `top_path` equals the path with the highest request count.
