import pytest
from playwright.sync_api import Page

from fixtures.browsers import page
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@pytest.fixture
def home_page(page: HomePage) ->Page:
    return HomePage(page=page)

@pytest.fixture
def home_page_with_state(page_with_state: HomePage) ->Page:
    return HomePage(page=page_with_state)

@pytest.fixture
def product_page(page: ProductPage) -> Page:
    return ProductPage(page=page)


@pytest.fixture
def cart_page(page: CartPage) -> Page:
    return CartPage(page=page)
