from playwright.sync_api import Page, expect
from elements.text import Text
from components.base_component import BaseComponent
import allure

class Footer(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.about_us_title = Text(page,'//h4[@class="grrrr"]//b[text()="About Us"]','Footer:About Us')
        self.get_in_touch_title = Text(page,'//h4[@class="grrrr"]//b[text()="Get in Touch"]','Footer:Get in Touch')
        self.store_title = Text(page,'//div[@class="caption"]//h4//img','Footer: PRODUCT STORE')
        self.copyright_text = Text(page,'//footer//p','Footer:Copyright text')

    @allure.step("Check visible footer")
    def check_visible_element(self):
        self.about_us_title.check_visible()
        self.get_in_touch_title.check_visible()
        self.store_title.check_visible()
        self.copyright_text.check_visible()






