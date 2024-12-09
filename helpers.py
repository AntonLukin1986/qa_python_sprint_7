'''Вспомогательные иснтрументы для API-тестов web-сервиса «Яндекс.Самокат».'''
import random
from string import ascii_lowercase, ascii_uppercase


def get_random_string(length=10):
    '''Генерация строки заданной длины из английских букв разного регистра.'''
    return ''.join(random.choices(ascii_lowercase + ascii_uppercase, k=length))


def get_account_data():
    '''Создание данных для регистрации аккаунта курьера.'''
    return {'firstName': get_random_string(),
            'login': get_random_string(),
            'password': get_random_string()}


def code_and_body_are_expected(response, code, message):
    '''Проверка соответствия статус-кода и тела ответа ожидаемым значениям.'''
    if isinstance(message, str):
        body = {'code': code, 'message': message}
    else:
        body = message
    return response.status_code == code and response.json() == body


def code_expected_and_data_in_body(response, code, key, _type):
    '''Проверка соответствия статус-кода и наличия данных требуемого типа
    в теле ответа.'''
    return response.status_code == code and \
        isinstance(response.json().get(key), _type)
