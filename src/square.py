from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        self.name = "Square"

        super().__init__(side_a, side_a)
