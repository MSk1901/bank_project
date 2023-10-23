def mask_card_number(number: str) -> str:
    """Приводит номер карты в замаскированный вид"""
    if len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    return "Некорректный номер карты"


def mask_account_number(number: str) -> str:
    """Приводит номер счета в замаскированный вид"""
    if len(number) == 20:
        return f"**{number[-4:]}"
    return "Некорректный номер счета"
