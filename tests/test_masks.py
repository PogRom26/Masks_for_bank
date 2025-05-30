from src.masks import get_mask_card_number

def test_up_get_mask_card_number ():
    assert get_mask_card_number('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'
