from selenium.webdriver.common.by import By


class ProfileLocators:
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '.autotest__profile-page__header-user-subscribe-button')
    NOT_SUBSCRIBED = (By.CSS_SELECTOR, '.autotest__profile-page__header-user-subscribe-button-not-subscribed')
    SUBSCRIBED = (By.CSS_SELECTOR, '.autotest__profile-page__header-user-subscribe-button-subscribed')
    NAME = (By.CSS_SELECTOR, '.adm__post-author')
    COMMENT_BUTTON = (By.XPATH, '//div[contains(@class, "adm__post-activity")]//button[2]')
    COMMENT_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Комментировать..."]')
    LEAVE_COMMENT_BUTTON = (By.XPATH, '//div[contains(@class, "ActionsButtonsGroup")]//button[2]')
