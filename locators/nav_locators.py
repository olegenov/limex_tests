from selenium.webdriver.common.by import By


class NavLocators:
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'header button[kind="outline"]')
    SIGNUP_MENU_BUTTON = (By.XPATH, '//div[contains(@class, "MobileMenustyles")]//button[contains(@class, "autotest__menu__sign-up")]')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'header button[kind="outline"] ~ button')
    SIGNIN_MENU_BUTTON = (By.XPATH, '//div[contains(@class, "MobileMenustyles")]//button[contains(@class, "autotest__menu__sign-in")]')
    AVATAR = (By.XPATH, '//button[contains(@class, "UserDropdown")]')

    SEARCH_INPUT = (By.CSS_SELECTOR, 'header form input')
    SEARCH_INPUT_MOBILE = (By.XPATH, '//div[contains(@class, "Mobile")]//input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[kind="ghost-secondary"]')
    MAGNIFIER_ICON = (By.CSS_SELECTOR, 'header form svg')
    SEARCH_FIELD_PLACEHOLDER = (By.CSS_SELECTOR, 'input[placeholder="Бумаги, посты, люди, продукты..."]')

    MENU = (By.XPATH, '//span[contains(@class, "MobileMenu")]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.autotest__user-menu-logout')
    FEED_LINK = (By.CSS_SELECTOR, '.autotest__menu__feed')
    FEED_LINK_MOBILE = (By.XPATH, '//div[contains(@class, "MobileMenu")][3]//a')
