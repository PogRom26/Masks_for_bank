import os
from unittest.mock import MagicMock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_currency_rate  # Импортируем тестируемую функцию


# Фикстура для загрузки .env
@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_successful_conversion():
    """Тест успешного конвертирования валют"""
    test_data = {"success": True, "result": 85.42}

    with patch("requests.request") as mock_request:
        # Настраиваем мок ответа
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_data
        mock_request.return_value = mock_response

        # Вызываем тестируемую функцию
        result = get_currency_rate("EUR", "USD", 100)

        # Проверяем результаты
        assert result == 85.42
        mock_request.assert_called_once_with(
            "GET",
            "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=USD&amount=100",
            headers={"apikey": os.getenv("API_KEY")},
        )


def test_api_error_response():
    """Тест обработки ошибки API"""
    with patch("requests.request") as mock_request:
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.reason = "Invalid currency"
        mock_request.return_value = mock_response

        result = get_currency_rate("INVALID", "USD", 100)
        assert result == "Invalid currency"


@pytest.mark.parametrize(
    "from_curr,to_curr,amount,expected",
    [("USD", "EUR", 100, 85.42), ("EUR", "USD", 100, 117.50), ("GBP", "JPY", 50, 7500.00)],
)
def test_different_currencies(from_curr, to_curr, amount, expected):
    """Тест разных валютных пар"""
    test_data = {"success": True, "result": expected}

    with patch("requests.request") as mock_request:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_data
        mock_request.return_value = mock_response

        result = get_currency_rate(to_curr, from_curr, amount)
        assert result == expected
