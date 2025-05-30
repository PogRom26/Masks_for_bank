from src.masks import get_mask_card_number

def test_up_get_mask_card_number ():
    assert get_mask_card_number('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'
    assert get_mask_card_number('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert get_mask_card_number('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'


import pytest

@pytest.mark.parametrize("card_info, masked_card_info", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")])

def test_get_mask_card_number (card_info, masked_card_info):
    assert get_mask_card_number(card_info) == masked_card_info

