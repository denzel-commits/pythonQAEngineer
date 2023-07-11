from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError

        if isinstance(side_a, str) or isinstance(side_b, str):
            raise ValueError

        self.name = "Rectangle"
        self._side_a = side_a
        self._side_b = side_b
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        return self._side_a * self._side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)
