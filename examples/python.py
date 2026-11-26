#!/usr/bin/env python3
"""Minimal 321AI chat example using the OpenAI Python SDK.

Usage:
  export API_KEY="sk-..."
  python examples/python.py
"""
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url="https://321ai.cc/v1",
)

response = client.chat.completions.create(
    model="gpt-6.1-sol",
    messages=[{"role": "user", "content": "Reply with OK only."}],
    max_tokens=16,
)
print(response.choices[0].message.content)
