from ..locators.search_locators import SearchLocators

from .base_page import BasePage


class SearchPage(BasePage):
    @property
    def posts_tab(self):
        return self.get_element(
            'Posts search tab',
            SearchLocators.BLOGS_TAB
        )

    @property
    def results(self):
        return self.get_elements(
            'Results',
            SearchLocators.POSTS
        )