def filter_by_currency(transactions: list, code: str = None) -> iter:
    """принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    Если код валюты не задан, то выбираются все транзакции.
    """

    #Код валюты не передан в функцию
    if code is None:
        #Считаем, есть ли вообще строки с операциями в документе
        count_code_in_doc = 0
        for transaction in transactions:
            if transaction.get("operationAmount").get("currency").get("code"):
                count_code_in_doc += 1

        # Если записей не оказалось, то есть счетчик равен 0, то выдает соответствующее сообщение
        if count_code_in_doc == 0:
            yield "Список операций пуст"

        #В ином случае (счетчик не 0, записи есть), выдаем все такие записи
        else:
            for transaction in transactions:
                yield transaction

    #Код валюты определен
    else:
        #Считаем количество операций по указанной валюте
        count_code_in_doc = 0
        for transaction in transactions:
            if transaction.get("operationAmount").get("currency").get("code") == code:
                count_code_in_doc += 1

        #Если записей не оказалось, то есть счетчик равен 0, то выдает соответствующее сообщение
        if count_code_in_doc == 0:
            yield "В списке операций отсутствует запрашиваемая валюта или список операций"

        # Если записей с указанной валютой есть, то вернет список операций
        else:
            for transaction in transactions:
                if transaction.get("operationAmount").get("currency").get("code") == code:
                    yield transaction


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
