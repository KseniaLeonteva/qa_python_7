import requests
import random
import string
from data import Endpoint
import allure


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


    def generate_data(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        return login, password, first_name


    def generate_data_payload(self):
        login, password, first_name = self.generate_data()
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        return payload


    @allure.step('Генерируем логин, пароль и имя курьера')
    def register_new_courier_and_return_login_password(self):
        login_pass = []
        payload = self.generate_data_payload()
        response = requests.post(Endpoint.CREATE_COURIER, data=payload)
        if response.status_code == 201:
            login_pass.append(payload['login'])
            login_pass.append(payload['password'])
            login_pass.append(payload['firstname'])
        return login_pass


    @allure.step('Удаляем курьера')
    def delete_courier(self, login, password):
        response_post = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login,
            'password': password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'{Endpoint.DELETE_COURIER}{courier_id}')

