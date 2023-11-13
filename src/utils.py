import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_data(filename: str) -> Any:
    """Получает данные из json файла если он существует и в нем хранятся корректные данные"""
    try:
        with open(filename) as file:
            data = file.read()
            if not data or not data.startswith("["):
                return []
            else:
                with open(filename) as f:
                    data_json = json.load(f)
                    return data_json
    except FileNotFoundError:
        return []


def transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях,
    при необходимости конвертируя другую валюту в рубли"""

    currency = transaction["operationAmount"]["currency"]["code"]
    date = transaction["date"][:10]
    if currency == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif currency == "USD" or currency == "EUR":
        load_dotenv()
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        if api_key is None:
            raise ValueError("Нет ключа API")
        try:
            url = f"https://api.apilayer.com/exchangerates_data/{date}?base={currency}"
            response = requests.get(url, headers={'apikey': api_key})
            response.raise_for_status()
            response_data = response.json()
            rate = response_data["rates"]["RUB"]

            amount: float = float(transaction["operationAmount"]["amount"]) * rate
            return round(amount, 2)
        except (requests.exceptions.HTTPError, ValueError, KeyError):
            raise ValueError("Что-то пошло не так")
    else:
        raise ValueError("Некорректная валюта")
