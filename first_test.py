"""Open the local QA-playbook storefront and print a tiny smoke-check summary."""

from pathlib import Path

from playwright.sync_api import sync_playwright


DEMO_URL = (Path(__file__).resolve().parent / "demo" / "storefront.html").as_uri()


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(DEMO_URL)
            title = page.title()
            product_count = page.get_by_test_id("product-card").count()
            page.get_by_test_id("add-notebook").click()
            subtotal = page.get_by_test_id("cart-total").inner_text()
            print(f"Title: {title}")
            print(f"Products shown: {product_count}")
            print(f"Subtotal after adding Notebook: {subtotal}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
