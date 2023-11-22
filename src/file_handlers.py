from typing import Any

import pandas as pd


def get_data_xls_csv(file: str) -> Any:
    """Получает данные из csv или xls файла"""
    if file.endswith(".csv"):
        df = pd.read_csv(file, sep=";", encoding="utf-8")
    elif file.endswith(".xls") or file.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        raise Exception("Некорректный формат файла или файл не найден")

    tr_dict = df.to_dict(orient="records")
    for tr in tr_dict:
        for k in tr.keys():
            if str(tr[k]) == "nan":
                tr[k] = None
        if tr["date"]:
            tr["date"] = tr["date"][:-1]
        tr["operationAmount"] = {"amount": tr.pop("amount"),
                                 "currency":
                                     {"name": tr.pop("currency_name"),
                                      "code": tr.pop("currency_code")}}
    return tr_dict
