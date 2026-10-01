from playwright.sync_api import sync_playwright, Page

from pages.home_page import HomePage
from tools.allure.tags import AllureTag
import pytest
import allure

from components.nav_bar import NavBar
from components.log_in_form import LogInForm

@pytest.mark.regression
@pytest.mark.smoke

@pytest.mark.parametrize("username,password", [
    ("username115", "password115")
])
@allure.title("Log in with valid username and password")
@allure.tag(AllureTag.USER_LOGIN,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Authorization")
@allure.story("Log in with valid data")
@allure.severity("critical")
def test_authorization(page:Page, username:str, password:str):
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page.goto("https://www.demoblaze.com")
    nav_bar = NavBar(page)
    log_in_form = LogInForm(page)
    nav_bar.check_visible_elements_non_authorized_user()
    nav_bar.click_login_link()
    log_in_form.check_visible()
    log_in_form.fill_form(username=username, password=password)
    log_in_form.click_log_in()
    nav_bar.check_visible_elements_authorized_user(username=username)


@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Log out")
@allure.tag(AllureTag.AUTHORIZATION,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Authorization")
@allure.story("Log out")
@allure.severity("critical")
def test_log_out(page_with_state:Page):
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page_with_state.goto("https://www.demoblaze.com")
    nav_bar = NavBar(page_with_state)
    nav_bar.check_visible_elements_authorized_user("username115")
    nav_bar.click_logout_link()
    nav_bar.check_visible_elements_non_authorized_user()


@pytest.mark.negative_tc
@pytest.mark.parametrize("username,password", [
    ("username115", "wrong_password115"),
    ("wrong_user115", "password115"),
    ("", ""),
    ("username115", ""),
    ("", "password115")
])
@allure.title("Log in with wrong username/password")
@allure.tag(AllureTag.USER_LOGIN,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Authorization")
@allure.story("Log in with wrong credentials")
@allure.severity("critical")
def test_log_in_with_wrong_credentials(page:Page, username:str, password:str):
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page.goto("https://www.demoblaze.com")
    nav_bar = NavBar(page)
    log_in_form = LogInForm(page)

    nav_bar.check_visible_elements_non_authorized_user()
    nav_bar.click_login_link()
    log_in_form.check_visible()
    log_in_form.fill_form(username=username, password=password)

    def handle_dialog(dialog):
        assert dialog.message in [
            "Wrong password.","User does not exist.","Please fill out Username and Password."
        ]
        print(f"Modal message: {dialog.message}")
        dialog.accept()
    page.on("dialog", handle_dialog)
    log_in_form.click_log_in()
    page.wait_for_timeout(500) #need for modal message








