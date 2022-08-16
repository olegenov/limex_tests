from .base_page import BasePage

from ..locators.logout_locators import LogoutLocators


class LogoutPage(BasePage):
    @property
    def confirm_logout(self):
        return self.get_element(
            'Logout confirm',
            LogoutLocators.LOGOUT_CONFIRM
        )