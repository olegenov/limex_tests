from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ..locators.base_locators import BaseLocators


class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url

    def should_be_right_page(self, url):
        assert url in self.driver.current_url, f'Incorrect url\n{url} expected, {self.driver.current_url} got'

    def check_button_enabled(self, button, locator):
        assert self.is_clickable_element(locator), \
               f'{button} is unactive'
    
    def check_button_disabled(self, button, locator):
        assert not self.is_clickable_element(locator), \
               f'{button} is active'
    
    def check_visibility(self, element, locator):
        assert self.is_visibility_of_element(locator),\
               f'{element} is not visible'
    
    def check_invisibility(self, element, locator):
        assert self.is_invisibility_of_element(locator),\
               f'{element} is visible'

    def compare_texts(self, got, expected):
        assert expected in got, 'Wrong text\n'\
               f'{expected} exptected, {got} got'

    def get_element(self, element, selector, wait=5):
        if self.is_visibility_of_element(selector, wait):
            return self.driver.find_element(*selector)
        else:
            raise TimeoutError(f'{element} is not found')
        
    def get_clickable_element(self, element, selector, wait=5):
        if self.is_clickable_element(selector, wait):
            return self.driver.find_element(*selector)
        else:
            raise TimeoutError(f'{element} is not found')

    def get_elements(self, element, selector):
        try: 
            return self.driver.find_elements(*selector)
        except:
            raise f'{element} are not found'
    
    def is_visibility_of_element(self, selector, wait=5):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            return False
        
        return True
    
    def is_invisibility_of_element(self, selector, wait=5):
        try:
            WebDriverWait(self.driver, wait).until_not(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            return False
        
        return True
    
    def is_clickable_element(self, selector, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            return False
        
        return True

    def is_mobile(self):
        return 'iPhone' in self.driver.execute_script('return navigator.userAgent',)