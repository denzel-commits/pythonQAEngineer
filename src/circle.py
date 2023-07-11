from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0 or isinstance(radius, str):
            raise ValueError

        self.name = "Circle"
        self._radius = radius
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        return pi * (self._radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self._radius
