from datetime import datetime

from src.masks import mask_card_number, mask_account_number


def make_numbers(data: str) -> str:
    """Получает на вход строку и возвращает номер карты/счета с замаскированным значением"""
    data_split = data.split(" ")
    name = " ".join(data_split[:-1])
    if len(data_split[-1]) == 16:
        masked_number = mask_card_number(data_split[-1])
    else:
        masked_number = mask_account_number(data_split[-1])
    return f"{name} {masked_number}"


def fix_date(date: str) -> str:
    """Приводит дату в нужный вид"""
    thedate = datetime.fromisoformat(date)
    return thedate.strftime("%d.%m.%Y")
