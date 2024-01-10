from unittest.mock import patch

import pytest
import requests

from src.utils import get_data, transaction_amount


@patch("src.utils.open")
def test_get_data_valid(mock_file):
    mock_file.return_value.__enter__.return_value.read.return_value = '[{"id": 1, "amount": 8563.45}]'
    assert get_data("mock.json") == [{"id": 1, "amount": 8563.45}]


@patch("src.utils.open")
def test_get_data_invalid_file(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "None"
    assert get_data("test.txt") == []
    mock_open.assert_called_once_with('test.txt')


@patch("src.utils.open")
def test_get_data_no_file(mock_file):
    mock_file.side_effect = FileNotFoundError
    assert get_data("mock.json") == []


def test_transaction_amount_rub(tr_list):
    assert transaction_amount(tr_list[2]) == 43318.34


@patch.object(requests, 'get')
def test_transaction_amount_usd(mock_get, tr_list):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}
    assert transaction_amount(tr_list[0]) == 982407.00


def test_transaction_amount_unsupported_currency(tr_list):
    with pytest.raises(ValueError):
        transaction_amount(tr_list[-1])
