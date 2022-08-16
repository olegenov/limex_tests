from selenium.webdriver.common.by import By


class SigninLocators:
    SIGNIN_POPUP = (By.CSS_SELECTOR, '.autotest__sign-in-screen')

    SOCIAL_NETWORK_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-social-networks-button')
    BROKERAGE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-brokerage-button')
    EMAIL_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-email-button')

    CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-in-screen svg')
    SIGNUP_BUTTON = (By.XPATH, '//p[text()="У вас еще нет аккаунта? "]/span')

    APPLE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-apple-button')
    GOOGLE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-google-button')

    EMAIL_FIELD = (By.CSS_SELECTOR, '.autotest__sign-in-email-text-field input')
    EMAIL_FIELD_LABEL = (By.CSS_SELECTOR, '.autotest__sign-in-email-text-field label')
    EMAIL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-in-email-screen svg')

    NEXT_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-email-next-button')
    BACK_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-email-cancel-button')

    CONFIRMATION = (By.CSS_SELECTOR, '.autotest__confirmation-screen')
    CONFIRM_BACK_BUTTON = (By.CSS_SELECTOR, '.autotest__confirmation-next-button')
    CONFIRM_QUIT_BUTTON = (By.CSS_SELECTOR, '.autotest__confirmation-cancel-button')

    HINT = (By.CSS_SELECTOR, '.autotest__sign-in-pin-notification')

    PIN_POPUP = (By.CSS_SELECTOR, 'div.autotest__sign-in-pin-screen')
    PIN_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-in-pin-screen svg')
    PIN_INPUT = (By.CSS_SELECTOR, 'div.autotest__sign-in-pin-screen input')
    PIN_NEXT_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-pin-next-button')
    PIN_CANCEL_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-in-pin-cancel-button')
    PIN_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-in-pin-screen svg')
