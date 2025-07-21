import re
from collections import Counter
from typing import Iterator, List, Dict


def filter_by_currency(transactions: List[Dict], code: str = None) -> Iterator[Dict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, выдающий транзакции, где валюта операции соответствует заданной (например, USD).
    Если код валюты не задан, возвращает все транзакции."""

    def extract_currency(transaction: dict) -> str | None:
        """Безопасно извлекает валюту из транзакции"""
        if isinstance(transaction.get('operationAmount'), dict):
            return transaction['operationAmount'].get('currency', {}).get('code')

        return transaction.get('currency_code') or None

    # Код валюты не указан
    if not code:
        if len(transactions) > 0:
            for t in transactions:
                yield t
        else:
            yield {"message": "Список операций пуст"}

    # Код валюты указан
    else:
        found_any = False
        for t in transactions:
            currency = extract_currency(t)
            if currency == code:
                found_any = True
                yield t

        if not found_any:
            yield {"message": f"В списке операций отсутствуют транзакции с валютой {code}"}


def transaction_descriptions(transactions: list) -> any:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    count_correct_description = 0
    for transaction in transactions:
        if transaction.get("description"):
            count_correct_description += 1
    if count_correct_description == 0:
        yield "В списке отсутствуют транзакции с описанием"
    else:
        for transaction in transactions:
            description = transaction.get("description")
            yield description


def card_number_generator(start=1, stop=9999999999999999):
    """который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    if start < 1 or stop > 9999999999999999:
        yield "Выбранное число не входит в диапазон от 1 до 9999.9999.9999.9999"

    elif start >= stop:
        yield "Стартовое число больше или не отличается от конечного"

    else:
        for number in range(start, stop):
            number = str(number).zfill(16)
            formatted_number = " ".join([number[i:i + 4] for i in range(0, len(number), 4)])
            yield formatted_number



########################################### Пример
# from pathlib import Path
# import os
# from src.reading_trans import reading_transaction
# from src.utils import load_transactions
#
#
# project_dir = Path(__file__).parent.parent
# data_dir = "data"
# data_folder = os.path.join(project_dir, data_dir)
#
# csv_files = [f.name for f in Path(data_folder).rglob('*.csv')]
# file_name = "".join(csv_files)
#
# path_to_file = os.path.join(project_dir, data_dir, file_name)
#
# file = reading_transaction(path_to_file)
# # file = load_transactions(path_to_file)
#
# # print(f"{file} это список из файла")
# print()
# # print(path_to_file)
# #
# result = list(filter_by_currency(file, "RUB"))
# # # #
# print(f" Вот такой результат {result}")

#
# for transaction in file:
#     if transaction["operationAmount"]["currency"]["code"] == "RUB":
#         print(transaction["operationAmount"]["currency"]["code"])
