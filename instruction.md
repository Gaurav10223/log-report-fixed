Parse the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists, is valid JSON, and is an object with exactly these keys: `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the integer count of non-empty log lines in `/app/access.log`.
3. `unique_ips` is the integer count of distinct client IP addresses, using the first whitespace-delimited field of each non-empty log line.
4. `top_path` is the string request path with the highest request count, parsed from the quoted HTTP request portion of each log line.
