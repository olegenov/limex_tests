from xml.sax.handler import property_declaration_handler
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

    @property
    def comment_button(self):
        return self.get_element(
            'Comment button',
            ProfileLocators.COMMENT_BUTTON
        )
    
    @property
    def comment_textarea(self):
        return self.get_element(
            'Comment textarea',
            ProfileLocators.COMMENT_TEXTAREA
        )

    @property
    def leave_comment_button(self):
        return self.get_element(
            'Leave comment button',
            ProfileLocators.LEAVE_COMMENT_BUTTON
        )
