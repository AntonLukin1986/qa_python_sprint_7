'''Статичные данные для API-тестов web-сервиса «Яндекс.Самокат».'''
WRONG_ID = 0
# универсальные ответы
OK_TRUE = {'ok': True}
CREATED = 201, OK_TRUE
NOT_FOUND = 404, 'Not Found.'
OK = 200, OK_TRUE


class Courier:
    '''Управление курьерами.'''
    LOGIN_ONLY = {'login': 'test'}
    NO_PASSWORD = {'login': 'test', 'password': ''}  # без пароля - ошибка 504
    PASSWORD_ONLY = {'password': 'test'}
    WRONG_ACCOUNT = {'login': 'test', 'password': 'test'}
    DUPLICATE = 409, 'Этот логин уже используется. Попробуйте другой.'
    LOGGED_IN = 200, 'id', int
    MISSED_DATA_CREATE = 400, 'Недостаточно данных для создания учетной записи'
    MISSED_DATA_LOGIN = 400, 'Недостаточно данных для входа'
    NO_ACCOUNT = 404, 'Учетная запись не найдена'
    NO_ID = 404, 'Курьера с таким id нет.'


class Orders:
    '''Управление заказами.'''
    CREATED = 201, 'track', int
    GOT_ORDER = 200, 'order', dict
    ORDERS_LIST = 200, 'orders', list
    MISSED_DATA = 400, 'Недостаточно данных для поиска'
    NOT_FOUND_ORDER = 404, 'Заказ не найден'
    WRONG_COURIER_ID = 404, 'Курьера с таким id не существует'
    WRONG_ORDER_ID = 404, 'Заказа с таким id не существует'
    COLORS = ['GREY'], ['BLACK'], [], ['BLACK', 'GREY']
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
