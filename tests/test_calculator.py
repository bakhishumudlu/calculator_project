from calculator.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(27, 3) == 9




