from ..locators.search_locators import SearchLocators

from .base_page import BasePage


class SearchPage(BasePage):
    @property
    def search_locator(self):
        return SearchLocators.SEARCH_RESULTS
    
    @property
    def search_result_locator(self):
        return SearchLocators.SEARCH_RESULT

    @property
    def posts_tab(self):
        return self.get_clickable_element(
            'Posts search tab',
            SearchLocators.BLOGS_TAB
        )
    
    @property
    def people_tab(self):
        return self.get_clickable_element(
            'People search tab',
            SearchLocators.PEOPLE_TAB
        )

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
