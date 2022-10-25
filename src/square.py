from src.circle import Circle
from src.main_figure import Figure


class Square(Figure):
    area_value = 0

    def __init__(self, a):
        self.a = a

    @property
    def perimeter(self):
        return 4 * self.a

    @property
    def area(self):
        return self.a**2


perimeter_1 = Square(a=2)
perimeter_value = perimeter_1.perimeter
assert perimeter_value

area_1 = Square(a=2)
area_value = area_1.area
assert area_value

circle = Circle(radius=3)
circle_area_value = circle.area
assert circle_area_value

sum_two_figures = area_1.add_area(circle_area_value, circle)
assert sum_two_figures
