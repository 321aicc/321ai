#!/usr/bin/env bash
set -euo pipefail

: "${API_KEY:?set API_KEY first}"

curl -sS https://321ai.cc/v1/chat/completions \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6.1-sol",
    "messages": [{"role": "user", "content": "Reply with OK only."}],
    "max_tokens": 16
  }'
