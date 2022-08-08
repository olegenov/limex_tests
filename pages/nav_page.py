import time

from .base_page import BasePage

from ..locators.nav_locators import NavLocators


class NavPage(BasePage):
    @property
    def signup_button(self):
        return self.get_element(
            'Signup button',
            NavLocators.SIGNUP_BUTTON,
        )
    
    @property
    def signin_button(self):
        return self.get_element(
            'Signin button',
            NavLocators.SIGNIN_BUTTON,
        )
    
    @property
    def avatar_locator(self):
        return NavLocators.AVATAR

    def close_hint(self):
        hint = self.get_element(
            'Hint',
            NavLocators.CLOSE_HINT,
        )
        hint.click()
