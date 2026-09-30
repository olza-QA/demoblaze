from tkinter import dialog

from playwright.sync_api import sync_playwright, Page, expect
import pytest
from faker import Faker
from components.nav_bar import NavBar
from components.sign_up_form import SignUpForm
import allure
from tools.allure.tags import AllureTag

fake = Faker()

@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Registration with valid data")
@allure.tag(AllureTag.REGISTRATION,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Registration")
@allure.story("Registration with valid data")
@allure.severity("critical")
def test_successful_registration(page:Page):
    username = fake.name() + "2026"
    password = fake.password()
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page.goto("https://www.demoblaze.com")

    nav_bar = NavBar(page)
    sign_up_from = SignUpForm(page)


    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message == "Sign up successful."
        dialog.accept()

    nav_bar.check_visible_elements_non_authorized_user()
    nav_bar.click_signup_link()
    sign_up_from.check_visible()
    sign_up_from.fill_form(username,password)
    page.on("dialog", handle_dialog)
    sign_up_from.click_sign_up()
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
def test_registration_with_invalid_data(page:Page, username:str, password:str):
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page.goto("https://www.demoblaze.com")

    nav_bar = NavBar(page)
    sign_up_from = SignUpForm(page)

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message in ("Please fill out Username and Password.","This user already exist.")
        dialog.accept()

    nav_bar.click_signup_link()
    sign_up_from.check_visible()
    sign_up_from.fill_form(username=username, password=password)

    page.on("dialog", handle_dialog)
    sign_up_from.click_sign_up()
    page.wait_for_timeout(500) #need for modal message


