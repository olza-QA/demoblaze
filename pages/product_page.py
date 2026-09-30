from playwright.sync_api import Page, expect

from components.footer import Footer
from components.nav_bar import NavBar
from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text
import allure


class ProductPage(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        nav_bar=NavBar(page)
        footer=Footer(page)

        self.product_title = Text(page,'//div[@id="tbodyid"]//h2','Product title')
        self.product_price = Text(page,'//div[@id="tbodyid"]//h3','Product price')
        self.product_description = Text(page,'//div[@id="tbodyid"]//p','Product description')
        self.product_image = Image(page,'//div[@class="product-image"]//img','Product image')
        self.add_to_cart_button = Button(page,'//a[text()="Add to cart"]','Add to-cart')

    @allure.step("Check product name, image,price,description")
    def check_visible(self):
        self.product_title.check_visible()
        self.product_price.check_visible()
        self.product_description.check_visible()
        self.product_image.check_visible()
        self.add_to_cart_button.check_visible()

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()