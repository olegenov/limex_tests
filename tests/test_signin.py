import pytest
import allure


class TestEmailSignin:
    @allure.testcase('Limex/Авторизация, регистрация/авторизация')
    @allure.feature('Авторизация, регистрация/авторизация')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_email_signin(self, app):
        with allure.step('Step 1. В шапке сайта нажать на Вход/ Sign In'):
            app.models.nav.click_login_button()

        with allure.step('Step 2. Кликнуть по крестику закрытия'):
            app.models.signin.close_popup()

        with allure.step('Step 3. Нажать на кнопку Email'):
            app.models.signin.click_email_button()
        
        with allure.step('Step 4. Ввести новый email'):
            email = 'aboba@tst.whotrades.org'
            app.models.signin.input_new_email(email)

        with allure.step('Step 5. Кликнуть по крестику закрытия в попапе ввода кода/пароля'):
            app.models.signin.close_pin_popup()

        with allure.step('Step 6. Завершение авторизации'):
            app.models.signin.complete_signin(email)
        
        with allure.step('Step 7. Нажать на кнопку Sign In/Войти'):
            app.models.signin.click_sign_in()
