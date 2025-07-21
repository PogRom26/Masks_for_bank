import re
from collections import Counter
from typing import Iterator, List, Dict, Any, Generator


def filter_by_currency(transactions: List[Dict], code: str = None) -> Generator[
    dict | dict[str, str] | str, None, None]:
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
            yield "В списке операций отсутствует запрашиваемая валюта или список операций"

    # Код валюты указан
    else:
        found_any = False
        for t in transactions:
            currency = extract_currency(t)
            if currency == code:
                found_any = True
                yield t

        if not found_any:
            yield "В списке операций отсутствует запрашиваемая валюта или список операций"


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
