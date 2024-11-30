'''Вспомогательные иснтрументы для API-тестов web-сервиса «Яндекс.Самокат».'''
import random
from string import ascii_lowercase, ascii_uppercase

import requests

from data import (
    CourierCreate as CC, CourierDelete as CD, CourierLogin as CL, Order,
    ORDER_DATA
)

ERROR = 'Ошибка при попытке {} тестового {}!'


def get_random_string(length=10):
    '''Генерация строки заданной длины из английских букв разного регистра.'''
    return ''.join(random.choices(ascii_lowercase + ascii_uppercase, k=length))


def get_account_data():
    '''Создание данных для регистрации аккаунта курьера.'''
    return {'firstName': get_random_string(),
            'login': get_random_string(),
            'password': get_random_string()}


def create_account():
    '''Создание тестового аккаунта курьера.'''
    account_data = get_account_data()
    response = requests.post(url=CC.API, data=account_data)
    assert response.status_code == 201, ERROR.format('создания', 'аккаунта')
    return account_data


def delete_account(account_data):
    '''Удаление тестового аккаунта курьера.'''
    account_id = requests.post(
        url=CL.API, data=account_data
    ).json().get('id')
    response = requests.delete(
        url=CD.API.format(id=account_id)
    )
    assert response.status_code == 200, ERROR.format('удаления', 'аккаунта')


def create_order():
    '''Создание тестового заказа.'''
    response = requests.post(url=Order.API_MAIN, data=ORDER_DATA)
    assert response.status_code == 201, ERROR.format('создания', 'заказа')
    return response.json().get('track')


def cancel_order(track):
    '''Отмена тестового заказа.'''
    response = requests.put(url=Order.API_CANCEL, data={'track': track})
    assert response.status_code == 200, ERROR.format('удаления', 'заказа')


def expected(code, message):
    '''Получение словаря с ожидаемыми кодом и телом ответа API.'''
    if isinstance(message, str):
        body = {'code': code, 'message': message}
    else:
        body = message
    return {'code': code, 'body': body}


def code_and_body_are_correct(response, code, body):
    '''Проверка на соответствие статус-кода и структуры ответа.'''
    return response.status_code == code and response.json() == body

# def code_and_body_are_correct(response, exp):
#     '''Проверка на соответствие статус-кода и структуры ответа.'''
#     result = expected(*exp)
#     return response.status_code == result['code'] and \
#         response.json() == result['body']


if __name__ == '__main__':
    pass
