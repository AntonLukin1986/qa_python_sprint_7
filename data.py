'''Статичные данные для API-тестов web-сервиса «Яндекс.Самокат».'''
API_BASE = 'https://qa-scooter.praktikum-services.ru/api/v1/'


class Courier:
    '''Эндпоинты, управляющие аккаунтом курьера.'''
    API_CREATE = API_BASE + 'courier'
    API_DELETE = API_BASE + 'courier/{id}'
    API_LOGIN = API_BASE + 'courier/login'
    # данные для отправки
    LOGIN_ONLY = {'login': 'test'}
    PASSWORD_ONLY = {'password': 'test'}
    NO_PASSWORD = {  # для теста логина (вариант LOGIN_ONLY - ошибка 504)
        'login': 'test', 'password': ''
    }
    WRONG_ACCOUNT = {'login': 'test', 'password': 'test'}
    WRONG_ID = 0
    # ожидаемые ответы
    CREATED = {'code': 201, 'body': {'ok': True}}
    DELETED = {'code': 200, 'body': {'ok': True}}
    LOGGED_IN = {'code': 200, 'body': {'id': int}}
    DUPLICATE = {
        'code': 409,
        'body': {
            'code': 409,
            'message': 'Этот логин уже используется. Попробуйте другой.'
        }
    }
    MISSED_DATA_CREATE = {
        'code': 400,
        'body': {
            'code': 400,
            'message': 'Недостаточно данных для создания учетной записи'
        }
    }
    MISSED_DATA_LOGIN = {
        'code': 400,
        'body': {'code': 400, 'message': 'Недостаточно данных для входа'}
    }
    NO_ACCOUNT = {
        'code': 404,
        'body': {'code': 404, 'message': 'Учетная запись не найдена'}
    }
    NO_ID = {
        'code': 404,
        'body': {'code': 404, 'message': 'Курьера с таким id нет.'}
    }
