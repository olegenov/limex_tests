from .base_model import BaseModel


class Profile(BaseModel):
    def check_following(self):
        self.page.check_visibility('Subscribed', self.page.subscribed_locator)
        self.page.compare_texts(self.page.subscribe_button.text, 'Вы подписаны')
        self.page.subscribe_button.click()
        self.page.check_visibility('Not subscribed', self.page.not_subscribed_locator)