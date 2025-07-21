import pytest

from src.find_operation import process_bank_search  # Импортируем тестируемую функцию

# Тестовые данные
TEST_DATA = [
    {"description": "Groceries ALDI", "amount": 50},
    {"description": "Transport Uber", "amount": 20},
    {"description": "ALDI groceries", "amount": 30},
    {"description": "Entertainment", "amount": 40},
    {"description": "Payment ALDI", "amount": 10},
    {"description": "Uber Eats", "amount": 15},
    {"amount": 100},  # Запись без description
]


# 1. Базовые тесты
def test_search_by_description():
    result = process_bank_search(TEST_DATA, "ALDI")
    assert len(result) == 3
    assert all("ALDI" in op["description"].upper() for op in result if "description" in op)


def test_empty_search_returns_all():
    result = process_bank_search(TEST_DATA, "")
    assert len(result) == len([d for d in TEST_DATA if any(isinstance(v, str) for v in d.values())])


def test_no_matches_returns_empty():
    result = process_bank_search(TEST_DATA, "NonExisting")
    assert result == []


# Тесты чувствительности к регистру
def test_case_insensitive_search():
    result = process_bank_search(TEST_DATA, "aldi")
    assert len(result) == 3
    result = process_bank_search(TEST_DATA, "ALDI")
    assert len(result) == 3


# Тест с частичным совпадением
def test_partial_match():
    result = process_bank_search(TEST_DATA, "eat")
    assert len(result) == 1
    assert "Uber Eats" in result[0]["description"]


# Параметризованные тесты
@pytest.mark.parametrize(
    "search_term,expected_count",
    [
        ("ALDI", 3),
        ("uber", 2),
        ("entertainment", 1),
        ("nonexistent", 0),
        ("", 6),  # Все записи со строковыми полями
    ],
)
def test_parametrized_search(search_term, expected_count):
    result = process_bank_search(TEST_DATA, search_term)
    assert len(result) == expected_count


# Тест с нестроковыми значениями
def test_non_string_values():
    test_data = [
        {"desc": "text", "num": 123},
        {"desc": "another", "flag": True},
        {"list": ["item1", "item2"]},
    ]
    result = process_bank_search(test_data, "text")
    assert len(result) == 1
    assert result[0]["desc"] == "text"
