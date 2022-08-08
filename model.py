from .pages.nav_page import NavPage
from .pages.signup_page import SignupPage
from .pages.email_page import EmailPage

from .models.nav_model import Nav
from .models.signup_model import Signup
from .models.email_model import Email


class Models:
    def __init__(self, driver, base_url):
        self.nav = Nav(driver, NavPage(driver, base_url))
        self.signup = Signup(driver, SignupPage(driver, base_url))
        self.email = Email(driver, EmailPage(driver, base_url))
