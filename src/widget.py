def make_numbers(data: str) -> str:
    """Приводит номер карты/счета в замаскированный вид"""
    if "Счет" in data:
        return f"{data[:5]}**{data[-4:]}"
    else:
        return f"{data[:-16]}{data[-16:-12]} {data[-12:-10]}** **** {data[-4:]}"
