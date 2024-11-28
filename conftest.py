'''Фикстуры для API-тестов web-сервиса «Яндекс.Самокат».'''
import pytest

from helpers import create_account, delete_account


@pytest.fixture(scope='function')
def register_new_courier():
    '''Создание новой учётной записи курьера с последующим удалением.'''
    response, account_data = create_account()
    yield response, account_data
    delete_account(account_data)
