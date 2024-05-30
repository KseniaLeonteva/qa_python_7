import pytest
import requests
from data import Endpoint, User
from helpers import Helpers


@pytest.fixture(scope='function')
def create_order():
    response_create_order = requests.post(Endpoint.CREATE_ORDER, json=User.user)
    track = response_create_order.json()['track']
    return track


@pytest.fixture(scope='function')
def create_courier(helpers):
    data = helpers.register_new_courier_and_return_login_password()
    response_post = requests.post(Endpoint.LOGIN_COURIER, data={
        'login': data[0],
        'password': data[1],
    })
    courier_id = response_post.json()['id']
    yield courier_id
    requests.delete(f'{Endpoint.DELETE_COURIER}/{courier_id}')


@pytest.fixture(scope='function')
def helpers():
    return Helpers()