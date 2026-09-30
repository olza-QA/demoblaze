from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.icon import Icon
from elements.input import Input

class SignUpForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "#signInModalLabel", "Title")
        self.username_input = Input(page, "#sign-username", "Username")
        self.password_input = Input(page, "#sign-password", "Password")
        self.sign_up_button_form = Button(page, 'button.btn-primary[onclick="register()"]', "Sign up")
        self.close_button_form_icon = Icon(page, "#signInModal button.close[data-dismiss='modal']", "Close x")
        self.close_button_form = Button(page, "#signInModal button.btn.btn-secondary[data-dismiss='modal']", "Close")

    @allure.step("Check 'Sign up form'")
    def check_visible(self):
        self.title.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()
        self.sign_up_button_form.check_visible()
        self.close_button_form_icon.check_visible()
        self.close_button_form.check_visible()

    @allure.step("Fill 'Sign up form'")
    def fill_form(self,username,password):
        self.username_input.fill(username)
        self.username_input.check_have_value(username)
        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_sign_up(self):
        self.sign_up_button_form.click()

    def click_close_icon(self):
        self.close_button_form_icon.click()

    def click_close_button(self):
        self.close_button_form.click()


