from selenium.webdriver.common.keys import Keys

from ..locators.search_locators import SearchLocators

from .base_page import BasePage
from .nav_page import NavPage


class SearchPage(BasePage):
    @property
    def search_locator(self):
        return SearchLocators.SEARCH_RESULTS
    
    @property
    def search_result_locator(self):
        return SearchLocators.SEARCH_RESULT
    
    @property
    def stocks_tab(self):
        return self.get_clickable_element(
            'Stocks search tab',
            self.stocks_tab_locator
        )
    
    @property
    def stocks_tab_locator(self):
        return SearchLocators.STOCKS_TAB

    @property
    def posts_tab(self):
        return self.get_clickable_element(
            'Posts search tab',
            self.posts_tab_locator
        )
    
    @property
    def posts_tab_locator(self):
        return SearchLocators.BLOGS_TAB
    
    @property
    def people_tab(self):
        return self.get_clickable_element(
            'People search tab',
            self.people_tab_locator
        )

    @property
    def people_tab_locator(self):
        return SearchLocators.PEOPLE_TAB
    
    @property
    def shop_tab(self):
        return self.get_clickable_element(
            'Shop search tab',
            self.shop_tab_locator
        )

    @property
    def shop_tab_locator(self):
        return SearchLocators.SHOP_TAB

    @property
    def post_results(self):
        return self.get_elements(
            'Post Results',
            SearchLocators.POSTS
        )
    
    @property
    def people_results(self):
        return self.get_elements(
            'People Results',
            SearchLocators.PEOPLE
        )

    @property
    def stocks_results(self):
        return self.get_elements(
            'Stocks Results',
            SearchLocators.STOCKS
        )
    
    @property
    def shop_results(self):
        return self.get_elements(
            'People Results',
            SearchLocators.SHOP
        )
    
    @property
    def close_button(self):
        return self.get_clickable_element(
            'Search close button',
            SearchLocators.CLOSE_BUTTON
        )
    
    @property
    def verified_locator(self):
        return SearchLocators.VERIFIED
    
    @property
    def self_subscription_locator(self):
        return SearchLocators.SELF_SUBSCRIPTION_BUTTON
    
    @property
    def follow_button(self):
        return self.get_elements(
            'Follow buttons',
            SearchLocators.FOLLOW_BUTTON
        )

    def check_no_results(self, request):
        results = self.get_element(
            'Results',
            SearchLocators.SEARCH_RESULTS
        )
        expected = 'По вашему запросу ' + request + ' ничего не найдено.'

        self.compare_texts(results.text, expected)
    
    def check_people_results(self, request):
        results = self.people_results
        expected = request.split(' ')

        for exp in expected:
            for result in results:
                self.compare_texts(result.text.lower(), exp.lower())
    
    def check_shop_results(self, request):
        results = self.shop_results
    
        for result in results:
            self.compare_texts(result.text.lower(), request.lower())

    def check_tabs(self):
        self.check_visibility(
            'Stocks tab', self.stocks_tab_locator
        )
        self.check_visibility(
            'People tab', self.people_tab_locator
        )
        self.check_visibility(
            'Posts tab', self.posts_tab_locator
        )
        self.check_visibility(
            'Shop tab', self.shop_tab_locator
        )
    
    def switch_tab(self, tab):
        if tab == 'stocks':
            self.stocks_tab.click()
        elif tab == 'people':
            self.people_tab.click()
        elif tab == 'posts':
            self.posts_tab.click()
        elif tab == 'shop':
            self.shop_tab.click()

    def close_search(self):
        page = NavPage(self.driver, self.driver.current_url)

        if self.is_visibility_of_element(page.search_input_locator, 1):
            self.close_button.click()
