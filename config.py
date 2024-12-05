'''Данные API web-сервиса «Яндекс.Самокат».'''
API_BASE = 'https://qa-scooter.praktikum-services.ru/api/v1/'

API_COURIER = API_BASE + 'courier/'
API_COURIER_DELETE = API_COURIER + '{id}'
API_COURIER_LOGIN = API_COURIER + 'login/'

API_ORDERS = API_BASE + 'orders'
API_ORDERS_ACCEPT = API_ORDERS + '/accept/{id}'
API_ORDERS_CANCEL = API_ORDERS + '/cancel'
API_ORDERS_GET = API_ORDERS + '/track'
