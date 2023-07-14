from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):

        self._validate_sides(side_a, side_b, side_c)
        self._validate_proper_triangle(side_a, side_b, side_c)

        self.name = "Triangle"

        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @staticmethod
    def _validate_sides(side_a, side_b, side_c):
        if isinstance(side_a, str) or isinstance(side_b, str) or isinstance(side_c, str):
            raise ValueError

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError

    @staticmethod
    def _validate_proper_triangle(side_a, side_b, side_c):
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError

    @property
    def area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2

        return round(((s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c)) ** 0.5), 2)

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def get_area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2

        return round(((s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c)) ** 0.5), 2)

    def get_perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def __str__(self):
        return f"{self.name}(side_a={self._side_a}, side_b={self._side_b}, side_c={self._side_c}, area={self.area}" \
               f", perimeter={self.perimeter})"
