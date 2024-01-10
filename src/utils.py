import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")


logger = logging.getLogger("utils")
file_handler = logging.FileHandler(PATH_TO_FILE, "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_data(filename: str) -> Any:
    """Получает данные из json файла если он существует и в нем хранятся корректные данные"""
    try:
        with open(filename) as f:
            data = json.load(f)
            logger.debug(f"Данные успешно загружены из файла {filename}")
            return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(e)
        return []


def transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях,
    при необходимости конвертируя другую валюту в рубли"""

    currency = transaction["operationAmount"]["currency"]["code"]
    date = transaction["date"][:10]
    if currency == "RUB":
        logger.debug("Получили сумму транзакции в рублях")
        return float(transaction["operationAmount"]["amount"])

    elif currency == "USD" or currency == "EUR":
        load_dotenv()
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")

        if api_key is None:
            logger.error("Нет ключа API")
            raise ValueError("Нет ключа API")

        try:
            url = f"https://api.apilayer.com/exchangerates_data/{date}?base={currency}"
            response = requests.get(url, headers={'apikey': api_key})
            response.raise_for_status()
            response_data = response.json()
            rate = response_data["rates"]["RUB"]

            amount: float = float(transaction["operationAmount"]["amount"]) * rate

            logger.debug(f"Сконвертировали {currency} в рубли c помощью внешнего API")
            return round(amount, 2)

        except (requests.exceptions.HTTPError, ValueError, KeyError) as e:
            logger.error(e)
            raise ValueError("Что-то пошло не так")
    else:
        logger.error(f"Передана некорректная валюта: {currency}")
        raise ValueError("Некорректная валюта")
