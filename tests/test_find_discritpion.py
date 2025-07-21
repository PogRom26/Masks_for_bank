import pytest

from src.find_discritpion import process_bank_operations  # Импортируем тестируемую функцию

# Тестовые данные
TEST_DATA = [
    {"description": "Groceries", "amount": 50},
    {"description": "Transport", "amount": 20},
    {"description": "Groceries", "amount": 30},
    {"description": "Entertainment", "amount": 40},
    {"description": "Transport", "amount": 10},
]

TEST_CATEGORIES = ["Groceries", "Transport", "Utilities"]


# Базовый тест с реальными данными
def test_process_bank_operations_basic():
    result = process_bank_operations(TEST_DATA, TEST_CATEGORIES)
    assert result == [("Groceries", 2), ("Transport", 2)]


# Тест с пустыми данными
def test_empty_data():
    result = process_bank_operations([], TEST_CATEGORIES)
    assert result == []


# Тест с категориями, которых нет в данных
def test_no_matching_categories():
    result = process_bank_operations(TEST_DATA, ["Utilities"])
    assert result == []


# 5. Тест с частичным совпадением категорий
def test_partial_category_match():
    result = process_bank_operations(TEST_DATA, ["Groceries", "Utilities"])
    assert result == [("Groceries", 2)]


# Тест с отсутствующим полем description
def test_missing_description_field():
    invalid_data = [{"amount": 100}, {"description": "Groceries", "amount": 50}]
    result = process_bank_operations(invalid_data, TEST_CATEGORIES)
    assert result == [("Groceries", 1)]


# Параметризованный тест
@pytest.mark.parametrize(
    "data,categories,expected",
    [
        (TEST_DATA, TEST_CATEGORIES, [("Groceries", 2), ("Transport", 2)]),
        ([{"description": "A"}, {"description": "A"}], ["A"], [("A", 2)]),
        ([{"description": "B"}], ["C"], []),
    ],
)
def test_parametrized(data, categories, expected):
    assert process_bank_operations(data, categories) == expected
