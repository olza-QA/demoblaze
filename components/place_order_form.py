from playwright.sync_api import Page
from components.base_component import BaseComponent
import allure
from elements.button import Button
from elements.icon import Icon
from elements.input import Input
from elements.text import Text

class PlaceOrderForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,"#orderModal","Title")
        self.total_label = Text(page,"#totalm",'Total')
        self.name_input = Input(page,'//div[@class="modal-body"]//input[@id="name"]',"Name")
        self.country_input = Input(page,'//div[@class="modal-body"]//input[@id="country"]',"Country")
        self.city_input = Input(page, '//div[@class="modal-body"]//input[@id="city"]', "City")
        self.card_input = Input(page, '//div[@class="modal-body"]//input[@id="card"]', "Card")
        self.month_input = Input(page, '//div[@class="modal-body"]//input[@id="month"]', "Month")
        self.year_input = Input(page, '//div[@class="modal-body"]//input[@id="year"]', "Year")
        self.purchase_button = Button(page, "button[onclick='purchaseOrder()']", "Purchase")
        self.close_button = Button(page, "#orderModal button.btn-secondary[data-dismiss='modal']", "Close")
        self.close_button_icon = Icon(page, "#orderModal button.close[data-dismiss='modal']", "Close x")

    @allure.step("Check 'Place order form'")
    def check_visible(self):
        self.title.check_visible()
        self.total_label.check_visible()
        self.name_input.check_visible()
        self.country_input.check_visible()
        self.city_input.check_visible()
        self.card_input.check_visible()
        self.month_input.check_visible()
        self.year_input.check_visible()
        self.purchase_button.check_visible()
        self.close_button.check_visible()
        self.close_button_icon.check_visible()

    @allure.step("Fill 'Place order form'")
    def fill_form(self, name, country, city,card, month, year):
        self.name_input.fill(name)
        self.country_input.fill(country)
        self.city_input.fill(city)
        self.card_input.fill(card)
        self.month_input.fill(month)
        self.year_input.fill(year)

    def click_purchase(self):
        self.purchase_button.click()

    def click_close_button(self):
        self.close_button.click()

    def click_close_button_icon(self):
        self.close_button_icon.click()

