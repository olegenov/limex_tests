from selenium.webdriver.common.by import By


class SearchLocators:
    BLOGS_TAB = (By.CSS_SELECTOR, '.autotest__search-tab-blogposts')
    PEOPLE_TAB = (By.CSS_SELECTOR, '.autotest__search-tab-users')
    STOCKS_TAB = (By.CSS_SELECTOR, '.autotest__search-tab-instruments')
    SHOP_TAB = (By.CSS_SELECTOR, '.autotest__search-tab-market')


    POSTS = (By.CSS_SELECTOR, '.autotest__search-blogposts-result a')
    PEOPLE = (By.CSS_SELECTOR, '.autotest__search-users-result a')
    STOCKS = (By.CSS_SELECTOR, '.autotest__search-instruments-result a')
    SHOP = (By.CSS_SELECTOR, '.autotest__search-market-result a')

    SEARCH_RESULTS = (By.XPATH, '//li[contains(text(), "По вашему запросу")]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '.autotest__search-result')

    VERIFIED = (By.CSS_SELECTOR, '.verified-icon-link')
    SELF_SUBSCRIPTION_BUTTON = (By.XPATH, '//div[contains(@class, "autotest__search-users-result")]//a[1]//div[3]')
    FOLLOW_BUTTON = (By.CSS_SELECTOR, '.autotest__search-users-result a svg')

    CLOSE_BUTTON = (By.XPATH, '//div[contains(@class, "Mobile")]/div[2]')