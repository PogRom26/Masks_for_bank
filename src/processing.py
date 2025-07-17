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


# Пример
# from pathlib import Path
# import os
# from src.reading_trans import reading_transaction
# from src.utils import load_transactions
#
# project_dir = Path(__file__).parent.parent
# data_dir = "data"
# data_folder = os.path.join(project_dir, data_dir)
#
# csv_files = [f.name for f in Path(data_folder).rglob('*.xlsx')]
# file_name = "".join(csv_files)
#
# path_to_file = os.path.join(project_dir, data_dir, file_name)
#
# file = reading_transaction(path_to_file)
# # file = load_transactions(path_to_file)
# print(f"{file} это список из файла")
# print()
# print(path_to_file)
#
# # for row in file:
# #     print(csv.)
#
# result = filter_by_state(file)
# # print(f" Вот такой результат {result}")
