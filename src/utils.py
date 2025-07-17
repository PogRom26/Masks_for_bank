import json
import logging
import os
from pathlib import Path
from typing import Any

# Создаем папку для логов, если её нет
log_dir = Path(__file__).parent.parent / "logs"

# Создание и получение именованного логера
logger = logging.getLogger(__name__)

# Установка уровня логирования
logger.setLevel(logging.DEBUG)

# Указываем полный путь к файлу
log_file = os.path.join(log_dir, f"{__name__}.log")  # Собираем путь корректно для ОС

# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler(log_file, mode="w")
logger.addHandler(file_handler)

# Форматер
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)


def load_transactions(file_path: str) -> list[Any] | list | str:
    """Загружает список транзакций из JSON-файла.
    Параметры: file_path: Путь к JSON-файлу с транзакциями
    Возвращает: Список словарей с транзакциями.
    Если файл не найден, пустой или содержит не список, возвращает пустой список"""

    try:
        path_to_file = file_path

        # Проверяем существование файла и что это файл
        if not os.path.exists(path_to_file) or not os.path.isfile(path_to_file):
            logger.error("Файл не существует или пустой")
            return f"Файл не существует или пустой"

        # Проверяем, что файл не пустой
        if os.path.getsize(path_to_file) == 0:
            logger.error("Файл пуст")
            return f"Файл пуст"

        # Читаем JSON
        with open(path_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем, что данные - это список
        if not isinstance(data, list):
            logger.error("В файле нет списка")
            return f"В файле нет списка"

        logger.error("Список успешно обработан")
        return data

    except (json.JSONDecodeError, ValueError):
        # Получаем возможные ошибки
        logger.error("Ошибка")
        return []
