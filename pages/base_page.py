from playwright.sync_api import Page
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Go to url {url}")
    def visit(self, url: str):
        self.page.goto(url)

    def reload(self):
        self.page.reload(wait_until='domcontentloaded')