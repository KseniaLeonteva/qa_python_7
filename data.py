class Endpoint:
    SCOOTER_URL = 'http://qa-scooter.praktikum-services.ru'
    # POST
    CREATE_COURIER = f'{SCOOTER_URL}/api/v1/courier'
    LOGIN_COURIER = f'{SCOOTER_URL}/api/v1/courier/login'
    CREATE_ORDER = f'{SCOOTER_URL}/api/v1/orders'
    # GET
    ORDER_LIST = f'{SCOOTER_URL}/api/v1/orders'
    GET_ORDER_TRACK = f'{SCOOTER_URL}/api/v1/orders/track'
    # DELETE
    DELETE_COURIER = f'{SCOOTER_URL}/api/v1/courier/'
    # PUT
    TAKE_ORDER = f'{SCOOTER_URL}/api/v1/orders/accept/'


class Message:
    CREATE_COURIER = '{"ok":true}'
    CREATE_EXISTING_COURIER = 'Этот логин уже используется'
    CREATE_COURIER_WITHOUT_LOGIN = 'Недостаточно данных для создания учетной записи'
    LOGING_COURIER = 'id'
    LOGING_COURIER_WITHOUT_DATA = 'Недостаточно данных для входа'
    LOGING_NOT_EXISTING_COURIER = 'Учетная запись не найдена'
    CREATE_ORDER = 'track'
    LIST_ORDERS = 'orders'
    DELETE_COURIER = '{"ok":true}'
    DELETE_COURIER_WITHOUT_ID = 'Not Found.'
    DELETE_NOT_EXISTING_COURIER = 'Курьера с таким id нет'
    TAKE_ORDER = '{"ok":true}'
    TAKE_ORDER_NOT_EXISTING_ID = 'Заказа с таким id не существует'
    TAKE_ORDER_NOT_EXISTING_COURIER = 'Курьера с таким id не существует'
    TAKE_ORDER_AGAIN = 'Этот заказ уже в работе'
    TAKE_ORDER_WITHOUT_ID_COURIER_OR_ORDER = 'Недостаточно данных для поиска'
    GET_ORDER = 'order'
    GET_ORDER_WITHOUT_TRACK = 'Недостаточно данных для поиска'
    GET_ORDER_NOT_EXISTING_TRACK = 'Заказ не найден'


class User:
    user = {
        'firstName': 'Ксения',
        'lastname': 'Леонтьева',
        'address': 'Москва',
        'metroStation': 5,
        'phone': '+79169233233',
        'rentTime': 2,
        'deliveryDate': '2024-07-10',
        'comment': ''
    }

