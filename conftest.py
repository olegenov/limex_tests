from re import S
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .apps import Application
from .pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption("--browser", default='desktop', action='store')


@pytest.fixture(scope="function")
def app(request):
    print("\nRunning app..")
    base_url = 'https://ng.tst.whotrades.net/'
    options = Options()
    options.add_argument('--lang=ru')
    browser = request.config.getoption('browser')
    
    if browser == 'mobile':
        mobile_emulation = {
            'deviceMetrics': {'width': 390, 'height': 844, 'pixelRatio': 3},
            'userAgent': '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.71 Mobile/15E148 Safari/604.1'
        }
        options.add_experimental_option('mobileEmulation', mobile_emulation)

    app = Application(webdriver.Chrome(options=options), base_url)

    if browser != 'mobile':
        app.models.main.close_hint()

    yield app

    print("\nQuiting browser..")
    app.driver.quit()
