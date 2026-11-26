# Integration guide

## Base URLs

| Protocol | Base URL |
|---|---|
| OpenAI-compatible | `https://321ai.cc/v1` |
| Anthropic-compatible | `https://321ai.cc` (use `/v1/messages`) |

Create an API key in **Console → API Tokens** on [321ai.cc](https://321ai.cc).

## OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",
    base_url="https://321ai.cc/v1",
)
```

The standard `chat.completions`, streaming and tool-calling paths are supported. Model IDs and current availability are listed in the [marketplace](https://321ai.cc/#/market).

## Anthropic SDK / Claude Code

```bash
export ANTHROPIC_BASE_URL=https://321ai.cc
export ANTHROPIC_AUTH_TOKEN=sk-...
```

Use the Anthropic model IDs shown in the console or marketplace. For OpenAI-compatible agents, use the `/v1` base URL instead.

## Choosing a route

- **Smart / cheap / stable / fast / guaranteed** groups select channels using different policies.
- **Pin a merchant** when you need a specific supplier or a confirmed merchant quote.
- A pinned channel can fall back to smart routing when the supplier becomes unavailable, depending on the route setting.

## Troubleshooting checklist

1. Confirm the key is active and has access to the model.
2. Confirm the base URL includes `/v1` for OpenAI clients and excludes it for Anthropic clients.
3. Check **Console → Usage Logs** for the request ID and upstream error.
4. If the model is not available in your group, switch to a group that covers it or remove an obsolete pin.
