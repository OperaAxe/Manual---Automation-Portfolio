# Manual QA → Automation Playbook

[![CI](https://github.com/OperaAxe/Manual---Automation-Portfolio/actions/workflows/playbook-tests.yml/badge.svg)](https://github.com/OperaAxe/Manual---Automation-Portfolio/actions/workflows/playbook-tests.yml)

A small local storefront for practising how a manual test idea becomes a repeatable Playwright check. The fixture is included in the repository, so the scenarios do not depend on a third-party site being available.

This is not a real shop. It does not take payments or create real orders.

## Try a cart scenario

The storefront has two products:

| Product | Price |
|---|---:|
| Notebook | $8.50 |
| Precision pen | $2.00 |

Add both products and the subtotal should be **$10.50**. Remove the notebook and the pen should remain, with a subtotal of **$2.00**. The second assertion matters: removing one item should not silently remove another.

## What the tests cover

- Both products render in the storefront.
- Adding a product updates the cart and subtotal.
- Adding the same product twice updates its quantity.
- Removing one product leaves the other in the cart.
- Required customer fields prevent an empty checkout.
- An empty cart cannot create a demo order.
- A valid demo checkout shows a confirmation and clears the cart.

## Run it

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

The storefront is local HTML and does not need an account, API key, or external network connection.

## Next additions

The playbook is still in progress. Planned additions include keyboard-only checks, direct tests for cart calculations, and more useful screenshot or trace evidence for failed browser runs.
