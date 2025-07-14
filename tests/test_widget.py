import pytest

from src.widget import definition_account_or_card, get_date

# Тестируем распознавание карты или счета


@pytest.mark.parametrize(
    "card_or_account_info, masked_info",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("5999414228426353", "Не указаны все необходимые данные"),
    ],
)
def test_up_widget(card_or_account_info, masked_info):
    """Проверка корректного распознает и применяет нужный тип маскировки
    в зависимости от типа входных данных (карта или счет)."""

    assert definition_account_or_card(card_or_account_info) == masked_info


# Тестируем правильность преобразования даты


@pytest.mark.parametrize("input_info, out_info", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(input_info, out_info):
    assert get_date(input_info) == out_info
    assert input_info[0:4] == out_info[-4:]
    assert input_info[5:7] == out_info[-7:-5]
    assert input_info[8:10] == out_info[-10:-8]


@pytest.fixture
def date_example():
    return "2024-03-11T02:26:18.671407"


def test_len_date(date_example, len_data=26):
    """Тестирование на количество цифр в данных о карте и их расположение в конце строки"""

    count_symbol_date = 0
    for num in date_example:
        count_symbol_date += 1
    assert count_symbol_date == len_data
