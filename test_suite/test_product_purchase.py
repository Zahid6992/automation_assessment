import pytest
import time
from playwright.sync_api import sync_playwright

from pages.product_purchase_page import ProductPurchasePage

class TestProductPurchase:

    @pytest.fixture(scope="function")
    def page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            yield page
            page.close()
            browser.close()

    def test_product_purchase(self, page):
        product_purchase_page = ProductPurchasePage(page)
        product_purchase_page.product_purchase(page)

