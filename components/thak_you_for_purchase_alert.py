from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.icon import Icon
import allure

class ThankYouForPurchaseAlert(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.alert_icon = Icon(page, '//div[@class="sa-icon sa-success animate"]', "Alert icon")
        self.alert_thank_you_text = Text(page, '//div[@class="sweet-alert  showSweetAlert visible"]//h2',"Thank you text")
        self.ok_button = Button(page, '//div[@class="sa-confirm-button-container"]//button', "OK")

    @allure.step("Check 'Thank you' alert")
    def check_visible(self):
        self.alert_icon.check_visible()
        self.alert_thank_you_text.check_visible()
        self.ok_button.check_visible()


    def click_ok_button(self):
        self.ok_button.click()