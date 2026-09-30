from playwright.sync_api import Page, expect
import allure

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page


    def check_current_url(self,expected_url):
        with allure.step(f"Check that current url is {expected_url}"):
            expect(self.page).to_have_url(expected_url)