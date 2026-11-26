# Cheapest AI API: how to compare LLM prices without getting fooled

The cheapest headline price is not always the cheapest request. Use this checklist before you switch providers.

## 1. Compare the same model ID

Model names and versions differ across suppliers. Compare the exact model ID and snapshot shown in the marketplace, not a generic family name.

## 2. Compare input, output and cache

A coding agent can send a large cached context every turn. If one supplier charges less input but has no cache, the effective bill can be higher.

## 3. Check the route health

A very cheap channel with a low success rate creates retries, latency and user pain. 321AI shows recent success, latency and self-test signals next to the quote.

## 4. Count failures

Failed requests should not be billed. Confirm the provider's policy and check the actual invoice.

## 5. Verify with a small run

Send a representative request, then inspect the usage log: route, prompt tokens, completion tokens, cache tokens and charged amount.

## 321AI price anchors

| Model | 321AI input / output | Official input / output | Approx. official |
|---|---:|---:|---:|
| Claude Sonnet 5.5 | $0.0405 / $0.2025 | $2 / $10 | 2.0% |
| GPT-6.2 Astra | $0.0675 / $0.3375 | $8 / $40 | 0.84% |
| Gemini 4 Neon | $0.0990 / $0.4950 | $3 / $15 | 3.3% |
| GLM-5.3 | $0.00651 / $0.02046 | $1.40 / $4.40 | 0.47% |
| DeepSeek V4.1 Flash | $0.001875 / $0.0075 | $0.30 / $1.20 | 0.63% |

Snapshot 2026-11-26 19:08 JST. Prices move; use the live marketplace.

## FAQ

### What is the absolute lowest price?

On the snapshot, GLM-5.3-Flash had the lowest input quote at **$0.000014/M**. It is a small/fast model, not a Claude replacement. Choose by workload, not by the single lowest number.

### Is a low price a guarantee?

No. Check the route, cache, success rate and final invoice. A marketplace gives you evidence; it does not make every cheap route suitable.

---

[Back to the repository](../README.md) · [Claude Code cheap](claude-code-cheap.md) · [OpenRouter alternative](openrouter-alternative.md)
