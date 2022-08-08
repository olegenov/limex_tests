from .base_page import BasePage

from ..locators.base_locators import BaseLocators
from ..locators.signup_locators import SignupLocators

from ..utils import wait


class SignupPage(BasePage):
    @property
    def popup_locator(self):
        return SignupLocators.SIGNUP_POPUP
    
    @property
    def pin_popup_locator(self):
        return SignupLocators.PIN_POPUP
    
    @property
    def cross_locator(self):
        return SignupLocators.CLOSE_BUTTON
    
    @property
    def terms_label_locator(self):
        return SignupLocators.TERMS_LABEL
    
    @property
    def terms_checkbox_locator(self):
        return SignupLocators.TERMS_CHECKBOX

    @property
    def close_button(self):
        return self.get_element(
            'Close button',
            SignupLocators.CLOSE_BUTTON
        )
    
    @property
    def pin_close_button(self):
        return self.get_element(
            'Pin close button',
            SignupLocators.PIN_CLOSE_BUTTON
        )

    @property
    def email_button(self):
        return self.get_element(
            'Email button',
            SignupLocators.EMAIL_BUTTON
        )

    @property
    def email_field(self):
        return self.get_element(
            'Email field',
            SignupLocators.EMAIL_FIELD
        )

    @property
    def next_button(self):
        return self.get_element(
            'Next button',
            SignupLocators.NEXT_BUTTON
        )
    
    @property
    def next_button_locator(self):
        return SignupLocators.NEXT_BUTTON
    
    @property
    def back_button_locator(self):
        return SignupLocators.BACK_BUTTON
    
    @property
    def pin_next_button(self):
        return self.get_element(
            'Pin next button',
            SignupLocators.PIN_NEXT_BUTTON
        )

    @property
    def pin_next_button_locator(self):
        return SignupLocators.PIN_NEXT_BUTTON
    
    @property
    def pin_cancel_button_locator(self):
        return SignupLocators.PIN_CANCEL_BUTTON
    
    @property
    def confirmation_locator(self):
        return SignupLocators.CONFIRMATION
    
    @property
    def confirmation_quit_button(self):
        return self.get_element(
            'Pin close button',
            SignupLocators.CONFIRM_QUIT_BUTTON
        )
    
    @property
    def confirmation_quit_button_locator(self):
        return SignupLocators.CONFIRM_QUIT_BUTTON

    
    @property
    def confirmation_back_button(self):
        return self.get_element(
            'Confirm back button',
            SignupLocators.CONFIRM_BACK_BUTTON
        )
    
    @property
    def confirmation_back_button_locator(self):
        return SignupLocators.CONFIRM_BACK_BUTTON
    
    @property
    def pin_input(self):
        return self.get_element(
            'Pin input',
            SignupLocators.PIN_INPUT
        )
    
    @property
    def pin_back_button_locator(self):
        return SignupLocators.PIN_BACK_BUTTON
    
    @property
    def success_popup_locator(self):
        return SignupLocators.SUCCESS_POPUP

    @property
    def got_it_button(self):
        return self.get_element(
            'Got it button',
            SignupLocators.GOT_IT_BUTTON
        )
    
    @property
    def avatar_locator(self):
        return SignupLocators.AVATAR
    
    def check_scroll(self):
        assert self.get_element(
            'Body',
            BaseLocators.BODY
        ).value_of_css_property('position') != 'fixed', 'Scroll is disabled'

    def check_options(self):
        options = [
            self.is_visibility_of_element(SignupLocators.SOCIAL_NETWORK_BUTTON),
            self.is_visibility_of_element(SignupLocators.BROKERAGE_BUTTON),
            self.is_visibility_of_element(SignupLocators.EMAIL_BUTTON),
            self.is_visibility_of_element(SignupLocators.SIGNIN_BUTTON),
            self.is_visibility_of_element(SignupLocators.APPLE_BUTTON),
            self.is_visibility_of_element(SignupLocators.GOOGLE_BUTTON),
        ]

        assert all(options),\
               'Not all options are visible'
    
    def check_active_email_field(self):
        element = self.get_element(
            'Email field label',
            SignupLocators.EMAIL_FIELD_LABEL
        )
        assert 'active' in element.get_attribute('class'),\
               'Email field is not active'
    
    def check_terms_checkbox(self):
        element = self.get_element(
            'Terms checkbox',
            SignupLocators.TERMS_CHECKBOX
        )
        assert 'Checked' in element.get_attribute('class'),\
               'Checkbox is unactive'

    @wait()
    def check_validation(self):
        element = self.get_element(
            'Email field label',
            SignupLocators.EMAIL_FIELD_LABEL
        )
        assert 'error' in element.get_attribute('class'),\
               'Invalid email validated'
    
    def check_confirmation_text(self):
        got = self.get_element('', self.confirmation_locator).text
        self.compare_texts(got, 'Вы уверены, что хотите отменить регистрацию?')
        self.compare_texts(got, 'Осталось пройти всего несколько простых шагов')
