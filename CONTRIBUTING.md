# Contributing to 321AI

Thanks for helping make the AI model market easier to use.

## Good first contributions

- Fix a broken link or example.
- Add an integration guide for a client we do not cover.
- Improve the error-code or rate-limit docs.
- Reproduce a bug with a request ID and a minimal example.

## Commit style

Use a conventional prefix:

- `feat: add ...`
- `fix: correct ...`
- `docs: explain ...`
- `chore: update ...`

## Never commit

- API keys, tokens, cookies or `.env` files
- Captured traffic containing authorization headers
- Screenshots containing keys, balances or personal data
- Credentials or private upstream configuration

If you accidentally expose a key, revoke it in the console first; deleting the commit is not enough.

## Pull requests

1. Keep the change focused.
2. Explain the user-visible problem and the fix.
3. Include a reproducible command or request ID when relevant.
4. Do not include real model-spend tests in pull requests unless the owner approved them.

By contributing, you agree that your contribution is licensed under the repository's MIT license.
