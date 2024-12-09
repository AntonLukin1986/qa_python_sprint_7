'''Методы нэймспейса «Courier» API web-сервиса «Яндекс.Самокат».'''
import allure
import requests

from config import API_COURIER, API_COURIER_LOGIN, API_COURIER_DELETE


class CourierMethods:

    @allure.step('Создание аккаунта курьера.')
    def create_courier(self, account_data):
        '''Создание аккаунта курьера.'''
        return requests.post(url=API_COURIER, data=account_data), account_data

    @allure.step('Авторизация курьера.')
    def login_courier(self, account_data):
        '''Авторизация курьера.'''
        response = requests.post(url=API_COURIER_LOGIN, data=account_data)
        return response, response.json().get('id')

    @allure.step('Удаление аккаунта курьера.')
    def delete_courier(self, account_id):
        '''Удаление аккаунта курьера.'''
        return requests.delete(url=API_COURIER_DELETE.format(id=account_id))
