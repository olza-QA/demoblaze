from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.input import Input
from elements.text import Text
from elements.textarea import Textarea

class ContactForm(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.title = Text(page,"#exampleModalLabel",'Contact form title')
        self.contact_email_input = Input(page,"#recipient-email",'Email')
        self.contact_name_input = Input(page,"#recipient-name",'Name')
        self.message_text_textarea=Textarea(page,"#message-text",'Message')
        self.send_message_button = Button(page,"button[onclick='send()']",'Send message')
        self.close_button_form = Button(page,"#exampleModal button.btn-secondary[data-dismiss='modal']",'Close')
        self.close_button_form_icon = Icon(page,"#exampleModal button.close[data-dismiss='modal']",'Close x ')

    @allure.step("Check visible 'Contact' pop-up")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_text("New message")
        self.contact_email_input.check_visible()
        self.contact_name_input.check_visible()
        self.message_text_textarea.check_visible()
        self.send_message_button.check_visible()
        self.send_message_button.check_text("Send message")
        self.close_button_form_icon.check_visible()
        self.close_button_form_icon.check_text("×")
        self.close_button_form.check_visible()
        self.close_button_form.check_text("Close")

    @allure.step("Fill contact form")
    def fill_form(self, email, name, message):
        self.contact_email_input.fill(email)
        self.contact_email_input.check_have_value(email)
        self.contact_name_input.fill(name)
        self.contact_name_input.check_have_value(name)
        self.message_text_textarea.fill(message)
        self.message_text_textarea.check_have_value(message)

    def click_send_message(self):
        self.send_message_button.click()

    def click_close_first(self):
        self.close_button_form_icon.click()

    def click_close_second(self):
        self.close_button_form.click()


