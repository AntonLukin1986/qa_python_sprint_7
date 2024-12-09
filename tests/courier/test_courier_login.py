'''Тесты эндпоинта для авторизации курьеров.'''
import allure
import pytest

from data import Courier
from helpers import code_and_body_are_expected, code_expected_and_data_in_body


class TestCourierLogin:

    @allure.title('Успешная авторизация курьера')
    def test_courier_login_success(self, courier_methods, test_courier):
        '''Успешная авторизация курьера.'''
        response, _ = courier_methods.login_courier(test_courier)
        assert code_expected_and_data_in_body(response, *Courier.LOGGED_IN)

    @allure.title('Невозможно авторизоваться без логина или пароля')
    @pytest.mark.parametrize(
        'account', [pytest.param(Courier.NO_PASSWORD, id='no password'),
                    pytest.param(Courier.PASSWORD_ONLY, id='password only')]
    )
    def test_courier_login_missed_login_or_password_error(
        self, courier_methods, account
    ):
        '''Невозможно авторизоваться без логина или пароля.'''
        response, _ = courier_methods.login_courier(account)
        assert code_and_body_are_expected(response, *Courier.MISSED_DATA_LOGIN)

    @allure.title('Ошибка авторизации с несуществующей парой логин-пароль')
    def test_courier_login_wrong_account_data_error(self, courier_methods):
        '''Ошибка авторизации с несуществующей парой логин-пароль.'''
        response, _ = courier_methods.login_courier(Courier.WRONG_ACCOUNT)
        assert code_and_body_are_expected(response, *Courier.NO_ACCOUNT)
