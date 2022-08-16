import time
from selenium.webdriver.common.keys import Keys

from ..utils import wait

from ..pages.nav_page import NavPage

from .base_model import BaseModel
from ..pages.signup_page import SignupPage
from ..pages.signin_page import SigninPage
from ..pages.search_page import SearchPage
from ..pages.logout_page import LogoutPage


class Nav(BaseModel):
    def click_signup_button(self):
        if self.page.is_mobile():
            self.page.menu.click()

        self.page.signup_button.click()
        page = SignupPage(self.driver, self.driver.current_url)
        page.check_visibility('Popup', page.popup_locator)
        page.check_options()
        page.check_visibility('Cross', page.cross_locator)

    def click_login_button(self):
        if self.page.is_mobile():
            self.page.menu.click()

        self.page.signin_button.click()
        page = SigninPage(self.driver, self.driver.current_url)
        page.check_visibility('Popup', page.popup_locator)
        page.check_options()
        page.check_visibility('Cross', page.cross_locator)
    
    def check_signed_in(self):
        self.page.check_visibility(
            'Avatar',
            self.page.avatar_locator
        )
    
    @wait(2)
    def click_avatar(self):
        self.page.avatar.click()
    
    def click_logout(self):
        self.page.logout_button.click()

        page = LogoutPage(self.driver, self.driver.current_url)
        page.confirm_logout.click()
    
    @wait(1)
    def input_post_search_request(self, request):
        self.page.search_input.clear()
        self.page.search_input.send_keys(Keys.CONTROL, "a")
        self.page.search_input.send_keys(Keys.COMMAND, "a")
        self.page.search_input.send_keys(Keys.DELETE)
        self.page.search_input.send_keys(request)
        page = SearchPage(self.driver, self.driver.current_url)
        page.posts_tab.click()
    
    @wait(1)
    def input_stocks_search_request(self, request):
        self.page.search_input.clear()
        self.page.search_input.send_keys(Keys.CONTROL, "a")
        self.page.search_input.send_keys(Keys.COMMAND, "a")
        self.page.search_input.send_keys(Keys.DELETE)
        self.page.search_input.send_keys(request)
        page = SearchPage(self.driver, self.driver.current_url)
        page.check_no_results(request)
    
    @wait(1)
    def input_people_search_request(self, request):
        self.page.search_input.clear()
        self.page.search_input.send_keys(Keys.CONTROL, "a")
        self.page.search_input.send_keys(Keys.COMMAND, "a")
        self.page.search_input.send_keys(Keys.DELETE)
        self.page.search_input.send_keys(request)
        page = SearchPage(self.driver, self.driver.current_url)
        page.people_tab.click()
        page.check_people_results(request)
        page.check_visibility('Verified', page.verified_locator)
    
    @wait(1)
    def click_search_button(self):
        self.page.search_button.click()
    
    @wait(1)
    def input_self_search_request(self, request):
        self.page.search_input.clear()
        self.page.search_input.send_keys(Keys.CONTROL, "a")
        self.page.search_input.send_keys(Keys.COMMAND, "a")
        self.page.search_input.send_keys(Keys.DELETE)
        self.page.search_input.send_keys(request)
        page = SearchPage(self.driver, self.driver.current_url)
        page.people_tab.click()
        page.check_invisibility('Self subscription button', page.self_subscription_locator)
    
    def close_menu(self):
        self.page.menu.click()
