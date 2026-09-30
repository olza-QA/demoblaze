from playwright.sync_api import Page
from components.nav_bar import NavBar
from components.footer import Footer
from pages.base_page import BasePage
from elements.link import Link
from elements.button import Button


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        nav_bar = NavBar(page)
        footer = Footer(page)

        self.categories_header_link = Link(page,'//div[@class="list-group"]//a[@id="cat"]',"Category header")
        self.phones_category_link = Link(page,'//div[@class="list-group"]//a[text()="Phones"]',"Phones category")
        self.laptops_category_link = Link(page,'//div[@class="list-group"]//a[text()="Laptops"]',"Laptops category")
        self.monitors_category_link = Link(page,'//div[@class="list-group"]//a[text()="Monitors"]',"Monitors category")


        self.previous_page_button = Button(page,'//li//button[@id="prev2"]',"Prev")
        self.next_page_button = Button(page,'//li//button[@id="next2"]',"Next")


    def click_categories_header(self):
        self.categories_header_link.check_visible()
        self.categories_header_link.click()

    def click_phones_category(self):
        self.phones_category_link.check_visible()
        self.phones_category_link.click()

    def click_laptops_category(self):
        self.laptops_category_link.check_visible()
        self.laptops_category_link.click()

    def click_monitors_category(self):
        self.monitors_category_link.check_visible()
        self.monitors_category_link.click()

    def click_next_button(self):
        self.next_page_button.check_visible()
        self.next_page_button.click()

    def click_previous_button(self):
        self.previous_page_button.check_visible()
        self.previous_page_button.click()







