import re


def sort_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Фильтрует список словарей и возвращает только те значения, где ключ "state" совпадает с заданным """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reversion: bool = True) -> list[dict]:
    """Сортирует список по дате (по умолчанию в начале более новые)"""
    return sorted(data, key=lambda x: x['date'], reverse=reversion)


def filter_by_description(data: list[dict], sample: str) -> list:
    """
    Фильтрует список по описанию операции
    :param data: список словарей с данными о банковских операциях
    :param sample: Строка, по которой будет фильтроваться список
    :return: Список словарей, в которых в описании есть заданная строка
    """
    return [x for x in data if re.search(sample, x["description"], flags=re.I)]
