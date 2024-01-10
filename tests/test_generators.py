import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_result", [("USD", [939719570,
                                                                142264268,
                                                                895315941
                                                                ]),
                                                       ("RUB", [873106923])
                                                       ])
def test_filter_by_currency(tr_list, currency, expected_result):
    assert [x["id"] for x in list(filter_by_currency(tr_list, currency))] == expected_result


def test_transaction_descriptions(tr_list):
    assert list(transaction_descriptions(tr_list)) == ["Перевод организации",
                                                       "Перевод со счета на счет",
                                                       "Перевод со счета на счет",
                                                       "Перевод с карты на карту",
                                                       "Перевод организации"
                                                       ]


@pytest.mark.parametrize("start, end, expected_result", [(1, 3, ["0000 0000 0000 0001",
                                                                 "0000 0000 0000 0002",
                                                                 "0000 0000 0000 0003"]),
                                                         (1034, 1035, ["0000 0000 0000 1034",
                                                                       "0000 0000 0000 1035"]),
                                                         (9999_9999_9999_9953,
                                                          9999_9999_9999_9955, ["9999 9999 9999 9953",
                                                                                "9999 9999 9999 9954",
                                                                                "9999 9999 9999 9955"]),
                                                         ])
def test_card_number_generator(start, end, expected_result):
    assert list(card_number_generator(start, end)) == expected_result
