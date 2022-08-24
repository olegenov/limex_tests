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

    def change_locale(self, locale):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        self.driver.options = options
        self.driver.refresh()
    
    def is_mobile(self):
        return 'iPhone' in self.driver.execute_script('return navigator.userAgent',)
    
    def login(self, login):
        self.models.nav.click_login_button()
        self.models.signin.click_email_button()
        email = login + '@tst.whotrades.org'
        self.models.signin.input_new_email(email)
        self.models.signin.complete_signin(email)
        self.models.signin.click_sign_in()
        self.models.nav.check_signed_in()
    
    def logout(self):
        self.models.nav.page.avatar.click()
        self.models.nav.click_logout()
