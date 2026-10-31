"""Browser tests against the local demo storefront; no production account is used."""

from __future__ import annotations

import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_storefront_exposes_two_products(shop_page) -> None:
    expect(shop_page.get_by_role("heading", name="Products")).to_be_visible()
    expect(shop_page.get_by_test_id("product-card")).to_have_count(2)


def test_adding_a_notebook_updates_subtotal(shop_page) -> None:
    shop_page.get_by_test_id("add-notebook").click()

    expect(shop_page.get_by_test_id("cart-items")).to_contain_text("Notebook × 1")
    expect(shop_page.get_by_test_id("cart-total")).to_have_text("$8.50")


def test_repeated_add_updates_quantity_and_total(shop_page) -> None:
    shop_page.get_by_test_id("add-notebook").click()
    shop_page.get_by_test_id("add-notebook").click()

    expect(shop_page.get_by_test_id("cart-items")).to_contain_text("Notebook × 2")
    expect(shop_page.get_by_test_id("cart-total")).to_have_text("$17.00")


def test_removing_one_item_preserves_the_other(shop_page) -> None:
    shop_page.get_by_test_id("add-notebook").click()
    shop_page.get_by_test_id("add-pen").click()
    expect(shop_page.get_by_test_id("cart-total")).to_have_text("$10.50")

    shop_page.get_by_test_id("remove-notebook").click()

    expect(shop_page.get_by_test_id("cart-items")).not_to_contain_text("Notebook")
    expect(shop_page.get_by_test_id("cart-items")).to_contain_text("Precision pen × 1")
    expect(shop_page.get_by_test_id("cart-total")).to_have_text("$2.00")


def test_required_name_and_email_block_empty_checkout(shop_page) -> None:
    shop_page.get_by_test_id("place-order").click()

    name_valid = shop_page.locator("#customer-name").evaluate("(el) => el.validity.valid")
    email_valid = shop_page.locator("#customer-email").evaluate("(el) => el.validity.valid")
    expect(shop_page.get_by_test_id("order-confirmation")).to_be_hidden()
    assert name_valid is False
    assert email_valid is False


def test_empty_cart_shows_a_helpful_checkout_message(shop_page) -> None:
    shop_page.get_by_label("Full name").fill("Ada Example")
    shop_page.get_by_label("Email address").fill("ada@example.test")
    shop_page.get_by_test_id("place-order").click()

    expect(shop_page.get_by_test_id("checkout-error")).to_have_text(
        "Add at least one item before checkout."
    )
    expect(shop_page.get_by_test_id("order-confirmation")).to_be_hidden()


def test_valid_demo_order_shows_confirmation_and_clears_cart(shop_page) -> None:
    shop_page.get_by_test_id("add-notebook").click()
    shop_page.get_by_test_id("add-pen").click()
    shop_page.get_by_label("Full name").fill("Ada Example")
    shop_page.get_by_label("Email address").fill("ada@example.test")
    shop_page.get_by_test_id("place-order").click()

    expect(shop_page.get_by_test_id("order-confirmation")).to_contain_text(
        "Order recorded for Ada Example. Demo total: $10.50. No payment was taken."
    )
    expect(shop_page.get_by_test_id("cart-total")).to_have_text("$0.00")
    expect(shop_page.get_by_test_id("cart-items")).to_be_empty()
