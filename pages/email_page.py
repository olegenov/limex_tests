from .base_page import BasePage

from ..locators.email_locators import EmailLocators


class EmailPage(BasePage):
    @property
    def signup_button(self):
        return self.get_element(
            'Signup button',
            EmailLocators.SIGNUP_BUTTON
        )
    
    @property
    def pin(self):
        return self.get_element(
            'Pin',
            EmailLocators.PIN
        )
