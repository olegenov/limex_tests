from selenium.webdriver.common.by import By


class SearchLocators:
    BLOGS_TAB = (By.CSS_SELECTOR, '.autotest__search-tab-blogposts')
    POSTS = (By.CSS_SELECTOR, '.autotest__search-blogposts-result a')