import pytest
from helpers import Helpers


@pytest.fixture(scope='function')
def helpers():
    return Helpers()


@pytest.fixture(scope='function')
def create_courier(helpers):
    login_pass = helpers.register_new_courier_and_return_login_password()
    yield login_pass
    helpers.delete_courier(login_pass[0], login_pass[1])

