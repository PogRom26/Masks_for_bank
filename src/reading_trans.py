import csv

import pandas as pd


def reading_transaction(path_to_file: str) -> list:
    """Функция получает путь к файлу с транзакциями, определяет тип файла,
    обрабатывает файл и выдает список словарей с транзакциями"""

    transactions = []

    try:

        # Код для CSV файлов
        if path_to_file.endswith("csv"):
            with open(path_to_file, "r") as file:
                reader = csv.DictReader(file, delimiter=";")
                for row in reader:
                    transactions.append(dict(row))

        # Код для EXCEL файлов
        elif path_to_file.endswith("xlsx"):
            df = pd.read_excel(path_to_file)
            transactions = df.to_dict(orient="records")

        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл '{path_to_file}' не найден.")

    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return transactions
