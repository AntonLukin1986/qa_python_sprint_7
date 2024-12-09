'''Методы нэймспейса «Orders» API web-сервиса «Яндекс.Самокат».'''
import allure
import json
import requests

from config import (
    API_ORDERS, API_ORDERS_ACCEPT, API_ORDERS_CANCEL, API_ORDERS_GET
)


class OrdersMethods:

    @allure.step('Создание заказа.')
    def create_order(self, order_data):
        '''Создание заказа.'''
        response = requests.post(url=API_ORDERS, data=json.dumps(order_data))
        return response, response.json().get('track')

    @allure.step('Отмена заказа.')
    def cancel_order(self, track):
        '''Отмена заказа.'''
        return requests.put(url=API_ORDERS_CANCEL, data={'track': track})

    @allure.step('Получение всех заказов.')
    def get_all_orders(self):
        '''Получение всех заказов.'''
        return requests.get(url=API_ORDERS)

    @allure.step('Получение заказа по трек-номеру.')
    def get_order(self, track):
        '''Получение заказа по трек-номеру.'''
        response = requests.get(url=API_ORDERS_GET, params={'t': track})
        order_data = response.json().get('order')
        return response, order_data

    @allure.step('Принятие заказа курьером.')
    def accept_order(self, order_id, courier_id):
        '''Принятие заказа курьером.'''
        return requests.put(
            url=API_ORDERS_ACCEPT.format(id=order_id),
            params={'courierId': courier_id}
        )
