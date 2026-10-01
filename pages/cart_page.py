from playwright.sync_api import Page

from components.footer import Footer
from components.nav_bar import NavBar
from components.thak_you_for_purchase_alert import ThankYouForPurchaseAlert
from pages.base_page import BasePage
from components.place_order_form import PlaceOrderForm
from elements.button import Button
from elements.text import Text
import allure

class CartPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

        self.place_order_form = PlaceOrderForm(page)
        self.nav_bar=NavBar(page)
        self.footer=Footer(page)
        self.thank_you_alert=ThankYouForPurchaseAlert(page)

        self.title_table = Text(page,'//table[@class="table table-bordered table-hover table-striped"]//thead',"Header of table")
        self.selected_product = Text(page,'//table[@class="table table-bordered table-hover table-striped"]//tr[@class="success"]',"Selected product")
        self.delete_product = Button(page,"a[onclick^='deleteItem']:has-text('Delete')","Delete product button")
        self.place_order_button = Button(page,"button[data-target='#orderModal']",'Place Order button')

    @allure.step("Check  selected product at index {nth} is visible")
    def check_visible_selected_product(self,nth:int=0):
        self.title_table.check_visible()
        self.selected_product.check_visible(nth)
        self.delete_product.check_visible(nth)

    @allure.step("Delete selected product at index {nth}")
    def click_delete_product_button(self,nth:int=0):
        self.delete_product.click(nth)

    def click_place_order_button(self):
        self.place_order_button.click()



