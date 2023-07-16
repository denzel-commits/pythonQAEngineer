from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float) -> None:

        self._validate_sides(side_a, side_b, side_c)
        self._validate_proper_triangle(side_a, side_b, side_c)

        self.name = "Triangle"

        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @staticmethod
    def _validate_sides(side_a: int | float, side_b: int | float, side_c: int | float) -> None:
        """Validates that the sides are positive numbers"""
        if isinstance(side_a, str) or isinstance(side_b, str) or isinstance(side_c, str):
            raise ValueError

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError

    @staticmethod
    def _validate_proper_triangle(side_a: int | float, side_b: int | float, side_c: int | float) -> None:
        """Validates that creation of triangle is possible"""
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError

    @property
    def area(self) -> int | float:
        s = (self._side_a + self._side_b + self._side_c) / 2

        return round(((s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c)) ** 0.5), 2)

    @property
    def perimeter(self) -> int | float:
        return self._side_a + self._side_b + self._side_c

    def __str__(self) -> str:
        return f"{self.name}(side_a={self._side_a}, side_b={self._side_b}, side_c={self._side_c}, area={self.area}" \
               f", perimeter={self.perimeter})"
