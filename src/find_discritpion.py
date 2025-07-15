from typing import Any
from pathlib import Path
import pandas as pd


from src.reading_trans import reading_transaction

def process_bank_operations(data:list[dict], categories:list)-> list[Any]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description"""

    # Путь к текущему модулю
    current_dir = Path(__file__).parent
    file_address = current_dir.parent / "src" / "transactions_excel.xlsx"

    data_with_trans = reading_transaction(file_address)
    categories = ["Перевод организации", "Открытие вклада"]

    #Формирование нового словаря с ключами - названиями категорий.

    key = "description"

    dict_with_names_category = []

    for item in data_with_trans:
        if item.get(key) not in dict_with_names_category:
            dict_with_names_category.append(item.get(key))




    # return data_with_trans
    return dict_with_names_category



# Путь к текущему модулю
current_dir = Path(__file__).parent

# Путь к файлу в соседней папке
file_path = current_dir.parent / "соседняя_папка" / "файл.txt"


file_address = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/transactions_excel.xlsx"
data = reading_transaction(file_address)
categories = ["Перевод организации", "Открытие вклада"]
print(process_bank_operations(data, categories))