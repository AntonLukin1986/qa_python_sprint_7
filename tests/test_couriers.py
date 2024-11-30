'''Тесты эндпоинтов для создания, удаления и авторизации курьеров.'''
import pytest
import requests

from data import (
    CourierCreate as CC, CourierDelete as CD, CourierLogin as CL,
    CREATED, NOT_FOUND, OK_TRUE, WRONG_ID
)
from helpers import (
    code_and_body_are_correct, delete_account, get_account_data
)


class TestCourier:

    def request(self, method, url, data=None):
        '''Совершение действия под аккаунтом курьера.'''
        return getattr(requests, method)(url=url, data=data)

    def test_create_courier_account_success(self):
        '''Успешное создание учётной записи курьера.'''
        account = get_account_data()
        response = self.request(method='post', url=CC.API, data=account)
        assert code_and_body_are_correct(response, CREATED)                 # в такой реализации убрать везде распаковку
        delete_account(account)

    def test_create_courier_duplicate_error(self, test_courier):
        '''Невозможно создать двух курьеров с одинаковым логином.'''
        response = self.request(
            method='post', url=CC.API, data=test_courier
        )
        assert code_and_body_are_correct(response, **CC.DUPLICATE)

    @pytest.mark.parametrize(
        'account', [pytest.param(CC.LOGIN_ONLY, id='login only'),
                    pytest.param(CC.PASSWORD_ONLY, id='password only')]
    )
    def test_create_courier_missed_data_error(self, account):
        '''Невозможно создать курьера без логина или пароля.'''
        response = self.request(
            method='post', url=CC.API, data=account
        )
        assert code_and_body_are_correct(response, **CC.MISSED_DATA)

    def test_courier_login_success(self, test_courier):
        '''Успешная авторизация курьера.'''
        response = self.request(
            method='post', url=CL.API, data=test_courier
        )
        CL.LOGGED_IN['body']['id'] = response.json().get('id')
        assert code_and_body_are_correct(response, **CL.LOGGED_IN)

    @pytest.mark.parametrize(
        'account', [pytest.param(CL.NO_PASSWORD, id='no password'),
                    pytest.param(CC.PASSWORD_ONLY, id='password only')]
    )
    def test_courier_login_missed_data_error(self, account):
        '''Невозможно авторизоваться без логина или пароля.'''
        response = self.request(
            method='post', url=CL.API, data=account
        )
        assert code_and_body_are_correct(response, **CL.MISSED_DATA)

    def test_courier_login_wrong_account_data_error(self):
        '''Ошибка авторизации с несуществующей парой логин-пароль.'''
        response = self.request(
            method='post', url=CL.API, data=CL.WRONG_ACCOUNT
        )
        assert code_and_body_are_correct(response, **CL.NO_ACCOUNT)

    def test_delete_courier_success(self):
        '''Успешное удаление аккаунта курьера.'''
        account = get_account_data()
        response = self.request(
            method='post', url=CD.API, data=account
        )
        assert code_and_body_are_correct(response, **CREATED)
        account_id = self.request(
            method='post', url=CL.API, data=account
        ).json().get('id')
        response = self.request(
            method='delete', url=CD.API.format(id=account_id)
        )
        assert code_and_body_are_correct(response, **OK_TRUE)

    @pytest.mark.parametrize(
        '_id, expected',
        [pytest.param((WRONG_ID, CD.NO_ID), id='wrong id'),
         pytest.param(('', NOT_FOUND), id='empty id')]
    )
    def test_delete_courier_wrong_id_error(self, _id, expected):
        '''Ошибка при попытке удалить курьера с несуществующим id
        или без передачи id.'''
        response = self.request(
            method='delete', url=CD.API.format(id=_id)
        )
        assert code_and_body_are_correct(response, **expected)
