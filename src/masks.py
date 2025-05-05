def get_mask_card_number(card_numbers: str) -> str:
    """принимает на вход номер карты и возвращает ее маску
    Видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками
    """
    card_numbers_masked = card_numbers[0:6] + "*" * 6 + card_numbers[-4:]

    first_quad = card_numbers_masked[0:4]
    second_quad = card_numbers_masked[4:8]
    third_quad = card_numbers_masked[8:12]
    fours_quad = card_numbers_masked[12:16]

    card_numbers_masked_list = [first_quad, second_quad, third_quad, fours_quad]

    card_numbers_masked_with_space = " ".join(card_numbers_masked_list)

    return card_numbers_masked_with_space


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Видны только последние 4 цифры номера"""
    account_number_masked = len(account_number[-6:-4]) * "*" + account_number[-4:]

    return account_number_masked
