import time
from selenium.webdriver.common.keys import Keys

from ..utils import wait

from .search_model import Search

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
    
    @wait(1)
    def clear_search_input(self):
        self.page.search_input.clear()
        self.page.search_input.send_keys(Keys.CONTROL, "a")
        self.page.search_input.send_keys(Keys.COMMAND, "a")
        self.page.search_input.send_keys(Keys.DELETE)
    
    @wait(2)
    def click_avatar(self):
        self.page.avatar.click()
    
    def click_logout(self):
        self.page.logout_button.click()

        page = LogoutPage(self.driver, self.driver.current_url)
        page.confirm_logout.click()
    
    def type_search_request(self, request):
        if self.page.is_mobile():
            self.page.open_search()

        self.clear_search_input()
        self.page.search_input.send_keys(request)
    
    @wait(1)
    def input_post_search_request(self, app, request):
        self.type_search_request(request)
        app.models.search.page.posts_tab.click()
    
    @wait(1)
    def input_stocks_search_request(self, app, request):
        self.type_search_request(request)
        app.models.search.page.check_no_results(request)
    
    @wait(1)
    def input_people_search_request(self, app, request):
        self.type_search_request(request)
        app.models.search.page.people_tab.click()
        app.models.search.page.check_people_results(request)
        app.models.search.page.check_visibility(
            'Verified',
            app.models.search.page.verified_locator
        )
    
    @wait(1)
    def input_shop_search_request(self, app, request):
        self.type_search_request(request)
        app.models.search.page.shop_tab.click()
        app.models.search.page.check_shop_results(request)
    
    @wait(1)
    def click_search_button(self):
        self.page.search_button.click()
    
    @wait(1)
    def input_self_search_request(self, app, request):
        self.type_search_request(request)
        app.models.search.page.people_tab.click()
        app.models.search.page.check_invisibility(
            'Self subscription button', 
            app.models.search.page.self_subscription_locator
        )
    
    def close_menu(self):
        self.page.menu.click()
    
    def check_components(self):
        if self.page.is_mobile():
            self.page.check_visibility('Search button', self.page.search_button_locator)
            self.page.check_visibility('Menu', self.page.menu_locator)
        else:
            self.page.check_visibility('Search field', self.page.search_input_locator)
            self.page.check_visibility('Magnifier icon', self.page.magnifier_icon_locator)
            self.page.check_visibility('Search field placeholder', self.page.search_field_placeholder_locator)
    
    def check_clickable_search(self):
        if self.page.is_mobile():
            self.page.open_search()

        if not self.page.is_mobile():
            self.page.magnifier_icon.click()
            self.page.check_search_field_active()

        self.page.search_input.click()
        self.page.check_search_field_active()

        self.page.click_right_corner_search_input()
        self.page.check_search_field_active()

        self.page.click_left_corner_search_input()
        self.page.check_search_field_active()

    def input_search_request(self, app, request):
        self.clear_search_input()
        self.page.search_input.send_keys(request)

        app.models.search.page.check_visibility(
            'Search popup',
            app.models.search.page.search_result_locator
        )
        app.models.search.page.check_tabs()

    def find_without_results(self, app, request):
        self.clear_search_input()
        self.page.search_input.send_keys(request)

        for tab in ['stocks', 'people', 'posts', 'shop']:
            app.models.search.page.switch_tab(tab)
            app.models.search.page.check_no_results(request)
