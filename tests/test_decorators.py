from datetime import datetime

from src.decorators import log


def test_log_without_filename_positive(capsys):
    @log()
    def add(a, b):
        return a + b

    date = str(datetime.now())
    result = add(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert captured.out.strip() == f"{date[:-7]} add ok"


def test_log_without_filename_negative(capsys):
    @log()
    def add(a, b):
        return a + b

    date = str(datetime.now())
    add(1, "a")
    captured = capsys.readouterr()

    assert captured.out.strip() == (
            f"{date[:-7]}" + " add error unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'a'), {}")


def test_log_with_filename_positive(capsys):
    @log(filename="testlog.txt")
    def add(a, b):
        return a + b

    date = str(datetime.now())

    assert add(1, 2) == 3

    with open("testlog.txt") as file:
        lines = file.readlines()
        line = lines[-1]

        assert line.strip() == f"{date[:-7]} add ok"


def test_log_with_filename_negative():
    @log(filename="testlog.txt")
    def add(a, b):
        return a + b

    date = str(datetime.now())
    add(1, "a")

    with open("testlog.txt") as file:
        lines = file.readlines()
        line = lines[-1]

        assert line.strip() == (
            f"{date[:-7]}" + " add error unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'a'), {}")
