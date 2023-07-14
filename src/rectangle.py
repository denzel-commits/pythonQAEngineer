from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):

        if isinstance(side_a, str) or isinstance(side_b, str):
            raise ValueError

        if side_a <= 0 or side_b <= 0:
            raise ValueError

        self.name = "Rectangle"
        self._side_a = side_a
        self._side_b = side_b

    @property
    def area(self):
        return self.get_area()

    @property
    def perimeter(self):
        return self.get_perimeter()

    def get_area(self):
        return self._side_a * self._side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def __str__(self):
        return f"{self.name}(side_a={self._side_a}, side_b={self._side_b}, area={self.area}" \
               f", perimeter={self.perimeter})"
