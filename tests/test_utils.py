import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions

# Тестовые данные
TEST_TRANSACTIONS = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]


@pytest.fixture
def file_path():
    """Указываем путь на файл JSON"""

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/operations.json"
    return path


@pytest.fixture
def file_empty_path():
    """Указываем путь на пустой файл"""

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/operations_empty.json"
    return path


@pytest.fixture
def to_dir_path():
    """Указываем путь на директорию"""

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/"
    return path


def test_nonexistent_file():
    """Тест несуществующего файла"""

    result = load_transactions("nonexistent.json")
    assert result == []


def test_directory_instead_of_file(to_dir_path):
    """Тест передачи директории вместо файла"""
    result = load_transactions(to_dir_path)
    assert result == []


def test_successful_load():
    """Тест успешной загрузки валидного JSON файла"""
    mock_json = json.dumps(TEST_TRANSACTIONS)

    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("builtins.open", mock_open(read_data=mock_json)),
    ):
        result = load_transactions("valid.json")
        assert result == TEST_TRANSACTIONS


def test_file_not_found():
    """Тест случая, когда файл не существует"""
    with patch("os.path.exists", return_value=False):
        result = load_transactions("missing.json")
        assert result == []


def test_path_is_directory():
    """Тест случая, когда путь ведет к директории"""
    with patch("os.path.exists", return_value=True), patch("os.path.isfile", return_value=False):
        result = load_transactions("some_directory/")
        assert result == []


def test_empty_file():
    """Тест пустого файла"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=0),
    ):
        result = load_transactions("empty.json")
        assert result == []


def test_invalid_json():
    """Тест невалидного JSON"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("builtins.open", mock_open(read_data="invalid json")),
        patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)),
    ):
        result = load_transactions("invalid.json")
        assert result == []


def test_json_not_list():
    """Тест случая, когда JSON не является списком"""
    mock_data = {"transactions": TEST_TRANSACTIONS}

    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("builtins.open", mock_open(read_data=json.dumps(mock_data))),
    ):
        result = load_transactions("not_list.json")
        assert result == []
