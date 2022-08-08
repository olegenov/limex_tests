import time

from .base_model import BaseModel
from ..pages.signup_page import SignupPage
from ..pages.signin_page import SigninPage


class Nav(BaseModel):
    def click_signup_button(self):
        self.page.close_hint()
        self.page.signup_button.click()
        self.page = SignupPage(self.driver, self.driver.current_url)
        self.page.check_visibility('Popup', self.page.popup_locator)
        self.page.check_options()
        self.page.check_visibility('Cross', self.page.cross_locator)

    def click_login_button(self):
        self.page.close_hint()
        self.page.signin_button.click()
        self.page = SigninPage(self.driver, self.driver.current_url)
        self.page.check_visibility('Popup', self.page.popup_locator)
        self.page.check_options()
        self.page.check_visibility('Cross', self.page.cross_locator)