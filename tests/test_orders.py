'''Тесты эндпоинтов для управления заказами.'''
import json
import pytest
import requests

from data import CourierLogin as CL, Order, ORDER_DATA, WRONG_ID
from helpers import code_and_body_are_correct


class TestOrder:

    @pytest.mark.parametrize('color', Order.COLORS)
    def test_create_order_using_color_success(self, color):
        '''Успешное создание заказа с использованием поля "Цвет".'''
        ORDER_DATA['color'] = color
        response = requests.post(url=Order.API_MAIN, data=json.dumps(ORDER_DATA))  # вопрос на вебинар
        Order.CREATED['body']['track'] = response.json().get('track')
        assert code_and_body_are_correct(response, **Order.CREATED)

    def test_get_orders_as_list_success(self):
        '''Успешное получение заказов в виде списка.'''
        response = requests.get(url=Order.API_MAIN)
        orders = response.json().get('orders')
        assert response.status_code == Order.GET_ORDERS['code'] and isinstance(orders, Order.GET_ORDERS['type'])

    def test_accept_order_success(self, test_courier, test_order):
        '''Успешное принятие заказа.'''
        courier_id = requests.post(url=CL.API, data=test_courier).json().get('id')
        order_id = requests.get(url=Order.API_GET_ORDER, params={'t': test_order}).json().get('order').get('id')
        response = requests.put(url=Order.API_ACCEPT.format(id=order_id), params={'courierId': courier_id})
        assert code_and_body_are_correct(response, **{'code': 200, 'body': {'ok': True}})

    def test_accept_order_no_courier_id_error(self, test_order):
        '''Ошибка при попытке принять заказ без id курьера.'''
        order_id = requests.get(url=Order.API_GET_ORDER, params={'t': test_order}).json().get('order').get('id')
        response = requests.put(url=Order.API_ACCEPT.format(id=order_id))
        assert code_and_body_are_correct(response, **Order.MISSED_DATA)

    def test_accept_order_wrong_courier_id_error(self, test_order):
        '''Ошибка при попытке принять заказ с несуществующим id курьера.'''
        order_id = requests.get(url=Order.API_GET_ORDER, params={'t': test_order}).json().get('order').get('id')
        response = requests.put(url=Order.API_ACCEPT.format(id=order_id), params={'courierId': WRONG_ID})
        assert code_and_body_are_correct(response, **Order.WRONG_COURIER_ID)

    def test_accept_order_wrong_order_id_error(self, test_courier):
        '''Ошибка при попытке принять заказ с несуществующим id.'''
        courier_id = requests.post(url=CL.API, data=test_courier).json().get('id')
        response = requests.put(url=Order.API_ACCEPT.format(id=WRONG_ID), params={'courierId': courier_id})
        assert code_and_body_are_correct(response, **Order.WRONG_ORDER_ID)

    def test_accept_order_no_order_id_error(self, test_courier):
        '''Ошибка при попытке принять заказ без пердачи его id.'''
        courier_id = requests.post(url=CL.API, data=test_courier).json().get('id')
        response = requests.put(url=Order.API_ACCEPT.format(id=''), params={'courierId': courier_id})
        assert code_and_body_are_correct(response, **{'code': 404, 'body': {'code': 404, 'message': 'Not Found.'}})

    def test_get_order_using_track_number_success(self, test_order):
        '''Успешное получение заказа по его трек-номеру.'''
        response = requests.get(url=Order.API_GET_ORDER, params={'t': test_order})
        assert response.status_code == 200 and 'order' in response.json()

    def test_get_order_no_track_number_error(self):
        '''Ошибка при попытке получить данные заказа без трек-номера.'''
        response = requests.get(url=Order.API_GET_ORDER)
        assert code_and_body_are_correct(response, **Order.MISSED_DATA)

    def test_get_order_wrong_track_number_error(self):
        '''Ошибка при попытке получить заказ по несуществующему трек-номеру.'''
        response = requests.get(url=Order.API_GET_ORDER, params={'t': WRONG_ID})
        assert code_and_body_are_correct(response, **Order.NOT_FOUND_ORDER)
