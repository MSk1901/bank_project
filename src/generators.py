from typing import Any, Iterable
from collections import Counter


def filter_by_currency(data: list[dict], currency: str) -> Iterable[dict[str, Any]]:
    """
    Принимает список словарей data и валюту currency.
    Возвращает итератор, выдающий операции с указанной валютой.
    """
    return (x for x in data if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Iterable[str]:
    """
    Принимает список словарей transactions.
    Возвращает итератор, выдающий описания операций из словарей.
    """
    return (x["description"] for x in transactions)


def card_number_generator(start: int, end: int) -> Iterable[str]:
    """
    Принимает начальное и конечное числа start и end.
    Генерирует номера карт в указанном диапазоне и возвращает итератор.
    """
    for num in range(start, end + 1):
        number = f"{'0' * (16 - len(str(num)))}{num}"
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"


def count_categories(data: list[dict]) -> dict:
    """
    Считает количество операций по категориям
    :param data: список словарей с данными о банковских операциях
    :return: Словарь с названиями категорий и количеством операций
    """
    descriptions = transaction_descriptions(data)
    counter = dict(Counter(descriptions))
    return counter
