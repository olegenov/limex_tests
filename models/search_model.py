from .base_model import BaseModel

from ..pages.signin_page import SigninPage
from ..pages.nav_page import NavPage
from ..pages.profile_page import ProfilePage


class Search(BaseModel):
    def click_post(self):
        post = self.page.post_results[0]
        post.click()
    
    def click_name(self, request):
        name = self.page.people_results[1]
        name.click()
        self.page.should_be_right_page('https://ng.tst.whotrades.net/profile/')

        page = ProfilePage(self.driver, self.driver.current_url)
        page.compare_texts(page.name.text, request)

        page = NavPage(self.driver, self.driver.current_url)

        if page.is_mobile():
            page.menu.click()

        page.feed_link.click()
    
    def guest_follow(self):
        self.page.follow_button[0].click()
        page = SigninPage(self.driver, self.driver.current_url)
        page.check_visibility('Signin popup', page.popup_locator)
        self.page.check_visibility('Search', self.page.search_result_locator)
        page.email_button.click()
        self.page.check_invisibility('Search', self.page.search_result_locator)
        page.email_close_button.click()

    def user_follow(self):
        self.page.follow_button[0].click()
        self.page.check_invisibility('Subscription button', self.page.self_subscription_locator)
        self.page.people_results[0].click()
    
    def close_search(self):
        if self.page.is_mobile():
            self.page.close_search()
    
    def click_ticker(self):
        self.page.stocks_results[0].click()
        self.page.should_be_right_page('https://ng.tst.whotrades.net/$')

        page = NavPage(self.driver, self.driver.current_url)

        if page.is_mobile():
            page.menu.click()

        page.feed_link.click()
