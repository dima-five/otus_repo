
class Figure:
    PI = 3.14  # const value

    def __init__(self, name, a, b, c, d, radius, area):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.radius = radius
        self.area = area

    def add_area(self, area_other_figure, figure_obj):
        if isinstance(figure_obj, Figure):
            return self.area + area_other_figure
        else:
            raise ValueError("Object is not belonged to 'Figure' class")

