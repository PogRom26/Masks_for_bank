import pytest

from src.processing import filter_by_state, sort_by_date

# Тестирование функции фильтрации по статусу


@pytest.fixture
def start_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(start_dict_list):
    """Проверяет фильтрацию списка по заданному ключу"""

    assert filter_by_state(start_dict_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_without_state():
    """Проверяет фильтрацию списка без ключа по умолчанию или без списка вообще"""

    assert (
        filter_by_state(
            [
                {"id": 41428829, "stated": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "stated": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "stated": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "stated": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == []
    )


def test_filter_by_state_with_another_key(start_dict_list):
    """Проверяет работу фильтрации с нестандартным ключом "CANCELED" """

    assert filter_by_state(start_dict_list, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Тестирование функции фильтрации по времени
def test_sort_by_date(start_dict_list):
    """Проверяем сортировку по умолчанию (по убыванию)"""

    assert sort_by_date(start_dict_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_with_reverse(start_dict_list):
    """Проверяем сортировку по возрастанию"""

    assert sort_by_date(start_dict_list, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
