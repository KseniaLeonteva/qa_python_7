import allure
import requests
import pytest
from data import Endpoint, Message
from conftest import helpers


class TestCreateCourier:
    @allure.step('Создать курьера')
    def test_create_courier(self, helpers):
        login, password, first_name = helpers.generate_data()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        r = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert r.status_code == 201 and Message.CREATE_COURIER in r.text
        helpers.delete_courier(login, password)


    @allure.step('Создать двух одинаковых курьеров')
    def test_create_existing_courier(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.CREATE_COURIER, data={
            'login': data[0],
            'password': data[1],
            'firstName': data[2]
        })
        assert r.status_code == 409 and Message.CREATE_EXISTING_COURIER in r.text


    @allure.step('Создать курьера без логина/пароля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_field(self, field, helpers):
        payload = helpers.generate_data_payload()
        del payload[field]
        r = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert r.status_code == 400 and Message.CREATE_COURIER_WITHOUT_LOGIN in r.text

