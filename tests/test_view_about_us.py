from playwright.sync_api import sync_playwright, Page
import pytest

from components.nav_bar import NavBar
from components.about_us import AboutUs
import allure
from tools.allure.tags import AllureTag

@pytest.mark.regression
@pytest.mark.smoke
@allure.title("About us - view video")
@allure.tag(AllureTag.NAVIGATION)
@allure.epic("Demoblaze")
@allure.feature("Navigation")
@allure.story("View About us")
@allure.severity("minor")
def test_view_about_us(page:Page):
    nav_bar = NavBar(page)
    about_us = AboutUs(page)
    with allure.step(f'Opening the url https://www.demoblaze.com'):
        page.goto("https://www.demoblaze.com")

    nav_bar.click_about_us_link()
    about_us.check_visible()
    about_us.click_play_button_main()
    about_us.click_play_video_div()
    about_us.click_close_button()
    nav_bar.click_about_us_link()
    about_us.click_close_icon()


