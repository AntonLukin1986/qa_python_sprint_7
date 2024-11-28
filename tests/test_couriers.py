'''Тесты эндпоинтов для создания, удаления и авторизации курьеров.'''
import pytest
import requests

from data import Courier


class TestCourier:

    def code_and_body_are_correct(self, response, code, body):
        '''Проверка на соответствие статус-кода и структуры ответа.'''
        return response.status_code == code and response.json() == body

    def test_create_courier_account_success(self, register_new_courier):
        '''Успешное создание учётной записи курьера.'''
        response, _ = register_new_courier
        assert self.code_and_body_are_correct(response, **Courier.CREATED)

    def test_create_courier_duplicate_error(self, register_new_courier):
        '''Невозможно создать двух курьеров с одинаковым логином.'''
        _, exist_account = register_new_courier                                 # дубль 1
        response = requests.post(url=Courier.API_CREATE, data=exist_account)    #
        assert self.code_and_body_are_correct(response, **Courier.DUPLICATE)

    @pytest.mark.parametrize(
        'payload',
        [
            pytest.param(Courier.LOGIN_ONLY, id='login only'),
            pytest.param(Courier.PASSWORD_ONLY, id='password only')
        ]
    )
    def test_create_courier_missed_data_error(self, payload):
        '''Невозможно создать курьера без логина или пароля.'''
        response = requests.post(url=Courier.API_CREATE, data=payload)
        assert self.code_and_body_are_correct(response, **Courier.MISSED_DATA_CREATE)

    def test_courier_login_success(self, register_new_courier):
        '''Успешная авторизация курьера.'''
        _, exist_account = register_new_courier                                 # дубль 1
        response = requests.post(url=Courier.API_LOGIN, data=exist_account)     #
        Courier.LOGGED_IN['body']['id'] = response.json().get('id')
        assert self.code_and_body_are_correct(response, **Courier.LOGGED_IN)

    @pytest.mark.parametrize(
        'payload',
        [
            pytest.param(Courier.NO_PASSWORD, id='no password'),
            pytest.param(Courier.PASSWORD_ONLY, id='password only')
        ]
    )
    def test_login_courier_missed_data_error(self, payload):
        '''Невозможно войти в аккаунт курьера без логина или пароля.'''
        response = requests.post(url=Courier.API_LOGIN, data=payload)
        assert self.code_and_body_are_correct(response, **Courier.MISSED_DATA_LOGIN)

    def test_login_courier_wrong_account_error(self):
        '''Запрос авторизации с несуществующей парой логин-пароль.'''
        response = requests.post(url=Courier.API_LOGIN, data=Courier.WRONG_ACCOUNT)
        assert self.code_and_body_are_correct(response, **Courier.NO_ACCOUNT)

    def test_delete_courier_success(self, register_new_courier):
        '''Успешное удаление аккаунта курьера.'''
        _, exist_account = register_new_courier                                                 # дубль 1
        exist_id = requests.post(url=Courier.API_LOGIN, data=exist_account).json().get('id')    #
        response = requests.delete(url=Courier.API_DELETE.format(id=exist_id))
        assert self.code_and_body_are_correct(response, **Courier.DELETED)

    def test_delete_courier_wrong_id_error(self):
        '''Ошибка при попытке удаления курьера по несуществующему id.'''
        response = requests.delete(url=Courier.API_DELETE.format(id=Courier.WRONG_ID))
        assert self.code_and_body_are_correct(response, **Courier.NO_ID)
