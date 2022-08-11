import time

from .base_page import BasePage

from ..locators.nav_locators import NavLocators


class NavPage(BasePage):
    @property
    def signup_button(self):
        if self.is_mobile():
            locator = NavLocators.SIGNUP_MENU_BUTTON
        else:
            locator = NavLocators.SIGNUP_BUTTON

        return self.get_element(
            'Signup button',
            locator,
        )
    
    @property
    def signin_button(self):
        if self.is_mobile():
            locator = NavLocators.SIGNIN_MENU_BUTTON
        else:
            locator = NavLocators.SIGNIN_BUTTON
    
        return self.get_element(
            'Signin button',
            locator,
        )
    
    @property
    def avatar_locator(self):
        return NavLocators.AVATAR
    
    @property
    def search_input(self):
        if self.is_mobile():
            locator = NavLocators.SEARCH_INPUT_MOBILE
        else:
            locator = NavLocators.SEARCH_INPUT

        return self.get_element(
            'Search input',
            locator
        )

    @property
    def search_button(self):
        return self.get_element(
            'Search button',
            NavLocators.SEARCH_BUTTON
        )
    
    @property
    def menu(self):
        return self.get_element(
            'Menu',
            NavLocators.MENU
        )