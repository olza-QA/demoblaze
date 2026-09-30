from playwright.sync_api import Page
import allure

from components.about_us import AboutUs
from components.base_component import BaseComponent
from components.contact_form import ContactForm
from components.log_in_form import LogInForm
from components.sign_up_form import SignUpForm
from elements.text import Text
from elements.link import Link



class NavBar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        log_in_form = LogInForm(page)
        signup_form = SignUpForm(page)
        contact_form = ContactForm(page)
        about_us = AboutUs(page)

        self.brand_link = Link(page,"#nava",'Brand')
        self.home_link = Link(page,'//li//a[@href="index.html"]','Home')
        self.contact_link = Link(page,'a[data-target="#exampleModal"]','Contact')
        self.about_us_link = Link(page,'a[data-target="#videoModal"]','About us')
        self.cart_link = Link(page,"#cartur",'Cart')
        self.login_link = Link(page,"#login2",'Log in')
        self.logout_link = Link(page,"#logout2",'Log out')
        self.username_label = Text(page,"#nameofuser",'Username label')
        self.signup_link = Link(page,"#signin2",'Sign up')


    def check_visible_elements(self):
        self.brand_link.check_visible()
        self.brand_link.check_text("PRODUCT STORE")
        self.home_link.check_visible()
        self.home_link.check_text("Home (current)")
        self.contact_link.check_visible()
        self.contact_link.check_text("Contact")
        self.about_us_link.check_visible()
        self.about_us_link.check_text("About us")
        self.cart_link.check_visible()
        self.cart_link.check_text("Cart")

    @allure.step("Check visible navigation for non authorized user")
    def check_visible_elements_non_authorized_user(self):
        self.check_visible_elements()
        self.login_link.check_visible()
        self.login_link.check_text("Log in")
        self.signup_link.check_visible()
        self.signup_link.check_text("Sign up")

    @allure.step("Check visible navigation for authorized user")
    def check_visible_elements_authorized_user(self,username):
        self.check_visible_elements()
        self.logout_link.check_visible()
        self.logout_link.check_text("Log out")
        self.username_label.check_visible()
        self.username_label.check_text(f"Welcome {username}")

    def click_brand_link(self,expected_url):
        self.brand_link.click()
        self.check_current_url(expected_url)

    def click_home_link(self,expected_url):
        self.home_link.click()
        self.check_current_url(expected_url)

    def click_contact_link(self):
        self.contact_link.click()

    def click_about_us_link(self):
        self.about_us_link.click()

    def click_cart_link(self):
        self.cart_link.click()

    def click_login_link(self):
        self.login_link.click()

    def click_logout_link(self):
        self.logout_link.click()

    def click_signup_link(self):
        self.signup_link.click()











