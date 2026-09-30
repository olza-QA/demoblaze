from playwright.sync_api import sync_playwright, Page
import pytest
from faker import Faker
from components.place_order_form import PlaceOrderForm
from components.nav_bar import NavBar
from components.product_list import Product
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from components.thak_you_for_purchase_alert import ThankYouForPurchaseAlert
from components.sign_up_form import SignUpForm
from components.log_in_form import LogInForm
import allure
from tools.allure.tags import AllureTag

fake = Faker()
@pytest.mark.flaky(reruns=3, reruns_delay=1)
@pytest.mark.regression
@pytest.mark.parametrize("product_name", [("Iphone 6 32gb")])
@allure.title("E2E: Registration, Log in, Purchase product, Log out")
@allure.tag(AllureTag.REGISTRATION,AllureTag.USER_LOGIN,AllureTag.NAVIGATION,AllureTag.PURCHASE)
@allure.epic("Demoblaze")
@allure.feature("Registration, Log in, Purchase product, Log out")
@allure.story("E2E scenario")
@allure.severity("blocker")
def test_e2e_scenario(page: Page, product_name: str):
    username = fake.name() + "new"
    password = fake.password()
    with allure.step(f'Opening the url "https://www.demoblaze.com"'):
        page.goto("https://www.demoblaze.com")

    nav_bar = NavBar(page)
    sign_up_from = SignUpForm(page)
    log_in_form = LogInForm(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    place_order_form = PlaceOrderForm(page)
    thankyou_alert = ThankYouForPurchaseAlert(page)
    home_page = HomePage(page)

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        dialog.accept()

    nav_bar.check_visible_elements_non_authorized_user()
    nav_bar.click_signup_link()
    sign_up_from.check_visible()
    sign_up_from.fill_form(username, password)
    page.on("dialog", handle_dialog)
    sign_up_from.click_sign_up()
    page.wait_for_timeout(500)  # need for modal message

    nav_bar.click_login_link()
    log_in_form.check_visible()
    log_in_form.fill_form(username, password)
    log_in_form.click_log_in()
    page.wait_for_load_state("load")
    nav_bar.check_visible_elements_authorized_user(username)

    def handle_dialog_purchase(dialog):
        print(f"Modal message: {dialog.message}")
        dialog.accept()

    page.goto("https://www.demoblaze.com")
    home_page.click_phones_category()
    page.wait_for_load_state("load")
    product_list = Product(page,product_name)
    product_list.click_product_link()
    product_page.check_visible()
    page.wait_for_load_state("load")
    page.on("dialog", handle_dialog_purchase)
    product_page.click_add_to_cart_button()
    page.wait_for_timeout(500) #need for modal message

    nav_bar.click_cart_link()
    page.wait_for_load_state("load")
    cart_page.check_visible_selected_product(0)
    cart_page.click_place_order_button()
    page.wait_for_load_state("load")

    place_order_form.fill_form(
        username,"Japan","Tokyo","5444233387779333","September","2026"
    )
    place_order_form.click_purchase()

    thankyou_alert.check_visible()
    thankyou_alert.click_ok_button()

    nav_bar.click_logout_link()


