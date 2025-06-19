from functools import wraps


def log(filename=None):
    """Декоратор для логирования выполнения функций"""

    def decorator(func):
        @wraps(func)

        def wrapper(*args, **kwargs):
            args_repr = f"args={args}, kwargs={kwargs}"
            # Выводим логи (в файл или консоль)
            def write_log(message):
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(message + '\n')
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                result_msg = f"{func.__name__} - ОК"
                write_log(result_msg)

                return result

            except Exception as e:
                error_type = type(e).__name__
                error_msg = (f"{func.__name__} - ОШИБКА: {error_type} - "
                             f"Inputs: {args_repr} - Сообщение: {str(e)}")
                write_log(error_msg)
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator