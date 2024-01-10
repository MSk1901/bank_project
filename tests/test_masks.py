import pytest

from src.masks import mask_account_number, mask_card_number


def test_mask_card_number():
    assert mask_card_number("1596837868705199") == "1596 83** **** 5199"
    with pytest.raises(ValueError):
        assert mask_card_number("1234") == "Некорректный номер карты"


def test_mask_account_number():
    assert mask_account_number("35383033474447895560") == "**5560"
    with pytest.raises(ValueError):
        assert mask_account_number("1234") == "Некорректный номер счета"
