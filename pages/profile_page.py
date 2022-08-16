from .base_page import BasePage

from ..locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):
    @property
    def subscribed_locator(self):
        return ProfileLocators.SUBSCRIBED
    
    @property
    def not_subscribed_locator(self):
        return ProfileLocators.NOT_SUBSCRIBED
    
    @property
    def subscribe_button(self):
        return self.get_clickable_element(
            'Subscribe button',
            ProfileLocators.SUBSCRIBE_BUTTON
        )

    @property
    def name(self):
        return self.get_element(
            'Name',
            ProfileLocators.NAME
        )
