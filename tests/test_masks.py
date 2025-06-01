from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest

#Тестирование функций с картой
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
def test_up_get_mask_account():
    """Тестирование правильности маскирования номера карты. Простой способ"""

    assert get_mask_account("Счет 73654108430135874305") == "Счет **4305"
    assert get_mask_account("Счет 35383033474447895560") == "Счет **5560"
    assert get_mask_account("Счет 73654108430135874305") == "Счет **4305"


@pytest.fixture
def account_num_example():
    return "Счет 73654108430135874305"

def test_len_account_number(account_num_example, len_account_number=20):
    """Тестирование на количество цифр в данных о карте и их расположение в конце строки"""

    total_count_num = 0
    count_num_from_end = 0
    for num in account_num_example[-len_account_number:]:
        if num in "0123456789":
            count_num_from_end += 1

    for num in account_num_example:
        if num in "0123456789":
            total_count_num += 1

    assert total_count_num == len_account_number
    assert count_num_from_end == len_account_number