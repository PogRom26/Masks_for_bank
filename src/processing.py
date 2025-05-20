def filter_by_state(list_with_dictions: list, key="EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    list_with_correct_key = []

    for diction in list_with_dictions:
        if diction.get("state") == key:
            list_with_correct_key.append(diction)

    return list_with_correct_key


def sort_by_date(list_with_dictions: list, key="EXECUTED") -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    sorted_list = sorted(list_with_dictionaries, key=lambda x: x["date"], reverse=True)

    return sorted_list

