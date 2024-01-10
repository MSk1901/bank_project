from unittest.mock import patch

import requests

from src.main import main


@patch.object(requests, 'get')
def test_main(mock_get, capsys):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}
    main()

    captured = capsys.readouterr()
    assert captured.out == """08.12.2019 Открытие вклада
Счет **5907
4109624.0 руб.

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
4815039.0 руб.

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
Счет **8381
21344.35 руб.

"""
