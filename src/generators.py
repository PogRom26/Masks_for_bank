from src.transactions import transactions


def filter_by_currency (transactions:list, code: str = "USD") -> iter:
    """принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == code:
            yield transaction


def transaction_descriptions(transactions:any) -> any:
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description")
        yield description


def card_number_generator():
    """который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    pass

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
