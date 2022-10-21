from src.main_figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a
        self.d = b

    @property
    def perimeter(self):
        if self.a == self.c and self.b == self.d:
            return 2 * (self.a + self.b)
        else:
            return "It is not rectangle"

    @property
    def area(self):
        if self.a == self.c and self.b == self.d:
            return self.a * self.b

    def add_area(self, area_other_figure):
        return self.area + area_other_figure


perimeter_1 = Rectangle(a=2, b=5)
perimeter_value = perimeter_1.perimeter
assert perimeter_value

area_1 = Rectangle(a=2, b=5)
area_value = area_1.area
assert area_value

