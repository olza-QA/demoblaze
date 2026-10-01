from playwright.sync_api import sync_playwright, Page

from pages.home_page import HomePage
from tools.allure.tags import AllureTag
import pytest
import allure


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
def test_authorization(home_page:HomePage,username:str, password:str):
    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.check_visible_elements_non_authorized_user()
    home_page.nav_bar.click_login_link()
    home_page.nav_bar.log_in_form.check_visible()
    home_page.nav_bar.log_in_form.fill_form(username=username, password=password)
    home_page.nav_bar.log_in_form.click_log_in()
    home_page.nav_bar.check_visible_elements_authorized_user(username=username)


@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Log out")
@allure.tag(AllureTag.AUTHORIZATION,AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Authorization")
@allure.story("Log out")
@allure.severity("critical")
def test_log_out(home_page_with_state:HomePage):
    home_page_with_state.visit("https://www.demoblaze.com")
    home_page_with_state.nav_bar.check_visible_elements_authorized_user("username115")
    home_page_with_state.nav_bar.click_logout_link()
    home_page_with_state.nav_bar.check_visible_elements_non_authorized_user()


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
def test_log_in_with_wrong_credentials(home_page:HomePage, page:Page,username:str, password:str):
    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.check_visible_elements_non_authorized_user()
    home_page.nav_bar.click_login_link()
    home_page.nav_bar.log_in_form.check_visible()
    home_page.nav_bar.log_in_form.fill_form(username=username, password=password)

    def handle_dialog(dialog):
        assert dialog.message in [
            "Wrong password.","User does not exist.","Please fill out Username and Password."
        ]
        print(f"Modal message: {dialog.message}")
        dialog.accept()
    page.on("dialog", handle_dialog)
    home_page.nav_bar.log_in_form.click_log_in()
    page.wait_for_timeout(500) #need for modal message








