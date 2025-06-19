import pytest

from src.decorators import log  # Импортируем ваш декоратор


# Тестовые функции
@log()
def successful_func(a, b):
    return a + b


@log()
def failing_func(x, y=0):
    raise ValueError("Invalid arguments")


# Тесты для вывода в консоль
def test_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""
    result = successful_func(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "successful_func - ОК" in captured.out


def test_console_error(capsys):
    """Тест ошибки с выводом в консоль"""
    with pytest.raises(ValueError):
        failing_func(10, y=5)

    captured = capsys.readouterr()
    output = captured.out

    assert "failing_func - ОШИБКА: ValueError" in output
    assert "Inputs: args=(10,), kwargs={'y': 5}" in output
    assert "Сообщение: Invalid arguments" in output


# Дополнительные тесты
def test_empty_args(capsys):
    """Тест функции без аргументов"""

    @log()
    def no_args():
        return 42

    no_args()

    captured = capsys.readouterr()
    assert "no_args - ОК" in captured.out


def test_kwargs_only(capsys):
    """Тест функции только с именованными аргументами"""

    @log()
    def kwargs_only(*, a, b):
        return a + b

    kwargs_only(a=1, b=2)

    captured = capsys.readouterr()
    assert "kwargs_only - ОК" in captured.out
    assert "Inputs: args=(), kwargs={'a': 1, 'b': 2}" in captured.out
