from .base_page import BasePage

from ..locators.base_locators import BaseLocators
from ..locators.signin_locators import SigninLocators


class SigninPage(BasePage):
    @property
    def popup_locator(self):
        return SigninLocators.SIGNIN_POPUP
    
    @property
    def cross_locator(self):
        return SigninLocators.CLOSE_BUTTON
    
    @property
    def close_button(self):
        return self.get_element(
            'Close button',
            SigninLocators.CLOSE_BUTTON
        )
    
    @property
    def email_button(self):
        return self.get_element(
            'Email button',
            SigninLocators.EMAIL_BUTTON
        )

    @property
    def email_field(self):
        return self.get_element(
            'Email field',
            SigninLocators.EMAIL_FIELD
        )

    @property
    def signup_button_locator(self):
        return SigninLocators.SIGNUP_BUTTON
    
    @property
    def pin_next_button(self):
        return self.get_element(
            'Pin next button',
            SigninLocators.PIN_NEXT_BUTTON
        )

    @property
    def next_button(self):
        return self.get_element(
            'Next button',
            SigninLocators.NEXT_BUTTON
        )

    @property
    def next_button_locator(self):
        return SigninLocators.NEXT_BUTTON
    
    @property
    def back_button_locator(self):
        return SigninLocators.BACK_BUTTON

    @property
    def pin_next_button_locator(self):
        return SigninLocators.PIN_NEXT_BUTTON
    
    @property
    def pin_cancel_button_locator(self):
        return SigninLocators.PIN_CANCEL_BUTTON
    
    @property
    def pin_close_button(self):
        return self.get_element(
            'Pin close button',
            SigninLocators.PIN_CLOSE_BUTTON
        )

    @property
    def hint_locator(self):
        return SigninLocators.HINT
    
    @property
    def confirmation_locator(self):
        return SigninLocators.CONFIRMATION
    
    @property
    def confirmation_quit_button(self):
        return self.get_element(
            'Pin close button',
            SigninLocators.CONFIRM_QUIT_BUTTON
        )
    
    @property
    def confirmation_quit_button_locator(self):
        return SigninLocators.CONFIRM_QUIT_BUTTON

    
    @property
    def confirmation_back_button(self):
        return self.get_element(
            'Confirm back button',
            SigninLocators.CONFIRM_BACK_BUTTON
        )
    
    @property
    def confirmation_back_button_locator(self):
        return SigninLocators.CONFIRM_BACK_BUTTON
    
    @property
    def pin_input(self):
        return self.get_element(
            'Pin input',
            SigninLocators.PIN_INPUT
        )

    def check_hint_text(self, email):
        hint = self.get_element('Pin hint', SigninLocators.HINT)

        self.compare_texts(hint.text, 'Мы отправили вам на email ' + email + ' одноразовый код подтверждения')

    def check_scroll(self):
        assert self.get_element(
            'Body',
            BaseLocators.BODY
        ).value_of_css_property('position') != 'fixed', 'Scroll is disabled'

    def check_options(self):
        options = [
            self.is_visibility_of_element(SigninLocators.SOCIAL_NETWORK_BUTTON),
            self.is_visibility_of_element(SigninLocators.BROKERAGE_BUTTON),
            self.is_visibility_of_element(SigninLocators.EMAIL_BUTTON),
            self.is_visibility_of_element(SigninLocators.SIGNUP_BUTTON),
            self.is_visibility_of_element(SigninLocators.APPLE_BUTTON),
            self.is_visibility_of_element(SigninLocators.GOOGLE_BUTTON),
        ]

        assert all(options),\
               'Not all options are visible'
    
    def check_active_email_field(self):
        element = self.get_element(
            'Email field label',
            SigninLocators.EMAIL_FIELD_LABEL
        )
        assert 'active' in element.get_attribute('class'),\
               'Email field is not active'
    
    def check_confirmation_text(self):
        got = self.get_element('', self.confirmation_locator).text
        self.compare_texts(got, 'Вы уверены, что хотите отменить вход?')
        self.compare_texts(got, 'Осталось пройти всего несколько простых шагов')
