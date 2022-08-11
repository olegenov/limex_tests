from .pages.nav_page import NavPage
from .pages.signup_page import SignupPage
from .pages.signin_page import SigninPage
from .pages.email_page import EmailPage
from .pages.main_page import MainPage
from .pages.search_page import SearchPage

from .models.nav_model import Nav
from .models.signup_model import Signup
from .models.signin_model import Signin
from .models.email_model import Email
from .models.main_model import Main
from .models.search_model import Search


class Models:
    def __init__(self, driver, base_url):
        self.nav = Nav(driver, NavPage(driver, base_url))
        self.main = Main(driver, MainPage(driver, base_url))
        self.signup = Signup(driver, SignupPage(driver, base_url))
        self.signin = Signin(driver, SigninPage(driver, base_url))
        self.email = Email(driver, EmailPage(driver, base_url))
        self.search = Search(driver, SearchPage(driver, base_url))
