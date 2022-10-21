import pytest

default_size = 3


def test_example():
    pass


def test_example_1():
    assert 1 + 3 == 4

# def test_example_2():
#     raise AssertionError


@pytest.mark.parametrize("value", [0, 1, -3, -5])
def test_initial_negative_value(value):
    list_1 = []
    if value < 0:
        list_1.append(value)
    print(list_1)


@pytest.fixture()
def database():
    browser = default_size

    yield browser  # 'yield' method is the same that 'return' meth. But We can invoke other method after 'yield'

    database.rm_cache()
