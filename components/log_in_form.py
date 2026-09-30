from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.input import Input
from elements.text import Text

class LogInForm(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)


        self.title = Text(page,"#logInModalLabel",'Log in title form')
        self.username_input = Input(page,"#loginusername",'Username')
        self.password_input = Input(page, "#loginpassword",'Password')
        self.log_in_button = Button(page,'#logInModal button.btn-primary[onclick="logIn()"]','Log in')
        self.close_button_form = Button(page, "#logInModal button.btn-secondary[data-dismiss='modal']","Close")
        self.close_button_form_icon = Icon(page,"#logInModal .modal-header .close",'Close x')

    @allure.step("Check visible 'Log in' form")
    def check_visible(self):
        self.title.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()
        self.log_in_button.check_visible()
        self.close_button_form.check_visible()
        self.close_button_form_icon.check_visible()

    @allure.step("Fill log in form")
    def fill_form(self, username, password):
        self.username_input.fill(username)
        self.username_input.check_have_value(username)
        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_log_in(self):
        self.log_in_button.click()

    def click_close_button_form_icon(self):
        self.close_button_form_icon.click()

    def click_close_button_form(self):
        self.close_button_form.click()





