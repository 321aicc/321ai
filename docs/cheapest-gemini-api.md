# Cheapest Gemini API: live pricing for Gemini 4

**Snapshot:** Gemini 4 Neon was **$0.0990 input / $0.4950 output per 1M tokens** on 321AI at 2026-11-26 19:08 JST, against an official list price of **$3 / $15** — about **3.3%** of the official price.

See the [Gemini 4 Neon model page](https://321ai.cc/models/gemini-4-neon) and the [marketplace](https://321ai.cc/#/market) for the current live quote.

## Why compare merchants?

The same model can have different prices, cache behavior and success rates across suppliers. 321AI shows those signals so a low headline price is not the only input to the decision.

## Use a Gemini model

```bash
curl https://321ai.cc/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini-4-neon","messages":[{"role":"user","content":"Hello"}],"max_tokens":32}'
```

Use the exact model ID from the marketplace; availability changes with supply.

## FAQ

### Does 321AI use Google's official endpoint?

321AI routes to independent suppliers. It is not a Google product and does not claim an official Google relationship.

### What if Gemini is unavailable?

Try another live merchant, switch policy, or check the marketplace before retrying. Failed requests are not billed.

---

[Back to the repository](../README.md) · [Cheapest Claude API](cheapest-claude-api.md)
