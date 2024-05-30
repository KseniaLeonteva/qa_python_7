import pytest
from helpers import Helpers


@pytest.fixture(scope='function')
def helpers():
    return Helpers()

