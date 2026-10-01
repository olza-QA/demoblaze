from playwright.sync_api import sync_playwright, Page
import pytest
from faker import Faker
from components.product_list import Product
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
import allure
from tools.allure.tags import AllureTag

fake = Faker()
@pytest.mark.flaky(reruns=1, reruns_delay=1)
@pytest.mark.regression
@pytest.mark.parametrize("product_name", [("Iphone 6 32gb")])
@allure.title("E2E: Registration, Log in, Purchase product, Log out")
@allure.tag(AllureTag.REGISTRATION,AllureTag.USER_LOGIN,AllureTag.NAVIGATION,AllureTag.PURCHASE)
@allure.epic("Demoblaze")
@allure.feature("Registration, Log in, Purchase product, Log out")
@allure.story("E2E scenario")
@allure.severity("blocker")
def test_e2e_scenario(home_page:HomePage,page: Page, product_name: str):
    username = fake.name() + "new"
    password = fake.password()
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        dialog.accept()

    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.check_visible_elements_non_authorized_user()
    home_page.nav_bar.click_signup_link()
    home_page.nav_bar.sign_up_form.check_visible()
    home_page.nav_bar.sign_up_form.fill_form(username, password)
    page.on("dialog", handle_dialog)
    home_page.nav_bar.sign_up_form.click_sign_up()
    page.wait_for_timeout(500)  # need for modal message

    home_page.nav_bar.click_login_link()
    home_page.nav_bar.log_in_form.check_visible()
    home_page.nav_bar.log_in_form.fill_form(username, password)
    home_page.nav_bar.log_in_form.click_log_in()
    home_page.nav_bar.check_visible_elements_authorized_user(username)

    home_page.nav_bar.click_home_link("https://www.demoblaze.com/index.html")
    home_page.click_phones_category()

    product_list = Product(page,product_name)
    product_list.click_product_link()
    product_page.check_visible()
    page.on("dialog", handle_dialog)
    product_page.click_add_to_cart_button()
    page.wait_for_timeout(500) #need for modal message
    product_page.nav_bar.click_cart_link()

    cart_page.check_visible_selected_product(0)
    cart_page.click_place_order_button()
    cart_page.place_order_form.fill_form(
        username,"Japan","Tokyo","5444233387779333","September","2026"
    )
    cart_page.place_order_form.click_purchase()
    cart_page.thank_you_alert.check_visible()
    cart_page.thank_you_alert.click_ok_button()
    cart_page.nav_bar.click_logout_link()


