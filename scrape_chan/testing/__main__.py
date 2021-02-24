def add(x, y):
    return x + y


def test_add():
    assert add(2, 9) == 11


def sub(x, y):
    return x + y


def test_sub():
    assert sub(2, 2) == 0

test_add()
test_sub()