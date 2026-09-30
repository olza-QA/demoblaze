
from components.base_component import BaseComponent
from elements.link import Link
from elements.image import Image
from elements.text import Text
import allure

class Product(BaseComponent):
    def __init__(self,page,prod_name):
        super().__init__(page)

        self.product_image = Image(page,
            f'//div[@class="card h-100"]//a[text()="{prod_name}"]//img',"Product image")
        self.product_link = Link(page,
            f'//div[@class="card h-100"]//a[text()="{prod_name}"]',"Product link")
        self.product_price =Text(page,
            f'//div[@class="card h-100"]//a[text()={prod_name}]//following-sibling::div[1]/h5',"Price")
        self.product_article = Text(page,
            f'//div[@class="card h-100"]/a[contains(@href, "prod.html?idp_={prod_name}")]/following-sibling::div[1]/p',"Product description")

    @allure.step("Check product image, name, price, description")
    def check_visible(self):
        self.product_image.check_visible()
        self.product_link.check_visible()
        self.product_price.check_visible()
        self.product_article.check_visible()

    def click_product_link(self):
        self.product_link.click()
