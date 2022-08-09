import pytest
import allure

from ..utils import generate_valid_email


class TestEmailSignup:
    @allure.testcase('Limex. Регистрация через email')
    @allure.feature('Регистрация через email')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.manual
    def test_email_signup(self, app):
        with allure.step('Step 1. В шапке сайта нажать на Регистрация/Sign Up'):
            app.models.nav.click_signup_button()

        with allure.step('Step 2. Кликнуть по крестику закрытия'):
            app.models.signup.close_popup()

        with allure.step('Step 3. Нажать на кнопку Email'):
            app.models.signup.click_email_button()
        
        with allure.step('Step 4. Ввести новый email'):
            email = generate_valid_email()
            app.models.signup.input_new_email(email)

        with allure.step('Step 5. Кликнуть по крестику закрытия в попапе ввода кода/пароля'):
            app.models.signup.close_pin_popup()

        with allure.step('Step 6. Кликнуть Назад'):
            app.models.signup.confirm_back()

        with allure.step('Step 7. Кликнуть Отмена'):
            app.models.signup.confirm_cancel()

        with allure.step('Step 8. Завершение регистрации'):
            app.models.signup.complete_signup(email)
        
        with allure.step('Step 9. Нажать на кнопку Sign In/Войти'):
            app.models.signup.click_sign_in()
        
        with allure.step('Step 10. Нажать на кнопку Got It/Все понятно'):
            app.models.signup.click_got_it()
        
        with allure.step('Asserts. Проверить, что пользователь вошёл'):
            app.models.nav.check_signed_in()
