# How to use Claude Code cheaply in 2026

Claude Code speaks the Anthropic API. 321AI exposes an Anthropic-compatible endpoint, so the setup is one environment variable and one key.

## 30-second setup

```bash
export ANTHROPIC_BASE_URL="https://321ai.cc"
export ANTHROPIC_AUTH_TOKEN="sk-..."
```

Create the key in the [321AI console](https://321ai.cc/#/console/tokens). Then run Claude Code normally.

For OpenAI-compatible coding agents (Codex, Cline, Continue), use:

```bash
export OPENAI_BASE_URL="https://321ai.cc/v1"
export OPENAI_API_KEY="sk-..."
```

## Why Claude Code gets expensive

Coding agents resend a large context on every turn. The effective cost is driven by:

- input price;
- output price;
- **cache-read price**;
- how often the client actually hits the cache.

A channel with a low headline input price but no cache can be more expensive than a slightly higher-priced channel with cache support. The marketplace exposes cache-read price and cache rate so you can compare the real cost.

## What to pin for Claude Code

1. Open [the marketplace](https://321ai.cc/#/market).
2. Filter to Claude and the model you use.
3. Compare input/output/cache, success rate and first-response time.
4. Pin the merchant that fits your workload, or use the **stable** / **fast** policy.
5. Check the confirmed price and usage logs after the first real request.

## Pricing snapshot

Claude Sonnet 5.5 was **$0.0405 / $0.2025 per 1M** on 2026-11-26 19:08 JST — roughly 2% of the official $2 / $10 list price. Prices move; use the live model page before a large run.

## FAQ

### Is Claude Code officially supported?

Claude Code is an Anthropic client. 321AI provides an Anthropic-compatible endpoint; it is not affiliated with Anthropic.

### Will my tools see a different API?

No. You keep the Anthropic protocol and change the base URL and token.

### What if a pinned merchant disappears?

Depending on the pin setting, the route can fall back to smart routing instead of hard-failing.

---

[Back to the repository](../README.md) · [Cheapest Claude API](cheapest-claude-api.md)
