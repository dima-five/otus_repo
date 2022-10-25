from math import sqrt

from src.circle import Circle
from src.main_figure import Figure


class TriangleFigure(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))


perimeter = TriangleFigure(a=5, b=3, c=7)
perimeter_value = perimeter.perimeter
assert perimeter_value

triangle = TriangleFigure(a=5, b=3, c=7)
area_value = triangle.area
assert area_value

circle = Circle(radius=3)
circle_area_value = circle.area
assert circle_area_value

sum_two_figures = triangle.add_area(circle_area_value, circle)
assert sum_two_figures
