from selenium.webdriver.common.by import By


class SignupLocators:
    SIGNUP_POPUP = (By.CSS_SELECTOR, '.autotest__sign-up-screen')

    SOCIAL_NETWORK_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-social-networks-button')
    BROKERAGE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-brokerage-button')
    EMAIL_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-email-button')

    CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-up-screen svg')
    SIGNIN_BUTTON = (By.XPATH, '//p[text()="У вас уже есть аккаунт? "]/span')

    APPLE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-apple-button')
    GOOGLE_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-google-button')

    EMAIL_FIELD = (By.CSS_SELECTOR, '.autotest__sign-up-email-text-field input')
    EMAIL_FIELD_LABEL = (By.CSS_SELECTOR, '.autotest__sign-up-email-text-field label')

    NEXT_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-email-next-button')
    BACK_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-email-cancel-button')

    CONFIRMATION = (By.CSS_SELECTOR, '.autotest__confirmation-screen')
    CONFIRM_BACK_BUTTON = (By.CSS_SELECTOR, '.autotest__confirmation-next-button')
    CONFIRM_QUIT_BUTTON = (By.CSS_SELECTOR, '.autotest__confirmation-cancel-button')

    TERMS_LABEL = (By.CSS_SELECTOR, 'label.placementRight')
    TERMS_CHECKBOX = (By.CSS_SELECTOR, 'span.placementRight svg')

    PIN_POPUP = (By.CSS_SELECTOR, 'div.autotest__sign-up-pin-screen')
    PIN_INPUT = (By.CSS_SELECTOR, 'div.autotest__sign-up-pin-screen input')
    PIN_NEXT_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-pin-next-button')
    PIN_CANCEL_BUTTON = (By.CSS_SELECTOR, '.autotest__sign-up-pin-cancel-button')
    PIN_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.autotest__sign-up-pin-screen svg')

    SUCCESS_POPUP = (By.CSS_SELECTOR, '.autotest__success-screen')
    GOT_IT_BUTTON = (By.CSS_SELECTOR, '.autotest__success-cancel-button')

    AVATAR = (By.CSS_SELECTOR, '.autotest__profile_header_avatar')
