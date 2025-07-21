import pytest
from pathlib import Path
from datetime import datetime
from main import main
from src.utils import load_transactions, reading_transaction
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.find_operation import process_bank_search

# Директории проекта
PROJECT_DIR = Path(__file__).parents[1]
DATA_DIR = PROJECT_DIR / "data"

@pytest.fixture(scope="module")
def sample_data():
    return [
        {
            "state": "EXECUTED",
            "amount": 100,
            "currency": "RUB",
            "description": "Операция выполнена успешно"
        },
        {
            "state": "CANCELED",
            "amount": 200,
            "currency": "USD",
            "description": "Операция отменена"
        }
    ]

def test_load_json_file(sample_data):
    """Проверяет загрузку данных из JSON-файла."""
    result = main("JSON", "", False, False, "", "")
    assert result == sample_data

def test_load_csv_file(sample_data):
    """Тестирует чтение данных из CSV-файла."""
    result = main("CSV", "", False, False, "", "")
    assert result == sample_data

def test_load_xlsx_file(sample_data):
    """Обрабатывает данные из XLSX-файла."""
    result = main("XLSX", "", False, False, "", "")
    assert result == sample_data

def test_filter_executed_state(sample_data):
    """Применяет фильтрацию по статусу EXECUTED."""
    result = main("JSON", "EXECUTED", False, False, "", "")
    expected_result = filter_by_state(sample_data, "EXECUTED")
    assert result == expected_result

def test_sort_by_date_descending(sample_data):
    """Сортирует транзакции по дате в порядке убывания."""
    result = main("JSON", "", True, True, "", "")
    sorted_list = sort_by_date(sample_data)
    assert result == sorted_list

def test_filter_by_rubles(sample_data):
    """Оставляет только рублёвую валюту."""
    result = main("JSON", "", False, False, "RUB", "")
    filtered_list = list(filter_by_currency(sample_data, "RUB"))
    assert result == filtered_list

def test_search_by_keyword(sample_data):
    """Осуществляет поиск по ключевым словам."""
    keyword = "Перевод"
    result = main("JSON", "", False, False, "", keyword)
    processed_list = process_bank_search(sample_data, keyword)
    assert result == processed_list

def test_no_matching_transactions():
    """Проверяет реакцию функции, когда нет совпадений по фильтрам."""
    result = main("JSON", "NON_EXISTING_STATE", False, False, "USD", "KeywordNotInData")
    expected_message = "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    assert result == expected_message