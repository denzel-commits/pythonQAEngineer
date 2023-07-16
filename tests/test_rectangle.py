import pytest
from mock import Mock

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


class TestRectangle:

    @pytest.mark.parametrize("side_a, side_b, expected_name", [
        (2, 4, "Rectangle"),
    ])
    def test_rectangle_name(self, side_a: int | float, side_b: int | float, expected_name: str):
        rectangle_obj = Rectangle(side_a, side_b)
        assert rectangle_obj.name == expected_name

    @pytest.mark.parametrize("side_a, side_b, expected_area, expected_perimeter", [
        (2, 4, 8, 12),
        (3, 6, 18, 18),
        (7, 8, 56, 30),
        (1, 4, 4, 10),
        (4, 1, 4, 10),
    ])
    def test_rectangle(self, side_a: int | float, side_b: int | float, expected_area: int | float,
                       expected_perimeter: int | float):
        rectangle_obj = Rectangle(side_a, side_b)
        assert rectangle_obj.area == expected_area
        assert rectangle_obj.perimeter == expected_perimeter

    @pytest.mark.parametrize("side_a, side_b", [
        (-2, 4),
        (2, -4),
        (-1, -6),
        (-5, -1),
        (0, 1),
        (1, 0),
        (1.5, 0),
        ("4", "4"),
        ("v", 4),
    ])
    def test_rectangle_negative(self, side_a: int | float, side_b: int | float):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)

    @pytest.mark.parametrize("rectangle_obj, square_obj, expected_area", [
        (Rectangle(2, 4), Square(2), 12),
        (Rectangle(3, 6), Square(4), 34),
        (Rectangle(4, 8), Square(10), 132),
    ], ids=str)
    def test_rectangle_add_square_area(self, rectangle_obj: Rectangle, square_obj: Square, expected_area: int | float):
        area = rectangle_obj.add_area(square_obj)
        assert area == expected_area

    @pytest.mark.parametrize("rectangle_obj, circle_obj, expected_area", [
        (Rectangle(2, 4), Circle(2), 20.57),
        (Rectangle(3, 6), Circle(4), 68.27),
        (Rectangle(4, 8), Circle(10), 346.16),
    ], ids=str)
    def test_rectangle_add_circle_area(self, rectangle_obj: Rectangle, circle_obj: Circle, expected_area: int | float):
        area = round(rectangle_obj.add_area(circle_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("rectangle_obj, triangle_obj, expected_area", [
        (Rectangle(2, 4), Triangle(2, 5, 6), 12.68),
        (Rectangle(3, 6), Triangle(6, 6, 6), 33.59),
        (Rectangle(4, 8), Triangle(10, 12, 10), 80),
    ], ids=str)
    def test_rectangle_add_triangle_area(self, rectangle_obj: Rectangle, triangle_obj: Triangle,
                                         expected_area: int | float):
        area = rectangle_obj.add_area(triangle_obj)
        assert area == expected_area

    @pytest.mark.parametrize("rectangle_obj, other_obj", [
        (Rectangle(2, 4), Mock()),
    ], ids=str)
    def test_rectangle_add_area_negative(self, rectangle_obj: Rectangle, other_obj: Mock):
        with pytest.raises(ValueError):
            rectangle_obj.add_area(other_obj)
