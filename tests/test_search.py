import pytest
import allure


class TestSearch:
    @allure.testcase('Limex. Поиск поста')
    @allure.feature('Поиск поста')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_posts_search(self, app):
        with allure.step('Step 1. Пользователь русский. В поле поиска ввести слова из заголовка поста'):
            app.change_locale('ru')
            if app.is_mobile():
                app.models.nav.click_search_button()
            app.models.nav.input_post_search_request('Сбербанк обозначил')

        with allure.step('Step 2. Пользователь английский. В поле поиска ввести слова из заголовка поста'):
            app.change_locale('en')
            if app.is_mobile():
                app.models.nav.click_search_button()
            app.models.nav.input_post_search_request('Gold')
        
        with allure.step('Step 3. Кликнуть на пост'):
            app.models.search.click_post()
        
        with allure.step('Asserts. Пост соответствует поиску'):
            app.models.main.check_post_match('Gold')

    @allure.testcase('Limex. Поиск людей')
    @allure.feature('Поиск людей')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_people_search(self, app):
        with allure.step('Step 1. В поле поиска ввести Имя пользователя'):
            if app.is_mobile():
                app.models.nav.click_search_button()
            
            app.models.nav.input_stocks_search_request('Дмитрий')
        
        with allure.step('Step 2. В поле поиска ввести Имя пользователя'):
            app.models.nav.input_people_search_request('Дмитрий')
        
        with allure.step('Step 3. Кликнуть на имя пользователя из списка'):
            app.models.search.click_name('Дмитрий')
        
        with allure.step('Step 4. Ввести Фамилию пользователя'):
            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.input_people_search_request('Кузьменко')
        
        with allure.step('Step 5. Ввести Имя и Фамилию пользователя'):
            app.models.nav.input_people_search_request('Tatyana Kalinnikova')
            app.models.nav.input_people_search_request('Kalinnikova Tatyana')

            if app.is_mobile():
                app.models.search.close_search()
        
        with allure.step('Step 6. Пользователем ввести собственное имя профиля'):
            app.login()

            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.input_self_search_request('aboba')

            if app.is_mobile():
                app.models.search.close_search()

            app.logout()

        with allure.step('Step 7. Гостем кликнуть на иконку подписки на пользователя'):
            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.input_people_search_request('Tatyana Kalinnikova')
            app.models.search.guest_follow()

        with allure.step('Step 8. Пользователем кликнуть на иконку подписки на пользователя'):
            app.login()

            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.input_people_search_request('Tatyana Kalinnikova')
            app.models.search.user_follow()
        
        with allure.step('Asserts. Пользователь подписан на пользователя'):
            app.models.profile.check_following()
            app.logout()
        
    @allure.testcase('Limex. Поиск. Внешний вид')
    @allure.feature('Поиск. Внешний вид')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_people_search(self, app):
        with allure.step('Step 1. Гостем/Пользователем открыть страницу ленты'):
            app.models.nav.check_components()
        
        with allure.step('Step 1. Кликнуть в любое место поле Поиска'):
            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.check_clickable_search()
        
        with allure.step('Step 3. Ввести название тикера'):
            app.models.nav.input_search_request('Google')

        with allure.step('Step 4. Кликнуть на название любого тикера'):
            app.models.search.click_ticker()
        '''
        with allure.step('Step 5. Гостем кликнуть по звездочке справа от любого тикера'):
            app.models.search.guest_click_ticker_star()
        
        with allure.step('Step 6. Пользователем кликнуть по иконке звездочке справа от любого тикера'):
            app.login()
            app.models.search.user_click_ticker_star()
        
        with allure.step('Step 7. Проверить отображение тикера в вотчлисте'):
            app.models.main.check_watchlist()
        
        with allure.step('Step 8. В поиск вновь ввести тот же тикер'):
            app.models.search.input_starred_search_request('Google')

        with allure.step('Step 9. Кликнуть на название любого тикера иным образом'):
            app.models.search.hot_click_ticker()
        '''
        with allure.step('Step 10. Переключиться на "Люди"'):
            if app.is_mobile():
                app.models.nav.click_search_button()

            app.models.nav.input_people_search_request('Дмитрий')
        
        with allure.step('Step 11. Переключиться на "Посты"'):
            app.models.nav.input_post_search_request('Сбербанк обозначил')
        
        with allure.step('Step 12. Переключиться на "Магазин"'):
            app.models.nav.input_shop_search_request('Research')
        
        with allure.step('Asserts. Проверить все табы на отсут. результат'):
            app.models.nav.find_without_results('Оцлоуимжцоуижсло')
