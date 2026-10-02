from playwright.sync_api import sync_playwright, Page
import pytest
from pages.home_page import HomePage
import allure
from tools.allure.tags import AllureTag

@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Contact -send message")
@allure.tag(AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Navigation")
@allure.story("Send message")
@allure.severity("normal")
def test_contact(home_page:HomePage,page:Page):

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message == "Thanks for the message!!"
        dialog.accept()

    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.click_contact_link()
    home_page.nav_bar.contact_form.check_visible()
    home_page.nav_bar.contact_form.fill_form("user@gmail.com","username","my message")
    page.on("dialog", handle_dialog)
    home_page.nav_bar.contact_form.click_send_message()
    page.wait_for_timeout(500) #need for modal message



