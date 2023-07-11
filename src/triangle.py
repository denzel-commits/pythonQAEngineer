from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError

        if isinstance(side_a, str) or isinstance(side_b, str) or isinstance(side_c, str):
            raise ValueError

        self.name = "Triangle"

        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2

        return (s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c)) ** 0.5

    def get_perimeter(self):
        return self._side_a + self._side_b + self._side_c
