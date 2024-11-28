'''Вспомогательные иснтрументы для API-тестов web-сервиса «Яндекс.Самокат».'''
import random
from string import ascii_lowercase, ascii_uppercase

import requests

from data import Courier

ERROR = 'Ошибка при попытке {} тестового аккаунта курьера!'
CREATE_ERROR = ERROR.format('создания')
DELETE_ERROR = ERROR.format('удаления')


def get_random_string(length=10):
    '''Генерация строки заданной длины из английских букв разного регистра.'''
    return ''.join(random.choices(ascii_lowercase + ascii_uppercase, k=length))


def create_account():
    '''Создание тестового аккаунта курьера.'''
    account_data = {
        'firstName': get_random_string(),
        'login': get_random_string(),
        'password': get_random_string()
    }
    response = requests.post(url=Courier.API_CREATE, data=account_data)
    assert response.status_code == Courier.CREATED['code'], CREATE_ERROR
    return response, account_data


def delete_account(account_data):
    '''Удаление тестового аккаунта курьера.'''
    account_id = requests.post(
        url=Courier.API_LOGIN, data=account_data
    ).json().get('id')
    response = requests.delete(
        url=Courier.API_DELETE.format(id=account_id)
    )
    assert response.status_code == Courier.DELETED['code'], DELETE_ERROR


if __name__ == '__main__':
    pass
