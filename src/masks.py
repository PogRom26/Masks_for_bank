def get_mask_card_number(card_numbers: str) -> str:
    """принимает на вход номер карты и возвращает ее маску
    Видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками
    """
    card_numbers_masked = card_numbers[-16:-10] + "*" * 6 + card_numbers[-4:]

    first_num_quad = card_numbers_masked[-16:-12]
    second_num_quad = card_numbers_masked[-12:-8]
    third_num_quad = card_numbers_masked[-8:-4]
    fours_num_quad = card_numbers_masked[-4:]

    card_numbers_masked_list = [first_num_quad, second_num_quad, third_num_quad, fours_num_quad]

    card_numbers_masked_with_space = " ".join(card_numbers_masked_list)

    return card_numbers_masked_with_space


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Видны только последние 4 цифры номера"""
    account_number_masked = len(account_number[-6:-4]) * "*" + account_number[-4:]

    return account_number_masked
