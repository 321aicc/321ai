# FAQ

## Is this the official API of OpenAI, Anthropic or Google?

No. 321AI is an independent aggregation gateway. Model names and trademarks belong to their owners. The gateway is compatible with common OpenAI/Anthropic protocols but is not an official endpoint.

## Which base URL should I use?

- OpenAI-compatible clients: `https://321ai.cc/v1`
- Anthropic-compatible clients: `https://321ai.cc`

## Are failed requests billed?

No. Failed requests are not billed; temporary reservations are released.

## Why does a model show as unavailable?

It may have no live supplier quote, or the suppliers may be temporarily failing. Check the marketplace and retry later. If a pinned supplier is unavailable, the pin's fallback setting determines whether smart routing can take over.

## How do I get a specific merchant?

Use **Pin merchant** in the marketplace/console for the model and token. The confirmed merchant price is shown when the pin is created.

## Do you train on my prompts?

The platform is a routing layer; prompts are sent to the selected upstream supplier to fulfill the request. Do not send secrets or regulated data. See the privacy policy on [321ai.cc](https://321ai.cc).

## How do I report a security issue?

Do not open a public issue with credentials or exploit details. Contact the operator through the website support channel first.
