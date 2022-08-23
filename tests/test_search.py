import pytest
import allure


class TestSearch:
    @allure.testcase('Поиск поста (8.0)')
    @allure.feature('Поиск поста')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_posts_search(self, app):
        with allure.step('Step 1. Гостем в поле поиска ввести слова из заголовка поста'):
            app.models.nav.input_post_search_request(app, 'Сбербанк обозначил')

        with allure.step('Step 2. Кликнуть на первый пост в выдаче'):
            app.models.search.click_post()
        
        with allure.step('Asserts. Проверить, что открытый пост содержит текст из поискового запроса'):
            app.models.main.check_post_match('Сбербанк обозначил')

    @allure.testcase('Поиск людей (9.0)')
    @allure.feature('Поиск людей')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_people_search(self, app):
        with allure.step('Setup. Авторизация'):
            app.login()

        with allure.step('Step 1. Пользователем открыть поиск на вкладке "Люди" и ввести существующее имя пользователя'):
            name = 'Дмитрий'
            app.models.nav.input_people_search_request(app, name)
        
        with allure.step('Step 2. Кликнуть на первое имя пользователя из списка'):
            app.models.search.click_name(app, name)
        
        with allure.step('Step 3. Ввести Фамилию пользователя'):
            surname = 'Иванов'
            app.models.nav.input_people_search_request(app, surname)
        
        with allure.step('Step 4. Ввести Имя и Фамилию пользователя'):
            app.models.nav.input_people_search_request(app, f'{name} {surname}')
        
        with allure.step('Step 5. Ввести Фамилию и имя пользователя в обратном порядке'):
            app.models.nav.input_people_search_request(app, f'{surname} {name}')
        
        with allure.step('Step 6. Пользователем ввести собственное имя профиля'):
            self_username = 'aboba'
            app.models.nav.input_self_search_request(app, self_username)

        with allure.step('Step 7. Пользователем найти пользователя и кликнуть на иконку подписки'):
            name, surname = 'Tatyana', 'Kalinnikova'
            app.models.nav.input_people_search_request(app, f'{name} {surname}')
            app.models.search.user_follow()
        
        with allure.step('Asserts. Пользователь подписан на пользователя'):
            app.models.profile.check_following()
        
        with allure.step('Teardown. Выход из аккаунта'):
            app.logout()

    @allure.testcase('Поиск. Внешний вид')
    @allure.feature('Поиск. Внешний вид')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_search_view(self, app):
        with allure.step('Step 1. Гостем/Пользователем открыть страницу ленты'):
            app.models.nav.check_components()
        
        with allure.step('Step 1. Кликнуть в любое место поле Поиска'):
            app.models.nav.check_clickable_search()
        
        with allure.step('Step 3. Ввести название тикера'):
            app.models.nav.input_search_request(app, 'Google')

        with allure.step('Step 4. Кликнуть на название любого тикера'):
            app.models.search.click_ticker(app)

        with allure.step('Step 5. Переключиться на "Люди"'):
            app.models.nav.input_people_search_request(app, 'Дмитрий')
        
        with allure.step('Step 6. Переключиться на "Посты"'):
            app.models.nav.input_post_search_request(app, 'Сбербанк обозначил')
        
        with allure.step('Step 7. Переключиться на "Магазин"'):
            app.models.nav.input_shop_search_request(app, 'Research')
        
        with allure.step('Asserts. Проверить все табы на отсут. результат'):
            app.models.nav.find_without_results(app, 'Оцлоуимжцоуижсло')
