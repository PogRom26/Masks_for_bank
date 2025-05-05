from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_account_or_cart: str, final_info=None) -> str:
    """Определяет счет или карту и маскирует их номера"""

    if 'Счет' in user_account_or_cart:
        final_info = get_mask_account(user_account_or_cart)
    else:
        final_info = get_mask_card_number(user_account_or_cart)

    return final_info
