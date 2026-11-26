# Cheapest GPT API: live GPT-6.2 Astra pricing

**Snapshot:** GPT-6.2 Astra was **$0.0675 input / $0.3375 output per 1M tokens** on 321AI at 2026-11-26 19:08 JST, against an official list price of **$8 / $40** — about **0.84%** of the official price.

Prices change. Use the [GPT-6.2 Astra model page](https://321ai.cc/models/gpt-6.2-astra) and the [marketplace](https://321ai.cc/#/market) for the current quote.

## Why a marketplace can be cheaper

Multiple independent suppliers can list the same model. 321AI compares their quotes and routes to a qualified channel; you can pin a specific merchant when you need a confirmed price.

## Compare the real cost

| Cost component | Why it matters |
|---|---|
| Input | Long prompts and agent contexts dominate |
| Output | Reasoning and code generation can be output-heavy |
| Cache read | Repeated context can be much cheaper |
| Retries | Failed requests should not be billed |

## Use GPT-6.2 Astra

```bash
curl https://321ai.cc/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-6.2-astra","messages":[{"role":"user","content":"Hello"}],"max_tokens":32}'
```

## FAQ

### Is this the official OpenAI price?

No. The official list price is shown for comparison. 321AI is an independent marketplace and is not affiliated with OpenAI.

### How often do prices change?

Supply changes continuously. The marketplace is the live source; the confirmed route price and invoice are final.

---

[Back to the repository](../README.md) · [Cheapest Claude API](cheapest-claude-api.md)
