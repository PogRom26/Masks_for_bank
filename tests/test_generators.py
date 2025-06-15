import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def empty_data():
    return []


@pytest.fixture
def data_for_tests():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency(data_for_tests):
    """Проверяет, что функция корректно фильтрует транзакции по заданной валюте."""

    assert list(filter_by_currency(data_for_tests, code = "USD")) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
                                                                      {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
                                                                      {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}]

    assert list(filter_by_currency(data_for_tests, code = "RUB")) == [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
                                                                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]


def test_filter_by_currency_without_code (data_for_tests, empty_data):
    """Проверка, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют или список пуст."""

    assert next(filter_by_currency(data_for_tests, code = "ass")) == "В списке операций отсутствует запрашиваемая валюта или список операций"
    assert next(filter_by_currency(empty_data, "")) == "В списке операций отсутствует запрашиваемая валюта или список операций"


def test_transaction_descriptions(data_for_tests):
    """Проверка, что функция возвращает корректные описания для каждой транзакции."""

    assert (list(transaction_descriptions(data_for_tests)) ==
    ['Перевод организации',
 'Перевод со счета на счет',
 'Перевод со счета на счет',
 'Перевод с карты на карту',
 'Перевод организации'])


def test_transaction_descriptions_with_empty(empty_data):
    """Тестируйте работу функции с различным количеством входных транзакций, включая пустой список."""
    assert next(transaction_descriptions(empty_data)) == "В списке отсутствуют транзакции с описанием"


def test_card_number_generator(start = 1, stop = 5):
    current_list = list(card_number_generator(start, stop))
    expected_list = ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004']
    assert current_list == expected_list


def test_card_number_generator_correct_format_count_num():
    """Проверьте корректность форматирования номеров карт. Проверка на 16 цифр в номере карты"""

    formatted_number = next(card_number_generator(1,5))

    list_with_symbols = []
    for symbol in formatted_number:
        if symbol in "1234567890":
            list_with_symbols.append(symbol)
    assert len(list_with_symbols) == 16


def test_card_number_generator_correct_format():
    """Проверьте корректность форматирования номеров карт. Проверка на наличие трех пробелов в номере карты и их расположение"""

    formatted_number = next(card_number_generator(1,5))

    assert formatted_number[4:5] == " "
    assert formatted_number[9:10] == " "
    assert formatted_number[14:15] == " "


def test_card_number_generator_():
    """Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию"""

    assert next(card_number_generator(0, 5)) == "Выбранное число не входит в диапазон от 1 до 9999.9999.9999.9999"
    assert next(card_number_generator(1, 999999999999999999)) == "Выбранное число не входит в диапазон от 1 до 9999.9999.9999.9999"
    assert next(card_number_generator(5, 2)) == "Стартовое число больше или не отличается от конечного"
    assert next(card_number_generator(5, 5)) == "Стартовое число больше или не отличается от конечного"