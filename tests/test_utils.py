import pytest
import json
import os

from src.utils import load_transactions  # Замените на ваш модуль


@pytest.fixture
def file_path():
    """ Указываем путь на файл JSON """

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/operations.json"
    return path


@pytest.fixture
def file_empty_path():
    """ Указываем путь на пустой файл """

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/operations_empty.json"
    return path


@pytest.fixture
def to_dir_path():
    """ Указываем путь на директорию """

    path = "/Users/romanpogorelcev/Documents/Pytons PRO/PythonProject/Masks_for_bank/data/"
    return path


def test_empty_file(file_empty_path):
    """Тест пустого файла"""

    result = load_transactions(file_empty_path)
    assert result == []


def test_nonexistent_file():
    """Тест несуществующего файла"""

    result = load_transactions("nonexistent.json")
    assert result == []


def test_directory_instead_of_file(to_dir_path):
    """Тест передачи директории вместо файла"""
    result = load_transactions(to_dir_path)
    assert result == []
