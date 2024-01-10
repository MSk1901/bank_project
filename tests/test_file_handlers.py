from unittest.mock import patch

import pytest

from src.file_handlers import get_data_xls_csv


@patch("src.file_handlers.pd.read_csv")
def test_csv(mock_read_csv, dataframe_valid, dataframe_invalid):
    mock_read_csv.return_value = dataframe_valid
    assert get_data_xls_csv("mock.csv") == [{"date": "2023-09-05T11:30:32",
                                             'operationAmount': {'amount': '26165.0',
                                                                 'currency': {'name': 'rubles',
                                                                              'code': 'RUB'}}}]
    mock_read_csv.return_value = dataframe_invalid
    assert get_data_xls_csv("mock.csv") == [{"date": None,
                                             "from": None,
                                             'operationAmount': {'amount': '26165.0',
                                                                 'currency': {'name': 'rubles',
                                                                              'code': 'RUB'}}}]


@patch("src.file_handlers.pd.read_excel")
def test_excel(mock_read_excel, dataframe_valid, dataframe_invalid):
    mock_read_excel.return_value = dataframe_valid
    assert get_data_xls_csv("mock.xls") == [{"date": "2023-09-05T11:30:32",
                                             'operationAmount': {'amount': '26165.0',
                                                                 'currency': {'name': 'rubles',
                                                                              'code': 'RUB'}}}]
    mock_read_excel.return_value = dataframe_invalid
    assert get_data_xls_csv("mock.xls") == [{"date": None,
                                             "from": None,
                                             'operationAmount': {'amount': '26165.0',
                                                                 'currency': {'name': 'rubles',
                                                                              'code': 'RUB'}}}]


def test_invalid_file():
    with pytest.raises(Exception):
        assert get_data_xls_csv("1234.csv") == "Некорректный формат файла или файл не найден"
        assert get_data_xls_csv("1234.txt") == "Некорректный формат файла или файл не найден"
