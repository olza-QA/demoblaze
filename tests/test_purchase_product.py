from playwright.sync_api import sync_playwright, Page
import pytest
from components.product_list import Product
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
import allure
from tools.allure.tags import AllureTag

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.flaky(reruns=3, reruns_delay=1)

@pytest.mark.parametrize("product_name1,product_name2,product_name3", [
    ("Samsung galaxy s6","MacBook air","ASUS Full HD")])
@allure.title("Purchase products")
@allure.tag(AllureTag.NAVIGATION,AllureTag.PURCHASE)
@allure.epic("Demoblaze")
@allure.feature("Purchase products")
@allure.story("Select products, delete product, place order")
@allure.severity("blocker")
def test_purchase_product(home_page:HomePage,cart_page:CartPage,product_page:ProductPage,page:Page,product_name1,product_name2,product_name3):

    def handle_dialog(dialog):
        print(f"Modal message: {dialog.message}")
        assert dialog.message == "Product added"
        dialog.accept()

    home_page.visit("https://www.demoblaze.com")
    home_page.click_phones_category()
    product_list = Product(page,product_name1)
    product_list.click_product_link()
    product_page.check_visible()
    page.on("dialog", handle_dialog)
    product_page.click_add_to_cart_button()
    page.wait_for_timeout(600) #need for modal message

    product_page.nav_bar.click_brand_link("https://www.demoblaze.com/index.html")
    home_page.click_categories_header()
    home_page.click_laptops_category()
    product_list = Product(page, product_name2)
    product_list.click_product_link()
    product_page.check_visible()

    page.on("dialog", handle_dialog)
    product_page.click_add_to_cart_button()
    page.wait_for_timeout(600) #need for modal message
    product_page.nav_bar.click_brand_link("https://www.demoblaze.com/index.html")
    home_page.click_categories_header()
    home_page.click_monitors_category()

    product_list = Product(page, product_name3)
    product_list.click_product_link()
    product_page.check_visible()
    page.on("dialog", handle_dialog)
    product_page.click_add_to_cart_button()
    page.wait_for_timeout(600) #need for modal message

    product_page.nav_bar.click_cart_link()
    cart_page.check_visible_selected_product(0)
    cart_page.check_visible_selected_product(1)
    cart_page.check_visible_selected_product(2)
    cart_page.click_delete_product_button(0)
    page.wait_for_timeout(1300) #need more time for new view
    cart_page.click_place_order_button()
    cart_page.place_order_form.fill_form(
        "Alex","Japan","Tokyo","5444233387779333","September","2026"
    )
    cart_page.place_order_form.click_purchase()
    cart_page.thank_you_alert.check_visible()
    cart_page.thank_you_alert.click_ok_button()











