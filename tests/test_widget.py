import pytest

from src.widget import make_numbers, fix_date


@pytest.mark.parametrize("data, expected_result", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                   ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                   ("Счет 73654108430135874305", "Счет **4305")
                                                   ])
def test_make_numbers(data, expected_result):
    assert make_numbers(data) == expected_result


@pytest.mark.parametrize("data, expected_result", [("2018-07-11T02:26:18.671407", "11.07.2018"),
                                                   ("2000-01-05T04:28:56.671407", "05.01.2000"),
                                                   ("2003-12-26T12:46:01.671407", "26.12.2003")
                                                   ])
def test_fix_date(data, expected_result):
    assert fix_date(data) == expected_result
