import pytest

from src.circle import Circle
from src.square import Square
from src.rectangle import Rectangle
from src.triangle import TriangleFigure

"_____________________________square_______________________"


@pytest.mark.parametrize("value", [0, 1, -3, 5])
def test_square_initial_negative_value_and_get_area(value):

    if value < 1:
        raise AssertionError(f"{value} is negative or 'zero'")
    else:
        square_value = Square(value)
        square_area = square_value.area
        assert square_area


@pytest.mark.parametrize("value", [0, 1, -3, 5])
def test_square_initial_negative_value_and_get_perimeter(value):

    if value < 1:
        raise AssertionError(f"{value} is negative or 'zero'")
    else:
        square_value = Square(value)
        square_perimeter = square_value.perimeter
        assert square_perimeter


"_____________________________rectangle_______________________"


def test_rectangle_initial_negative_value_and_get_area():

    def verify_value_get_area(value_1, value_2):
        if value_1 > 0 and value_2 > 0:
            rectangle_value = Rectangle(value_1, value_2)
            rectangle_area = rectangle_value.area
            assert rectangle_area
        else:
            raise AssertionError(f"{value_1} or {value_2} value < 1")

    verify_value_get_area(2, 5)
    verify_value_get_area(-3, 5)


def test_rectangle_initial_negative_value_and_get_perimeter():

    def verify_value_get_perimeter(value_1, value_2):
        if value_1 > 0 and value_2 > 0:
            rectangle_value = Rectangle(value_1, value_2)
            rectangle_perimeter = rectangle_value.perimeter
            assert rectangle_perimeter
        else:
            raise AssertionError(f"{value_1} or {value_2} value < 1")

    verify_value_get_perimeter(2, 5)
    verify_value_get_perimeter(-2, 5)


"_____________________________triangle_______________________"


def test_triangle_initial_negative_value_and_get_area():

    def verify_value_get_area(value_1, value_2, value_3):
        if value_1 > 0 and value_2 > 0 and value_3 > 0:
            if value_1 + value_2 > value_3:
                triangle_value = TriangleFigure(value_1, value_2, value_3)
                triangle_area = triangle_value.area
                assert triangle_area
            else:
                raise AssertionError(f"SUM of '{value_1}' + value '{value_2}' value < '{value_3}'")
        else:
            raise AssertionError(f"'{value_1}' or '{value_2}' or '{value_3}' are negative or zero")

    verify_value_get_area(3, 5, 6)
    verify_value_get_area(-4, 5, 6)


def test_triangle_initial_negative_value_and_get_perimeter():
    def verify_value_get_perimeter(value_1, value_2, value_3):
        if value_1 > 0 and value_2 > 0 and value_3 > 0:
            if value_1 + value_2 > value_3:
                triangle_value = TriangleFigure(value_1, value_2, value_3)
                triangle_perimeter = triangle_value.perimeter
                assert triangle_perimeter
            else:
                raise AssertionError(f"SUM of '{value_1}' + value '{value_2}' value < '{value_3}'")
        else:
            raise AssertionError(f"'{value_1}' or '{value_2}' or '{value_3}' are negative or zero")

    verify_value_get_perimeter(3, 5, 6)
    verify_value_get_perimeter(-4, 5, 6)


"_____________________________circle_______________________"


@pytest.mark.parametrize("radius", [0, -1, 5, 7])
def test_circle_initial_negative_value_and_get_area(radius):

    if radius < 1:
        raise AssertionError(f"{radius} is negative or 'zero'")
    else:
        circle_value = Circle(radius)
        circle_area = circle_value.area
        assert circle_area


@pytest.mark.parametrize("radius", [0, -1, 5, 7])
def test_circle_initial_negative_value_and_get_perimeter(radius):
    if radius < 1:
        raise AssertionError(f"{radius} is negative or 'zero'")
    else:
        circle_value = Circle(radius)
        circle_perimeter = circle_value.perimeter
        assert circle_perimeter
