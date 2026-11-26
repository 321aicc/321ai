// Minimal 321AI chat example using the OpenAI Node SDK.
// Usage: API_KEY=sk-... node examples/node.mjs
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.API_KEY,
  baseURL: "https://321ai.cc/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-6.1-sol",
  messages: [{ role: "user", content: "Reply with OK only." }],
  max_tokens: 16,
});

console.log(response.choices[0]?.message?.content);
