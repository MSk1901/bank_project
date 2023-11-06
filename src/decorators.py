import sys
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(*, filename: str | None = None) -> Callable:
    """Логирует вызов функции и её результат в файл или консоль"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Optional[Any], **kwargs: Optional[Any]) -> None:
            time = str(datetime.now())
            if not filename:
                try:
                    result = func(*args, **kwargs)
                    text = f"{time[:-7]} {func.__name__} ok\n"
                    print(f"{result}\n{text}")
                except Exception:
                    err_type = sys.exc_info()
                    print(f"{time[:-7]} {func.__name__} error {err_type[1]}. Inputs: {args}, {kwargs}\n")
            else:
                with open(filename, "a+") as file:
                    try:
                        result = func(*args, **kwargs)
                        text = f"{time[:-7]} {func.__name__} ok\n"
                        file.write(text)
                        print(result)
                    except Exception:
                        err_type = sys.exc_info()
                        file.write(
                            f"{time[:-7]} {func.__name__} error {err_type[1]}. Inputs: {args}, {kwargs}\n")
        return inner
    return wrapper
