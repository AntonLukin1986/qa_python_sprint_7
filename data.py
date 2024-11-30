'''Статичные данные для API-тестов web-сервиса «Яндекс.Самокат».'''
API_BASE = 'https://qa-scooter.praktikum-services.ru/api/v1/'

# универсальные ответы
NOT_FOUND = 404, 'Not Found.'  # NOT_FOUND = {'code': 404, 'body': {'code': 404, 'message': 'Not Found.'}}
OK_TRUE = 200, {'ok': True}  # {'code': 200, 'body': {'ok': True}}
CREATED = 201, {'ok': True}  # {'code': 201, 'body': {'ok': True}}
ORDER_DATA = {
    'firstName': 'Люси',
    'lastName': 'Маклин',
    'address': 'Убежище 33',
    'metroStation': 7,
    'phone': '213-25-VAULT',
    'rentTime': 3,
    'deliveryDate': '2297-05-15',
    'comment': 'War, war never changes'
}
WRONG_ID = 0


class CourierCreate:
    '''Создание аккаунта курьера.'''
    API = API_BASE + 'courier'
    LOGIN_ONLY = {'login': 'test'}
    PASSWORD_ONLY = {'password': 'test'}
    DUPLICATE = 409, 'Этот логин уже используется. Попробуйте другой.'  # {'code': 409, 'body': {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}
    MISSED_DATA = 400, 'Недостаточно данных для создания учетной записи'  # {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}}


class CourierDelete:
    '''Удаление аккаунта курьера.'''
    API = CourierCreate.API + '/{id}'
    NO_ID = 404, 'Курьера с таким id нет.'  # {'code': 404, 'body': {'code': 404, 'message': 'Курьера с таким id нет.'}}


class CourierLogin:
    '''Авторизация аккаунта курьера.'''
    API = CourierCreate.API + '/login'
    NO_PASSWORD = {'login': 'test', 'password': ''}  # вариант LOGIN_ONLY - ошибка 504
    WRONG_ACCOUNT = {'login': 'test', 'password': 'test'}
    LOGGED_IN = 200, {'id': int}  # {'code': 200, 'body': {'id': int}}
    MISSED_DATA = 400, 'Недостаточно данных для входа'  # {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для входа'}}
    NO_ACCOUNT = 404, 'Учетная запись не найдена'  # {'code': 404, 'body': {'code': 404, 'message': 'Учетная запись не найдена'}}


class Order:
    '''Управление заказами.'''
    API_MAIN = API_BASE + 'orders'
    API_ACCEPT = API_MAIN + '/accept/{id}'
    API_GET_ORDER = API_MAIN + '/track'
    API_CANCEL = API_MAIN + '/cancel'
    # данные для отправки
    COLORS = ['GREY'], ['BLACK'], [], ['BLACK', 'GREY']
    # ожидаемые ответы
    CREATED = {'code': 201, 'body': {'track': int}}
    GET_ORDERS = {'code': 200, 'type': list}
    MISSED_DATA = {
        'code': 400,
        'body': {'code': 400, 'message': 'Недостаточно данных для поиска'}
    }
    WRONG_COURIER_ID = {
        'code': 404,
        'body': {'code': 404, 'message': 'Курьера с таким id не существует'}
    }
    WRONG_ORDER_ID = {
        'code': 404,
        'body': {'code': 404, 'message': 'Заказа с таким id не существует'}
    }
    NOT_FOUND_ORDER = {
        'code': 404,
        'body': {'code': 404, 'message': 'Заказ не найден'}
    }
