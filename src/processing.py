def sort_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Фильтрует список словарей и возвращает только те значения, где ключ "state" совпадает с заданным """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reversion: bool = True) -> list[dict]:
    """Сортирует список по дате (по умолчанию в начале более новые)"""
    return sorted(data, key=lambda x: x['date'], reverse=reversion)
