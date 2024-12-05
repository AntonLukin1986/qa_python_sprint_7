'''Тесты эндпоинта для принятия заказов.'''
import allure
import pytest
from data import NOT_FOUND, OK, WRONG_ID, Orders
from helpers import code_and_body_are_expected


class TestOrdersAccept:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(
            self, orders_methods, courier_methods, test_courier, test_order
    ):
        '''Успешное принятие заказа.'''
        _, courier_id = courier_methods.login_courier(test_courier)
        _, order_data = orders_methods.get_order(test_order)
        response = orders_methods.accept_order(
            order_data.get('id'), courier_id
        )
        assert code_and_body_are_expected(response, *OK)

    @allure.title(
        'Ошибка при попытке принять заказ без или с неверным id курьера'
    )
    @pytest.mark.parametrize(
        'courier_id, expected',
        [(None, Orders.MISSED_DATA), (WRONG_ID, Orders.WRONG_COURIER_ID)]
    )
    def test_accept_order_no_or_wrong_courier_id_error(
        self, orders_methods, test_order, courier_id, expected
    ):
        '''Ошибка при попытке принять заказ без или с неверным id курьера.'''
        _, order_data = orders_methods.get_order(test_order)
        response = orders_methods.accept_order(
            order_data.get('id'), courier_id
        )
        assert code_and_body_are_expected(response, *expected)

    @allure.title(
        'Ошибка при попытке принять заказ без или с неверным id заказа'
    )
    @pytest.mark.parametrize(
        'order_id, expected',
        [(WRONG_ID, Orders.WRONG_ORDER_ID), ('', NOT_FOUND)]
    )
    def test_accept_order_no_or_wrong_order_id_error(
        self, courier_methods, orders_methods, test_courier, order_id, expected
    ):
        '''Ошибка при попытке принять заказ без или с неверным id заказа.'''
        _, courier_id = courier_methods.login_courier(test_courier)
        response = orders_methods.accept_order(order_id, courier_id)
        assert code_and_body_are_expected(response, *expected)
