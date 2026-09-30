from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text
import allure



class AboutUs(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.title= Text(page,"#videoModalLabel", "About us title")
        self.play_button_main= Button(page,"button.vjs-big-play-button",'Play video button')
        self.play_video_div = Button(page,"#example-video_html5_api","play video div")
        self.close_button_form =Button(page,"#videoModal button.btn-secondary[data-dismiss='modal']",'Close')
        self.close_button_form_icon = Icon(page,"#videoModal button.close[data-dismiss='modal']",'Close x')

    @allure.step("Check visible 'About Us' pop-up")
    def check_visible(self):
        self.title.check_visible()
        self.play_button_main.check_visible()
        self.play_video_div.check_visible()
        self.close_button_form.check_visible()
        self.close_button_form_icon.check_visible()

    @allure.step("Play video via main button")
    def click_play_button_main(self):
        self.play_button_main.click()

    @allure.step("Click on video")
    def click_play_video_div(self):
        self.play_video_div.click()


    def click_close_icon(self):
        self.close_button_form_icon.click()

    def click_close_button(self):
        self.close_button_form.click()
