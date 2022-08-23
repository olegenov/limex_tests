import pytest
import allure


class TestNotification:
    @allure.testcase('Уведомление о лайке публикации (2.0)')
    @allure.feature('Уведомление о лайке публикации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_post_like_notification(self, app):
        with allure.step('Step 1. Пользователем 1 опубликовать запись с текстом минимум в 2 строки'):
            pass
        with allure.step('Step 2. Пользователем 2 лайкнуть запись от пользователя 1'):
            pass
        with allure.step('Asserts. Проверить, что в уведомлении текст публикации максимально может быть отображен в двух строках'):
            pass
