# Error codes

321AI returns OpenAI-compatible error envelopes:

```json
{
  "error": {
    "message": "…",
    "type": "new_api_error",
    "code": ""
  }
}
```

| HTTP | Meaning | Action |
|---|---|---|
| 400 | Invalid request, malformed JSON, unsupported parameter | Fix the request body or model name |
| 401 | Missing or invalid API key | Check the Bearer token and key status |
| 403 | Key cannot use the requested model/group, or account balance is negative | Check token model limits, group and balance |
| 404 | Model or route not found | Refresh the model list and retry |
| 429 | Rate limit | Back off and retry with jitter |
| 500/502/503/504 | Gateway or upstream failure | Retry with backoff; failed requests are not billed |

## Request IDs

Every response includes a request ID (for example `x-oneapi-request-id`). Include it when opening a support ticket.

## Billing on errors

Failed requests are not billed. A temporary authorization may be reserved and is released automatically when the request fails.

## Reporting a reproducible problem

Open an issue with the model, request time, request ID, HTTP status and the error message. Do not include API keys, prompts containing personal data, or full response bodies with secrets.
