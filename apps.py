from selenium.webdriver.chrome.options import Options

from .model import Models


class Application(object):
    def __init__(self, driver, base_url, token=None, \
             angara_token=None, txauth_token=None):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.models = Models(driver, base_url)

        self.driver.get(base_url)

    def go_to(self, url):
        self.driver.get(url)
