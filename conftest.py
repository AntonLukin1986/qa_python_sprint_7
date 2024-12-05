'''Фикстуры для API-тестов web-сервиса «Яндекс.Самокат».'''
import pytest

from endp_methods.courier_methods import CourierMethods
from endp_methods.orders_methods import OrdersMethods
from data import Orders
from helpers import get_account_data


@pytest.fixture(scope='function')
def courier_methods():
    return CourierMethods()


@pytest.fixture(scope='function')
def orders_methods():
    return OrdersMethods()


@pytest.fixture(scope='function')
def test_courier(courier_methods):
    '''Создание тестовой учётной записи курьера с последующим удалением.'''
    _, account_data = courier_methods.create_courier(get_account_data())
    yield account_data
    courier_methods.delete_courier(account_data)


@pytest.fixture(scope='function')
def test_order(orders_methods):
    '''Создание тестового заказа с последующим удалением.'''
    _, track = orders_methods.create_order(Orders.ORDER_DATA)
    yield track
    orders_methods.cancel_order(track)
