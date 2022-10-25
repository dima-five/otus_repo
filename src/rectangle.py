from src.circle import Circle
from src.main_figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b

    # def add_area(self, area_other_figure):
    #     return self.area + area_other_figure


perimeter_1 = Rectangle(a=2, b=5)
perimeter_value = perimeter_1.perimeter
assert perimeter_value

area_1 = Rectangle(a=2, b=5)
area_value = area_1.area
assert area_value

circle = Circle(radius=3)
circle_area_value = circle.area
assert circle_area_value

assert isinstance(area_1, Rectangle)

sum_two_figures = area_1.add_area(circle_area_value, circle)
assert sum_two_figures


