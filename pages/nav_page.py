import time
from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage

from ..locators.nav_locators import NavLocators


class NavPage(BasePage):
    @property
    def feed_link(self):
        if self.is_mobile():
            locator = NavLocators.FEED_LINK_MOBILE
        else:
            locator = NavLocators.FEED_LINK
    
        return self.get_element(
            'Feed link',
            locator
        )

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
    def logout_button(self):
        return self.get_clickable_element(
            'Logout button',
            NavLocators.LOGOUT_BUTTON
        )

    @property
    def avatar(self):
        return self.get_clickable_element(
            'Avatar',
            self.avatar_locator
        )

    @property
    def avatar_locator(self):
        return NavLocators.AVATAR
    
    @property
    def search_input(self):
        return self.get_element(
            'Search input',
           self.search_input_locator
        )
    
    @property
    def search_input_locator(self):
        if self.is_mobile():
            locator = NavLocators.SEARCH_INPUT_MOBILE
        else:
            locator = NavLocators.SEARCH_INPUT

        return locator

    @property
    def search_button(self):
        return self.get_clickable_element(
            'Search button',
            NavLocators.SEARCH_BUTTON
        )
    
    @property
    def magnifier_icon(self):
        return self.get_clickable_element(
            'Magnifier icon',
            self.magnifier_icon_locator
        )
    
    @property
    def magnifier_icon_locator(self):
        return NavLocators.MAGNIFIER_ICON
    
    @property
    def search_field_placeholder_locator(self):
        return NavLocators.SEARCH_FIELD_PLACEHOLDER

    @property
    def menu(self):
        return self.get_clickable_element(
            'Menu',
            NavLocators.MENU
        )
    
    def check_search_field_active(self):
        assert self.search_input == self.driver.switch_to.active_element,\
               'Search field is not active'
    
    def click_right_corner_search_input(self):
        element = self.search_input
        size = element.size
        height, width = size['height'], size['width']
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, width//2, height//2)
        action.click()
        action.perform()
    
    def click_left_corner_search_input(self):
        element = self.search_input
        size = element.size
        height, width = size['height'], size['width']
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, width//2, 0)
        action.click()
        action.perform()
