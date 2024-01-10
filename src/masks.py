import logging
import os

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log")

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(PATH_TO_FILE, "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def mask_card_number(number: str) -> str:
    """Приводит номер карты в замаскированный вид"""
    if len(number) == 16:
        logger.debug("Передан корректный номер карты")
        return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    logger.error("Передан некорректный номер карты")
    raise ValueError("Некорректный номер карты")


def mask_account_number(number: str) -> str:
    """Приводит номер счета в замаскированный вид"""
    if len(number) == 20:
        logger.debug("Передан корректный номер счета")
        return f"**{number[-4:]}"
    logger.error("Передан некорректный номер счета")
    raise ValueError("Некорректный номер счета")
