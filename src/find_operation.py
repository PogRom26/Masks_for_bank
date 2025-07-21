import os
import re

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
