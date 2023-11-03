import json


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
