from src.decorators import log


def test_log_without_filename():
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    result1 = add(1, "a")

    assert f"{result[0]}\n{result[-7:]}" == "3\nadd ok\n"
    assert "error" in result1 and "unsupported operand" in result1


def test_log_with_filename():
    @log(filename="testlog.txt")
    def add(a, b):
        return a + b

    result = add(1, 2)
    add(1, "a")

    with open("testlog.txt") as file:
        lines = file.readlines()
        line1 = lines[-2]
        line2 = lines[-1]
        assert result == 3
        assert line1[-7:] == "add ok\n"
        assert "error" in line2 and "unsupported operand" in line2
