# Manual QA → Automation Playbook

> **Playbook status: in progress.** I'm building this in public as I turn practical testing questions into repeatable browser checks. The code is still growing. The examples are runnable, and the limits are written down rather than hidden.

This repository uses a small local shop demo so anyone can run the same scenarios without needing a customer account or depending on a third-party site to be online. It behaves like a small storefront, but it is a practice fixture—not a real shop and it never takes payments.

## Start here

1. Read the scenario below and decide what evidence would prove the flow worked.
2. Run the browser tests.
3. Compare the assertions with the behaviour they are meant to protect.
4. Try changing the demo, introduce a defect, and watch which test catches it.

## Example: adding and removing products

The demo has two products:

| Product | Price |
|---|---:|
| Notebook | $8.50 |
| Precision pen | $2.00 |

A single notebook should produce a subtotal of **$8.50**. Adding the pen should bring it to **$10.50**. Removing the notebook should leave the pen in the cart and return the subtotal to **$2.00**.

The important check isn't only that the subtotal changes. The test also checks that removing one product doesn't remove the other one by accident.

## What the current code covers

- The storefront displays both products.
- Adding a product updates the cart and subtotal.
- Adding the same product twice updates its quantity.
- Removing one product leaves the other product alone.
- Required customer fields block an empty checkout.
- An empty cart shows a clear message instead of creating an order.
- A valid demo checkout shows a confirmation and clears the cart.

## Run it locally

Use Python 3.11 or newer.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

Run the small smoke walkthrough separately:

```bash
python first_test.py
```

The suite uses a local HTML file. It doesn't need a server, real account, API key, or external network connection.

## How I'm using this as a learning playbook

I want the test design to stay visible. For every automated assertion, I should be able to explain the user risk, the setup, the expected result, and what a failure would tell us.

Manual exploration comes first when I'm still learning a flow. Automation comes next when a check is repeatable and has a clear result. Not every useful testing question can be reduced to an assertion; this repo is a record of that work in progress.

## Next things I'm working on

- Add keyboard-only checks and explicit focus-order examples.
- Separate the cart calculation from the UI so it can have direct unit tests too.
- Add a clear artifact pattern for screenshots and traces when browser checks fail.
- Keep the manual test notes alongside the cases that later become automation.

I will update this README as those pieces exist. Until then, this is a playbook under active development, not a claim that the test suite covers every checkout risk.

## Contact

- GitHub: [OperaAxe](https://github.com/OperaAxe)
- LinkedIn: [davidchristianj](https://linkedin.com/in/davidchristianj)
- Upwork: [Christian David](https://upwork.com/freelancers/~010e703beaa0687103)
