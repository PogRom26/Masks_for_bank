import os
import re
from pathlib import Path

from src.reading_trans import reading_transaction

def process_bank_search(data:list[dict], search:str = "")->list[dict]:
    """Функция для поиска в списке словарей операций по заданной строке — описанию.
    Принимает два аргумента: список с транзакциями и строку для поиска.
    Возвращает список словарей с операциями, у которых в описании есть строка, переданная аргументу функции."""

    list_with_operation = []

    pattern = search

    for item in data:
        # Проверяем все значения словаря
        for value in item.values():
            if isinstance(value, str):
                if re.search(pattern, value, re.IGNORECASE):
                    list_with_operation.append(item)
                    break
    return list_with_operation

# Пример работы программы
# project_dir = Path(__file__).parent.parent
# data_dir = "data"
# file_name = "transactions_excel.xlsx"
# path_to_file = os.path.join(project_dir, data_dir, file_name)
#
# data = reading_transaction(path_to_file)
# print(process_bank_search(data, "пере"))
