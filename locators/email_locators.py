from selenium.webdriver.common.by import By


class EmailLocators:
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '.autotest__mail-login-button')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, '.autotest__mail-submit-button')
    PIN = (By.CSS_SELECTOR, 'strong')
