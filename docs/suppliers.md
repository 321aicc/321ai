# Supplier and channel comparison

321AI is a marketplace, not a single upstream account. A model can be offered by multiple independent suppliers; each supplier/channel is a separate quote and a separate route.

## What to compare

- **Input / output / cache prices** — the marketplace displays merchant quotes; a low headline price may not be the lowest effective cost for a cache-heavy workload.
- **Recent success rate and first-response time** — use the public self-test and live request history shown next to the listing.
- **Cache support** — for Claude/agent workloads, a channel with cache-read support can be substantially cheaper than a lower headline price without cache.
- **Context capacity** — confirm the supplier has served requests at your context size.
- **Pinned vs smart routing** — a pin guarantees the supplier but can be more expensive; smart/cheap routing can switch suppliers as the market moves.

## How routing chooses a channel

The console offers policy groups such as smart, cheap, stable, fast and guaranteed, plus per-token/per-model pins. Each policy applies its own price, reliability and latency constraints. If a selected merchant becomes unavailable, fallback behavior depends on the pin's fallback setting.

## Adding a supplier

Supplier onboarding is managed separately from this repository. Use the merchant center or contact the operator through [321ai.cc](https://321ai.cc); do not post supplier credentials in an issue.
