'''Фикстуры для API-тестов web-сервиса «Яндекс.Самокат».'''
import pytest

from helpers import cancel_order, create_account, create_order, delete_account


@pytest.fixture(scope='function')
def test_courier():
    '''Создание тестовой учётной записи курьера с последующим удалением.'''
    account_data = create_account()
    yield account_data
    delete_account(account_data)


@pytest.fixture(scope='function')
def test_order():
    '''Создание тестового заказа с последующим удалением.'''
    track = create_order()
    yield track
    cancel_order(track)
