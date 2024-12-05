'''Тесты эндпоинта для удаления курьеров.'''
import allure
import pytest

from data import Courier, NOT_FOUND, OK, WRONG_ID
from helpers import code_and_body_are_expected


class TestCourierDelete:

    @allure.title('Успешное удаление аккаунта курьера')
    def test_delete_courier_success(self, courier_methods, test_courier):
        '''Успешное удаление аккаунта курьера.'''
        _, account_id = courier_methods.login_courier(test_courier)
        response = courier_methods.delete_courier(account_id)
        assert code_and_body_are_expected(response, *OK)

    @allure.title('''Ошибка при попытке удалить курьера с несуществующим \
id или без передачи id''')
    @pytest.mark.parametrize(
        'account_id, expected',
        [pytest.param(WRONG_ID, Courier.NO_ID, id='wrong id'),
         pytest.param('', NOT_FOUND, id='empty id')]
    )
    def test_delete_courier_wrong_or_no_id_error(
        self, courier_methods, account_id, expected
    ):
        '''Ошибка при попытке удалить курьера с несуществующим id
        или без передачи id.'''
        response = courier_methods.delete_courier(account_id)
        assert code_and_body_are_expected(response, *expected)
