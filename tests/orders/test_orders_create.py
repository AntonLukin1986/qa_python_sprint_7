'''Тесты эндпоинта для создания заказов.'''
import allure
import pytest

from data import Orders
from helpers import code_expected_and_data_in_body


class TestOrdersCreate:

    @allure.title('Успешное создание заказа с использованием поля "Цвет"')
    @pytest.mark.parametrize('color', Orders.COLORS)
    def test_create_order_using_color_success(self, orders_methods, color):
        '''Успешное создание заказа с использованием поля "Цвет".'''
        order_data = Orders.ORDER_DATA.copy()
        order_data['color'] = color
        response, track = orders_methods.create_order(order_data)
        orders_methods.cancel_order(track)
        assert code_expected_and_data_in_body(response, *Orders.CREATED)
