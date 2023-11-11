import sys
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(*, filename: str | None = None) -> Callable:
    """Логирует вызов функции и её результат в файл или консоль"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Optional[Any], **kwargs: Optional[Any]) -> Optional[Any]:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                text = f"{time} {func.__name__} ok\n"
            except Exception:
                err_type = sys.exc_info()
                text = f"{time} {func.__name__} error {err_type[1]}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a+") as file:
                    file.write(text)
            else:
                print(text)
            return result
        return inner
    return wrapper
