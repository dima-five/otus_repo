from src.main_figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * self.PI * self.radius

    @property
    def area(self):
        return 2 * (self.PI * self.radius ** 2)


perimeter_1 = Circle(radius=3)
perimeter_value = perimeter_1.perimeter
assert perimeter_value

area_1 = Circle(radius=3)
area_value = area_1.area
assert area_value
