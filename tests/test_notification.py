import pytest
import allure


class TestNotification:
    @allure.testcase('Уведомление о комментарии в своей публикации (2.0)')
    @allure.feature('Уведомление о комментарии в своей публикации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regress
    def test_self_post_comment_notification(self, app):
        user1 = 'aboba'
        user2 = 'abober'

        with allure.step(f'Step 1. Пользователем {user1} опубликовать пост'):
            app.login(user1)
            app.models.main.publish_post()
            app.logout()

        with allure.step(f'Step 2. Пользователем {user2} оставить комментарий под постом пользователя 1'):
            app.login(user2)
            app.models.profile.leave_comment(app, user1)
            app.logout()

        with allure.step(f'Step 3. Пользователем {user1} открыть центр уведомлений'):
            pass
        with allure.step('Step 4. Кликнуть на уведомление'):
            pass
        with allure.step('Asserts. Открыт нужный пост в профиле'):
            pass