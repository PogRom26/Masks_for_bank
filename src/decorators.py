import logging
from functools import wraps


def log(filename=None):
    """ Декоратор для логирования выполнения функций."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Настройка логирования
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # Формат логов
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

            # Определяем куда писать логи
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()

            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                # Логируем начало выполнения
                logger.info(f"Начало выполнения функции {func.__name__}")
                logger.info(f"Аргументы: args={args}, kwargs={kwargs}")

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                logger.info(f"Функция {func.__name__} выполнена успешно")
                logger.info(f"Результат: {result}")

                return result

            except Exception as e:
                # Логируем ошибку
                logger.error(f"Ошибка в функции {func.__name__}: {str(e)}", exc_info=True)
                raise  # Пробрасываем исключение дальше

            finally:
                # Удаляем обработчик, чтобы избежать дублирования логов
                logger.removeHandler(handler)

        return wrapper

    return decorator