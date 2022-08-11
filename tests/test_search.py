import pytest
import allure


class TestSearch:
    @allure.testcase('Limex. Поиск поста')
    @allure.feature('Поиск поста')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_posts_search(self, app):
        with allure.step('Step 1. Пользователь русский. В поле поиска ввести слова из заголовка поста'):
            if app.is_mobile():
                app.models.nav.click_search_button()

            app.change_locale('ru')
            app.models.nav.input_search_request('Сбербанк обозначил')

        with allure.step('Step 2. Пользователь английский. В поле поиска ввести слова из заголовка поста'):
            app.change_locale('en')
            app.models.nav.input_search_request('Gold')
        
        with allure.step('Step 3. Кликнуть на пост'):
            app.models.search.click_post()
        
        with allure.step('Asserts. Пост соответствует поиску'):
            app.models.main.check_post_match('Gold')
