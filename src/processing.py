def sort_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Фильтрует список словарей и возвращает только те значения, где ключ "state" совпадает с заданным """
    return [item for item in data if item.get("state") == state]
