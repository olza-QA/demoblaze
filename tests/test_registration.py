from playwright.sync_api import sync_playwright, Page
import pytest
from faker import Faker
import allure
from tools.allure.tags import AllureTag
from pages.home_page import HomePage

fake = Faker()

@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Registration with valid data")
@allure.tag(AllureTag.REGISTRATION,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Registration")
@allure.story("Registration with valid data")
@allure.severity("critical")
def test_successful_registration(home_page:HomePage,page:Page):
    username = fake.name() + "2026"
    password = fake.password()

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message == "Sign up successful."
        dialog.accept()

    home_page.visit("https://www.demoblaze.com")

    home_page.nav_bar.check_visible_elements_non_authorized_user()
    home_page.nav_bar.click_signup_link()
    home_page.nav_bar.sign_up_form.check_visible()
    home_page.nav_bar.sign_up_form.fill_form(username,password)
    page.on("dialog", handle_dialog)
    home_page.nav_bar.sign_up_form.click_sign_up()
    page.wait_for_timeout(600) #need for modal message


@pytest.mark.negative_tc
@pytest.mark.parametrize("username,password", [
    ("username115", "password115"),
    ("", ""),
    ("username", ""),
    ("", "password")])
@allure.title("Registration with invalid data")
@allure.tag(AllureTag.REGISTRATION,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Registration")
@allure.story("Registration with invalid data + existed user")
@allure.severity("critical")
def test_registration_with_invalid_data(home_page:HomePage,page:Page, username:str, password:str):

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message in ("Please fill out Username and Password.","This user already exist.")
        dialog.accept()

    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.click_signup_link()
    home_page.nav_bar.sign_up_form.check_visible()
    home_page.nav_bar.sign_up_form.fill_form(username=username, password=password)
    page.on("dialog", handle_dialog)
    home_page.nav_bar.sign_up_form.click_sign_up()
    page.wait_for_timeout(500) #need for modal message


