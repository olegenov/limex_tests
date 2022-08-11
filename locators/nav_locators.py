from selenium.webdriver.common.by import By


class NavLocators:
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'header button[kind="outline"]')
    SIGNUP_MENU_BUTTON = (By.XPATH, '//div[contains(@class, "MobileMenustyles")]//button[contains(@class, "autotest__menu__sign-up")]')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'header button[kind="outline"] ~ button')
    SIGNIN_MENU_BUTTON = (By.XPATH, '//div[contains(@class, "MobileMenustyles")]//button[contains(@class, "autotest__menu__sign-in")]')
    AVATAR = (By.CSS_SELECTOR, '.autotest__profile_header_avatar')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'header form input')
    SEARCH_INPUT_MOBILE = (By.XPATH, '//div[contains(@class, "Mobile")]//input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[kind="ghost-secondary"]')
    MENU = (By.XPATH, '//span[contains(@class, "MobileMenu")]')
