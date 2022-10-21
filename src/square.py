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

    def add_area(self, area_other_figure):
        return self.area + area_other_figure


perimeter_1 = Square(a=2)
perimeter_value = perimeter_1.perimeter
assert perimeter_value

area_1 = Square(a=2)
area_value = area_1.area
assert area_value
