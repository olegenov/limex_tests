from selenium.webdriver.common.keys import Keys

from .base_model import BaseModel

from ..pages.nav_page import NavPage
from ..pages.signup_page import SignupPage
from ..pages.email_page import EmailPage

from ..utils import generate_invalid_email


class Signup(BaseModel):
    def close_popup(self):
        self.page.close_button.click()
        self.page.check_invisibility('Popup', self.page.popup_locator)
        self.page.check_scroll()

    def click_email_button(self):
        self.page = NavPage(self.driver, self.driver.current_url)
        self.page.signup_button.click()
        self.page = SignupPage(self.driver, self.driver.current_url)
        self.page.email_button.click()
        self.page.check_active_email_field()
        self.page.check_visibility('Terms', self.page.terms_label_locator)
        self.page.check_visibility(
            'Terms Checkbox',
            self.page.terms_checkbox_locator
        )
        self.page.check_button_disabled(
            'Next button',
            self.page.next_button_locator
        )
        self.page.check_button_enabled(
            'Back button',
            self.page.back_button_locator
        )

    def input_new_email(self, email):
        self.page.email_field.clear()
        invalid_email = generate_invalid_email()
        self.page.email_field.send_keys(invalid_email)
        self.page.next_button.click()
        self.page.check_validation()
        self.page.next_button.click()
        self.page.email_field.clear()
        self.page.email_field.send_keys(Keys.COMMAND, "a")
        self.page.email_field.send_keys(Keys.CONTROL, "a")
        self.page.email_field.send_keys(Keys.DELETE)
        self.page.email_field.send_keys(email)
        self.page.next_button.click()
        self.page.check_button_disabled(
            'Signup button',
            self.page.pin_next_button_locator
        )
        self.page.check_button_enabled(
            'Signup Cancel',
            self.page.pin_cancel_button_locator
        )
    
    def close_pin_popup(self):
        self.page.pin_close_button.click()
        self.page.check_visibility(
            'Confirmation',
            self.page.confirmation_locator
        )
        self.page.check_confirmation_text()
        self.page.check_visibility(
            'Back button',
            self.page.confirmation_back_button_locator
        )
        self.page.check_visibility(
            'Quit button',
            self.page.confirmation_quit_button_locator
        )

    def confirm_back(self):
        self.page.confirmation_back_button.click()
        self.page.check_visibility(
            'Pin popup',
            self.page.pin_popup_locator
        )

    def confirm_cancel(self):
        self.page.pin_close_button.click()
        self.page.confirmation_quit_button.click()
        self.page.check_invisibility(
            'Signup popup',
            self.page.popup_locator
        )

    def complete_signup(self, email):
        self.go_to('https://mailtst.dev.whotrades.net/{}/'.format(email))
        self.page = EmailPage(self.driver, self.driver.current_url)
        pin = self.page.pin.text
        self.page.signup_button.click()
        self.page = SignupPage(self.driver, self.driver.current_url)
        got_pin = self.page.pin_input.get_attribute('value')
        self.page.compare_texts(got_pin, pin)
        self.page.check_invisibility(
            'Cancel button',
            self.page.pin_cancel_button_locator
        )

    def click_sign_in(self):
        self.page.pin_next_button.click()
        self.page.check_visibility(
            'Succes Popup',
            self.page.success_popup_locator
        )

    def click_got_it(self):
        self.page.check_visibility(
            'Succes Popup',
            self.page.success_popup_locator
        )
        self.page.got_it_button.click()
