from playwright.sync_api import sync_playwright, Page
import pytest

from components.nav_bar import NavBar
from components.contact_form import ContactForm
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
def test_contact(page:Page):
    nav_bar = NavBar(page)
    contact_form = ContactForm(page)
    with allure.step(f'Opening the url https://www.demoblaze.com'):
        page.goto("https://www.demoblaze.com")

    nav_bar.click_contact_link()
    contact_form.check_visible()

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message == "Thanks for the message!!"
        dialog.accept()
    contact_form.fill_form("user@gmail.com","username","my message")
    page.on("dialog", handle_dialog)
    contact_form.click_send_message()
    page.wait_for_timeout(500) #need for modal message


