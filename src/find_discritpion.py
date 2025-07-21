import os
from typing import Any
from pathlib import Path
from src.reading_trans import reading_transaction
from collections import Counter


def process_bank_operations(data:list[dict], categories:list)-> list[Any]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description"""

    #Формирование нового словаря с ключами - названиями категорий.
    key = "description"

    dict_with_names_category = []

    for item in data:
        if item.get(key) in categories:
            dict_with_names_category.append(item.get(key))

    #Подсчет количество операций в каждой категории
    counted  = Counter(dict_with_names_category)
    list_with_counter = counted.most_common()

    return list_with_counter
