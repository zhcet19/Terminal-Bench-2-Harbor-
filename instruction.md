Parse the Apache-style access log at `/app/access.log` and write a JSON summary to `/app/report.json`.

The output must be a JSON object with these keys:

1. `total_requests` — total number of requests (i.e. lines) in the log.
2. `unique_ips` — number of distinct client IPs seen.
3. `top_path` — the request path that appears the most.

Success criteria:

1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` is correct.
3. `unique_ips` is correct.
4. `top_path` is correct.
