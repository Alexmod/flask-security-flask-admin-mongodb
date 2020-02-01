# -*- coding: utf-8 -*-
import unittest
import warnings

from flask import url_for


def warn(*args, **kwargs):
    pass


warnings.warn = warn


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(extra_config_settings={
            'TESTING': True,
            'WTF_CSRF_ENABLED': False})
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    # ---------------------------------------------------------------------
    #  Тесты публичной части сайта
    # ---------------------------------------------------------------------

    def test_home_page(self):  # Тест главной страницы
        response = self.client.get(url_for('public.home_page'),
                                   content_type='html/text')
        self.assertEqual(response.status_code, 200)
        assert 'Войти' in response.data.decode('utf-8')

    # ---------------------------------------------------------------------
    #  Тесты пользовательской части сайта
    # ---------------------------------------------------------------------

    def login(self, username, password):
        r = self.client.post(url_for('security.login'), data=dict(
            email=username,
            password=password
        ), follow_redirects=True)
        return r

    def logout(self):
        return self.client.get(url_for('security.logout'),
                               follow_redirects=True)

    def test_login_logout(self):  # Тесты входа, выхода, неверн.: емайл, пароля
        rv = self.login('user@example.com', 'Password1')
        assert 'Профиль' in rv.data.decode('utf-8')
        rv = self.logout()

        rv = self.login('user@example.com', 'wrong_password')
        assert 'Неверный пароль' in rv.data.decode('utf-8')
        rv = self.login('wrong@email.com', '123456')
        assert 'Данный пользователь не найден' in rv.data.decode('utf-8')


if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from app import create_app
    result = unittest.main()
