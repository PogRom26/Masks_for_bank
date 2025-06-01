import pytest
from src.widget import mask_account_card, get_date

#Тестируем распознавание карты или счета

@pytest.mark.parametrize(
    "card_or_account_info, masked_info",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305")
    ],
)
def test_up_widget (card_or_account_info, masked_info):
    """Проверка корректного распознает и применяет нужный тип маскировки
    в зависимости от типа входных данных (карта или счет)."""

    assert mask_account_card(card_or_account_info) == masked_info

#Тестируем правильность преобразования даты

