"""Shared browser fixtures for the storefront test suite."""

from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import Page

DEMO_URL = (Path(__file__).resolve().parents[1] / "demo" / "storefront.html").as_uri()


@pytest.fixture
def shop_page(page: Page) -> Page:
    """Open the demo storefront and return the page object."""
    page.goto(DEMO_URL)
    return page
