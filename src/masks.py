def get_mask_card_number(card_numbers: str, len_card_number: int = 16) -> str:
    """принимает на вход номер карты и возвращает ее маску
    Видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками
    """

    # Считаем (проверяем) цифры в конце строки
    total_count_num = 0
    count_num_from_end = 0
    for num in card_numbers[-len_card_number:]:
        if num in "0123456789":
            count_num_from_end += 1

    # Считаем (проверяем), что всего 16 цифр в строке
    for num in card_numbers:
        if num in "0123456789":
            total_count_num += 1

    if total_count_num == 0:
        return "Номер карты не указан"

    elif len_card_number != total_count_num or len_card_number != count_num_from_end:
        return "Некорректный номер карты. Должно быть 16 цифр"

    else:
        card_numbers_masked = card_numbers[-16:-10] + "*" * 6 + card_numbers[-4:]

        first_num_quad = card_numbers_masked[-16:-12]
        second_num_quad = card_numbers_masked[-12:-8]
        third_num_quad = card_numbers_masked[-8:-4]
        fours_num_quad = card_numbers_masked[-4:]

        # выделение типа карты
        card_type = card_numbers[0:-17]

        card_numbers_masked_list = [first_num_quad, second_num_quad, third_num_quad, fours_num_quad]

        card_numbers_masked_with_space = " ".join(card_numbers_masked_list)

        return f"{card_type} {card_numbers_masked_with_space}"


def get_mask_account(account_number: str, len_account_number=20) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Видны только последние 4 цифры номера"""

    total_count_num = 0
    count_num_from_end = 0
    for num in account_number[-len_account_number:]:
        if num in "0123456789":
            count_num_from_end += 1

    # Считаем (проверяем), что всего 16 цифр в строке
    for num in account_number:
        if num in "0123456789":
            total_count_num += 1

    if total_count_num == 0:
        return "Номер счета не указан"

    elif len_account_number != total_count_num or len_account_number != count_num_from_end:
        return "Некорректный номер счета. Должно быть 20 цифр"

    else:
        count_letter = 0
        for i in account_number:
            if i.isalpha():
                count_letter += 1
        account_type = account_number[0:count_letter]

        account_number_masked = len(account_number[-6:-4]) * "*" + account_number[-4:]

        return f"{account_type} {account_number_masked}"
