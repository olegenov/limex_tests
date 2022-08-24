from .base_page import BasePage
from ..locators.main_locators import MainLocators


class MainPage(BasePage):
    @property
    def post(self):
        return self.get_element(
            'Post',
            MainLocators.POST
        )

    @property
    def hint(self):
        return self.get_element(
            'Hint',
            MainLocators.CLOSE_HINT,
        )

    @property
    def post_textarea(self):
        return self.get_element(
            'Post Textarea',
            MainLocators.POST_TEXTAREA
        )
    
    @property
    def add_post(self):
        return self.get_element(
            'Add post',
            MainLocators.ADD_POST
        )
    
    @property
    def publish_button(self):
        return self.get_element(
            'Publish button',
            MainLocators.PUBLISH_BUTTON
        )
