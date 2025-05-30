from src.masks import get_mask_card_number


def test_up_get_mask_card_number():
    assert get_mask_card_number("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert get_mask_card_number("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert get_mask_card_number("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"


import pytest


@pytest.fixture
def card_num_example():
    return "Visa Platinum 7000792289606361"


@pytest.mark.parametrize(
    "card_info, masked_card_info",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card_info, masked_card_info):
    assert get_mask_card_number(card_info) == masked_card_info


def test_len_card_number(card_num_example, len_card_number=16):
    count_num = 0
    for num in card_num_example[-16:]:
        if num in "0123456789":
            count_num += 1
    assert count_num == len_card_number
