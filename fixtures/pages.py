import pytest
from playwright.sync_api import Page

from fixtures.browsers import page
from pages.home_page import HomePage

@pytest.fixture
def home_page(page: HomePage) ->Page:
    return HomePage(page=page)

@pytest.fixture
def home_page_with_state(page_with_state: HomePage) ->Page:
    return HomePage(page=page_with_state)