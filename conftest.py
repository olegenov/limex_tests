from re import S
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .apps import Application



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
        options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X)' +
            ' AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        )

    app = Application(webdriver.Chrome(options=options), base_url)
    app.driver.set_window_rect

    yield app

    print("\nQuiting browser..")
    app.driver.quit()
