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


# Для примера работы функций
list_with_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(filter_by_state(list_with_dictionaries))

print(sort_by_date(list_with_dictionaries))
