'''Тесты эндпоинта для создания курьеров.'''
import allure
import pytest

from data import Courier, CREATED
from helpers import code_and_body_are_expected, get_account_data


class TestCourierCreate:

    @allure.title('Успешное создание учётной записи курьера')
    def test_create_courier_account_success(self, courier_methods):
        '''Успешное создание учётной записи курьера.'''
        response, account = courier_methods.create_courier(get_account_data())
        _, account_id = courier_methods.login_courier(account)
        courier_methods.delete_courier(account_id)
        assert code_and_body_are_expected(response, *CREATED)

    @allure.title('Невозможно создать двух курьеров с одинаковым логином')
    def test_create_courier_duplicate_error(
        self, courier_methods, test_courier
    ):
        '''Невозможно создать двух курьеров с одинаковым логином.'''
        response, _ = courier_methods.create_courier(test_courier)
        assert code_and_body_are_expected(response, *Courier.DUPLICATE)

    @allure.title('Невозможно создать курьера без логина или пароля')
    @pytest.mark.parametrize(
        'account', [pytest.param(Courier.LOGIN_ONLY, id='login only'),
                    pytest.param(Courier.PASSWORD_ONLY, id='password only')]
    )
    def test_create_courier_missed_data_error(self, courier_methods, account):
        '''Невозможно создать курьера без логина или пароля.'''
        response, _ = courier_methods.create_courier(account)
        assert code_and_body_are_expected(
            response, *Courier.MISSED_DATA_CREATE
        )
