from playwright.sync_api import expect
from elements.base_element import BaseElement
import allure

class Textarea(BaseElement):
    @property
    def type_of(self):
        return 'textarea'

    def fill(self,value: str,**kwargs) :
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

    def check_have_value(self,value: str,**kwargs) :
        with allure.step(f'Check {self.type_of} {self.name} has a value "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)