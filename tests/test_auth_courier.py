import allure
import requests
from data import Endpoint, Message
from conftest import helpers


class TestAuthCourier:
    @allure.step('Авторизация курьера')
    def test_auth_courier(self, helpers):
        login_pass = helpers.register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        assert r.status_code == 200 and Message.LOGING_COURIER in r.text
        helpers.delete_courier(login_pass[0],login_pass[1])


    @allure.step('Авторизация курьера без логина')
    def test_auth_without_login(self, helpers):
        login_pass = helpers.register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': '',
            'password': login_pass[1]
        })
        assert r.status_code == 400 and Message.LOGING_COURIER_WITHOUT_DATA in r.text
        helpers.delete_courier(login_pass[0], login_pass[1])


    @allure.step('Авторизация курьера без пароля')
    def test_auth_without_password(self, helpers):
        login_pass = helpers.register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': ''
        })
        assert r.status_code == 400 and Message.LOGING_COURIER_WITHOUT_DATA in r.text
        helpers.delete_courier(login_pass[0], login_pass[1])


    @allure.step('Авторизация несуществующего курьера')
    def test_auth_not_existing_courier(self, helpers):
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': 'ksenia',
            'password': 'qwerty1234'
        })
        assert r.status_code == 404 and Message.LOGING_NOT_EXISTING_COURIER in r.text

