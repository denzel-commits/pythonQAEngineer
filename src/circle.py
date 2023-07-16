from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius: int | float) -> None:
        if isinstance(radius, str) or radius <= 0:
            raise ValueError

        self.name = "Circle"
        self._radius = radius

    @property
    def area(self) -> int | float:
        return round(pi * (self._radius ** 2), 2)

    @property
    def perimeter(self) -> int | float:
        return round(2 * pi * self._radius, 2)

    def __str__(self) -> str:
        return f"{self.name}(radius={self._radius}, area={self.area}, perimeter={self.perimeter})"
