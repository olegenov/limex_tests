from selenium.webdriver.common.keys import Keys

from .base_model import BaseModel

from ..pages.nav_page import NavPage
from ..pages.signin_page import SigninPage
from ..pages.email_page import EmailPage

from ..utils import generate_invalid_email


class Signin(BaseModel):
    def close_popup(self):
        self.page.close_button.click()
        self.page.check_invisibility('Popup', self.page.popup_locator)
        self.page.check_scroll()

    def click_email_button(self):
        self.page.email_button.click()
        self.page.check_active_email_field()
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
        self.page.email_field.send_keys(email)
        self.page.next_button.click()
        self.page.check_visibility(
            'Hint',
            self.page.hint_locator
        )
        self.page.check_hint_text(email)
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

    def complete_signin(self, email):
        self.go_to('https://mailtst.dev.whotrades.net/{}/'.format(email))

        page = EmailPage(self.driver, self.driver.current_url)
        pin = page.pin.text
        page.signin_button.click()

        got_pin = self.page.pin_input.get_attribute('value')
        self.page.compare_texts(got_pin, pin)
        self.page.check_invisibility(
            'Cancel button',
            self.page.pin_cancel_button_locator
        )

    def click_sign_in(self):
        self.page.pin_next_button.click()
