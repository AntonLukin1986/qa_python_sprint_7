'''Тесты эндпоинта для получения заказов.'''
import allure
import pytest
from data import Common, Orders
from helpers import code_and_body_are_expected, code_expected_and_data_in_body


class TestOrdersGet:

    @allure.title('Успешное получение заказов в виде списка')
    def test_get_orders_as_list_success(self, orders_methods):
        '''Успешное получение заказов в виде списка.'''
        response = orders_methods.get_all_orders()
        assert code_expected_and_data_in_body(response, *Orders.ORDERS_LIST)

    @allure.title('Успешное получение заказа по трек-номеру')
    def test_get_order_using_track_number_success(
            self, orders_methods, test_order
    ):
        '''Успешное получение заказа по трек-номеру.'''
        response, order_data = orders_methods.get_order(test_order)
        assert (
            code_expected_and_data_in_body(response, *Orders.GOT_ORDER) and
            test_order == order_data['track']
        )

    @allure.title('''Ошибка при попытке получить данные заказа без или по \
неверному трек-номеру''')
    @pytest.mark.parametrize(
        'track, expected',
        [(None, Orders.MISSED_DATA), (Common.WRONG_ID, Orders.NOT_FOUND_ORDER)]
    )
    def test_get_order_no_or_wrong_track_number_error(
        self, orders_methods, track, expected
    ):
        '''Ошибка при попытке получить данные заказа без или по неверному
        трек-номеру.'''
        response, _ = orders_methods.get_order(track)
        assert code_and_body_are_expected(response, *expected)
