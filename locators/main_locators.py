from selenium.webdriver.common.by import By


class MainLocators:
    POST = (By.CSS_SELECTOR, '.autotest__feed-item')
    CLOSE_HINT = (By.CSS_SELECTOR, '.autotest__reactour__close-btn')
    POST_TEXTAREA = (By.CSS_SELECTOR, '.autotest__feed_status__container .ce-paragraph')
    ADD_POST = (By.CSS_SELECTOR, '.autotest__add-status')
    PUBLISH_BUTTON = (By.CSS_SELECTOR, '.autotest__add-feed-status__submit')