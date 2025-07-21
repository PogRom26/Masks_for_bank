def filter_by_state(list_with_dictions: list, key: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    list_with_correct_key = []

    for diction in list_with_dictions:
        if "state" in diction:
            if diction.get("state") == key:
                list_with_correct_key.append(diction)

    return list_with_correct_key


def sort_by_date(list_with_dictions: list, key=lambda x: x["date"], reverse=True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""

    if key:
        sorted_list = sorted(list_with_dictions, key=key, reverse=reverse)
    else:
        sorted_list = sorted(list_with_dictions, reverse=reverse)

    return sorted_list
