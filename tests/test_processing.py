from conftest import list_dicts
from src.processing import sort_by_date, sort_by_state


def test_sort_by_state(list_dicts):
    assert sort_by_state(list_dicts) == [{"id": 1, "state": "EXECUTED", "date": "2020-10-30"},
                                         {"id": 3, "state": "EXECUTED", "date": "2018-06-12"}]
    assert sort_by_state(list_dicts, "CANCELED") == [{"id": 2, "state": "CANCELED", "date": "2023-12-01"}]


def test_sort_by_date(list_dicts):
    assert sort_by_date(list_dicts) == [{"id": 2, "state": "CANCELED", "date": "2023-12-01"},
                                        {"id": 1, "state": "EXECUTED", "date": "2020-10-30"},
                                        {"id": 3, "state": "EXECUTED", "date": "2018-06-12"}
                                        ]
    assert sort_by_date(list_dicts, False) == [{"id": 3, "state": "EXECUTED", "date": "2018-06-12"},
                                               {"id": 1, "state": "EXECUTED", "date": "2020-10-30"},
                                               {"id": 2, "state": "CANCELED", "date": "2023-12-01"}
                                               ]
