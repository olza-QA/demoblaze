from playwright.sync_api import sync_playwright, Page
import pytest
from pages.home_page import HomePage
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
def test_view_about_us(home_page:HomePage,page:Page):
    home_page.visit("https://www.demoblaze.com")
    home_page.nav_bar.click_about_us_link()
    home_page.nav_bar.about_us.check_visible()
    home_page.nav_bar.about_us.click_play_button_main()
    home_page.nav_bar.about_us.click_play_video_div()
    home_page.nav_bar.about_us.click_close_button()
    home_page.nav_bar.click_about_us_link()
    home_page.nav_bar.about_us.click_close_icon()



