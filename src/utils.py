import json
import os
import requests
from dotenv import load_dotenv


def get_data(filename: str) -> list[dict]:
    """Получает данные из json файла если он существует и в нем хранятся корректные данные"""
    try:
        with open(filename) as file:
            data = file.read()
            if not data or not data.startswith("["):
                return []
            else:
                with open(filename) as f:
                    data = json.load(f)
                    return data
    except FileNotFoundError:
        return []


def transaction_amount(transaction: dict) -> float | str:
    """Возвращает сумму транзакции в рублях,
    при необходимости конвертируя другую валюту в рубли"""

    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif currency == "USD" or currency == "EUR":
        try:
            load_dotenv()
            API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

            url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
            response = requests.get(url, headers={'apikey': API_KEY})
            response.raise_for_status()
            response_data = response.json()
            rate = response_data["rates"]["RUB"]

            amount = float(transaction["operationAmount"]["amount"]) * rate
            return round(amount, 2)
        except (requests.exceptions.HTTPError, ValueError, KeyError):
            raise ValueError("Что-то пошло не так")
    else:
        raise ValueError("Некорректная валюта")
