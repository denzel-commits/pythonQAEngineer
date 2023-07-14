from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        if isinstance(radius, str) or radius <= 0:
            raise ValueError

        self.name = "Circle"
        self._radius = radius

    @property
    def area(self):
        return round(pi * (self._radius ** 2), 2)

    @property
    def perimeter(self):
        return round(2 * pi * self._radius, 2)

    def get_area(self):
        return round(pi * (self._radius ** 2), 2)

    def get_perimeter(self):
        return round(2 * pi * self._radius, 2)

    def __str__(self):
        return f"{self.name}(radius={self._radius}, area={self.area}, perimeter={self.perimeter})"
