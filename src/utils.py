import json
import os


def load_transactions(file_path: str) -> list:
    """ Загружает список транзакций из JSON-файла.
    Параметры: file_path: Путь к JSON-файлу с транзакциями
    Возвращает: Список словарей с транзакциями.
    Если файл не найден, пустой или содержит не список, возвращает пустой список """

    try:
        path_to_file = file_path

        # Проверяем существование файла и что это файл
        if not os.path.exists(path_to_file) or not os.path.isfile(path_to_file):
            return []

        # Проверяем, что файл не пустой
        if os.path.getsize(path_to_file) == 0:
            return []

        # Читаем JSON
        with open(path_to_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, что данные - это список
        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, ValueError):
        # Получаем возможные ошибки
        return []
