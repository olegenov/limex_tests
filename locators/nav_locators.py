from selenium.webdriver.common.by import By


class NavLocators:
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'header button[kind="outline"]')
    CLOSE_HINT = (By.CSS_SELECTOR, '.autotest__reactour__close-btn')
