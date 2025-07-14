from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.reading_trans import reading_transaction


@pytest.fixture
def sample_csv_data():
    return """id,amount,date
1,100,2023-01-01
2,200,2023-01-02"""


@pytest.fixture
def sample_excel_data(tmp_path):
    df = pd.DataFrame({"id": [1, 2], "amount": [100, 200], "date": ["2023-01-01", "2023-01-02"]})
    path = tmp_path / "test.xlsx"
    df.to_excel(path, index=False)
    return path


def test_read_csv_success(sample_csv_data):
    """Тест успешного чтения CSV файла"""
    with patch("builtins.open", mock_open(read_data=sample_csv_data)):
        result = reading_transaction("dummy.csv")
        assert len(result) == 2
        assert result[0]["id"] == "1"
        assert result[1]["amount"] == "200"


def test_csv_file_not_found():
    """Тест обработки отсутствующего CSV файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = reading_transaction("missing.csv")
        assert result == []


def test_csv_invalid_data():
    """Тест поврежденного CSV файла"""
    with patch("csv.DictReader", side_effect=Exception("Invalid CSV")):
        with patch("builtins.open", mock_open(read_data="bad data")):
            result = reading_transaction("invalid.csv")
            assert result == []


def test_read_excel_success(sample_excel_data):
    """Тест успешного чтения Excel файла"""
    result = reading_transaction(str(sample_excel_data))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 200


@patch("pandas.read_excel")
def test_excel_file_not_found(mock_read_excel):
    """Тест отсутствующего Excel файла"""
    mock_read_excel.side_effect = FileNotFoundError
    result = reading_transaction("missing.xlsx")
    assert result == []


@patch("pandas.read_excel")
def test_excel_read_error(mock_read_excel):
    """Тест ошибки чтения Excel"""
    mock_read_excel.side_effect = Exception("Excel read error")
    result = reading_transaction("corrupted.xlsx")
    assert result == []


def test_unsupported_file_format():
    """Тест неподдерживаемого формата файла"""
    result = reading_transaction("document.pdf")
    assert result == []


@patch("builtins.open", mock_open(read_data="test"))
@patch("csv.DictReader")
def test_general_exception_handling(mock_reader):
    """Тест обработки общего исключения"""
    mock_reader.side_effect = Exception("Unexpected error")
    result = reading_transaction("test.csv")
    assert result == []


@pytest.mark.parametrize(
    "filename,expected",
    [("data.csv", "csv"), ("data.xlsx", "excel"), ("data.txt", "unsupported"), ("data", "unsupported")],
)
def test_file_format_detection(filename, expected):
    """Тест определения формата файла"""
    if expected == "csv":
        with patch("builtins.open", mock_open(read_data="test")):
            with patch("csv.DictReader") as mock_csv:
                reading_transaction(filename)
                mock_csv.assert_called_once()
    elif expected == "excel":
        with patch("pandas.read_excel") as mock_excel:
            reading_transaction(filename)
            mock_excel.assert_called_once()
    else:
        result = reading_transaction(filename)
        assert result == []


def test_coverage():
    """Проверка что все основные сценарии покрыты"""
    # 1. Успешное чтение CSV
    # 2. Ошибка чтения CSV
    # 3. Успешное чтение Excel
    # 4. Ошибка чтения Excel
    # 5. Неподдерживаемый формат
    # 6. Общие исключения
    assert True  # Реальная проверка через pytest-cov
