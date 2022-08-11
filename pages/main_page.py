from .base_page import BasePage
from ..locators.main_locators import MainLocators


class MainPage(BasePage):
    @property
    def post(self):
        return self.get_element(
            'Post',
            MainLocators.POST
        )

    @property
    def hint(self):
        return self.get_element(
            'Hint',
            MainLocators.CLOSE_HINT,
        )
