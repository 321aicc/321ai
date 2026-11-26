# Rate limits and quotas

321AI applies several independent limits:

- **Account balance / token quota** — a token with a quota cannot spend beyond its remaining quota; an account with a negative balance cannot start new calls.
- **Global and per-token request rate** — protects the gateway from bursts and abuse. Limits can change with capacity.
- **Upstream concurrency** — the selected supplier channel has its own concurrency and throughput; a busy channel can return 429 or time out.
- **Registration and verification limits** — separate anti-abuse controls apply to account creation and email verification.

## Recommended client behavior

- Retry `429`, `500`, `502`, `503` and `504` with exponential backoff and jitter.
- Do not retry `400`, `401` or `403` without changing the request or configuration.
- Keep long-running streams cancellable; abort on user cancellation.
- For high-volume workloads, open a support ticket to discuss routing and capacity.

Rate limits are operational safeguards, not a purchased quota. Actual capacity depends on live supplier supply.
