import datetime as dt

from .base_model import BaseModel


class Profile(BaseModel):
    def check_following(self):
        self.page.check_visibility('Subscribed', self.page.subscribed_locator)
        self.page.compare_texts(self.page.subscribe_button.text, 'Вы подписаны')
        self.page.subscribe_button.click()
        self.page.check_visibility('Not subscribed', self.page.not_subscribed_locator)
    
    def leave_comment(self, app, request):
        now = dt.datetime.now()
        text = now.strftime('%Y-%m-%d %H:%M:%S Comment notification test comment')

        app.models.nav.input_people_search_request(app, request)
        app.models.search.page.people_results[0].click()

        self.page.comment_button.click()
        self.page.comment_textarea.click()
        self.page.comment_textarea.send_keys(text)
        self.page.leave_comment_button.click()