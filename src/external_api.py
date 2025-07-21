import os

import requests
from dotenv import load_dotenv


def get_currency_rate(finish_curr: str, start_curr: str, how_many: float) -> any:
    """Принимает тип конечной валюты, тип начальной валюты и сумму.
    После чего обращается по API за курсом валюты
    и конвертирует сумму начальной валюты в конечную"""

    load_dotenv()

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}

    to = finish_curr
    from_str = start_curr
    amount = how_many

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_str}&amount={amount}"

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        return response.reason

    result_of_response = response.json()
    result = result_of_response["result"]

    return result


def currency_conversion(list_with_transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли"""

    summ_in_rub = 0
    if list_with_transaction["operationAmount"]["currency"]["code"] == "RUB":
        summ_in_rub = list_with_transaction["operationAmount"]["amount"]

    if list_with_transaction["operationAmount"]["currency"]["code"] != "RUB":
        operation_amount = list_with_transaction["operationAmount"]["amount"]
        start_curr = list_with_transaction["operationAmount"]["currency"]["code"]
        finish_curr = "RUB"

        summ_in_rub = get_currency_rate(finish_curr, start_curr, operation_amount)

    return summ_in_rub
