from src.masks import get_mask_card_number, get_mask_account
import pytest

# Тестирование функций с картой
@pytest.mark.parametrize(
    "card_info, masked_card_info",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 599941422842635311", "Некорректный номер карты. Должно быть 16 цифр"),
        ("Visa Gold 59994142284263", "Некорректный номер карты. Должно быть 16 цифр"),
        ("","Номер карты не указан")
    ],
)
def test_get_mask_card_number(card_info, masked_card_info):
    """Тестирование правильности маскирования номера карты"""

    assert get_mask_card_number(card_info) == masked_card_info


#Тестирование функций со счетом
@pytest.mark.parametrize("account_info, masked_account_info",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 736541084301358743051", "Некорректный номер счета. Должно быть 20 цифр"),
        ("Счет 7365410843013587430", "Некорректный номер счета. Должно быть 20 цифр"),
        ("", "Номер счета не указан")
    ],
)

def test_up_get_mask_account(account_info, masked_account_info):
    """Тестирование правильности маскирования номера карты. Простой способ"""
    assert get_mask_account(account_info) == masked_account_info