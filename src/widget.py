from src.masks import get_mask_account, get_mask_card_number


def definition_account_or_card(user_account_or_cart: str, final_info: str = None) -> str:
    """Определяет счет или карту и маскирует их номера"""

    count_letter = 0
    for letter in user_account_or_cart:
        if letter not in "1234567890":
            count_letter += 1

    if count_letter < 4:
        final_info = "Не указаны все необходимые данные"

    elif "Счет" in user_account_or_cart:
        final_info = get_mask_account(user_account_or_cart)

    else:
        final_info = get_mask_card_number(user_account_or_cart)

    return final_info


def get_date(data_date_time: str, date_in_d_m_y=None) -> str:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""

    date_in_y_m_d = data_date_time[0 : data_date_time.index("T")]
    date_in_y_m_d_split = date_in_y_m_d.split("-")
    date_in_d_m_y = date_in_y_m_d_split[2], date_in_y_m_d_split[1], date_in_y_m_d_split[0]
    date_in_d_m_y_jointed = ".".join(date_in_d_m_y)
    return date_in_d_m_y_jointed
