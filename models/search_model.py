from .base_model import BaseModel

from ..pages.signin_page import SigninPage
from ..pages.nav_page import NavPage
from ..pages.profile_page import ProfilePage


class Search(BaseModel):
    def click_post(self):
        post = self.page.post_results[0]
        post.click()
    
    def click_name(self, app, request):
        name = self.page.people_results[0]
        name.click()
        self.page.should_be_right_page('https://ng.tst.whotrades.net/profile/')
        app.models.profile.page.compare_texts(app.models.profile.page.name.text, request)

        if app.models.nav.page.is_mobile():
            app.models.nav.page.menu.click()

        app.models.nav.page.feed_link.click()
    
    def guest_follow(self, app):
        self.page.follow_button[0].click()
        app.models.signin.page.check_visibility(
            'Signin popup',
            app.models.signin.page.popup_locator
        )
        self.page.check_visibility('Search', self.page.search_result_locator)
        app.models.signin.page.email_button.click()
        self.page.check_invisibility('Search', self.page.search_result_locator)
        app.models.signin.page.email_close_button.click()

    def user_follow(self):
        self.page.follow_button[0].click()
        self.page.check_invisibility('Subscription button', self.page.self_subscription_locator)
        self.page.people_results[0].click()
    
    def close_search(self):
        if self.page.is_mobile():
            self.page.close_search()
    
    def click_ticker(self, app):
        self.page.stocks_results[0].click()
        self.page.should_be_right_page('https://ng.tst.whotrades.net/$')

        if app.models.nav.page.is_mobile():
            app.models.nav.page.menu.click()

        app.models.nav.page.feed_link.click()
