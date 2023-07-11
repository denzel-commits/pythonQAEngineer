import pytest
from mock import Mock
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle


class TestSquare:
    @pytest.mark.parametrize("side_a, expected_name", [
        (2, "Square"),
    ])
    def test_square_name(self, side_a, expected_name):
        square_obj = Square(side_a)
        assert square_obj.name == expected_name

    @pytest.mark.parametrize("side_a, expected_area, expected_perimeter", [
        (2, 4, 8),
        (3, 9, 12),
        (7, 49, 28),
    ])
    def test_square(self, side_a, expected_area, expected_perimeter):
        square_obj = Square(side_a)
        assert square_obj.area == expected_area
        assert square_obj.perimeter == expected_perimeter

    @pytest.mark.parametrize("side_a", [-2, -4, 0, "o"])
    def test_square_negative(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)

    @pytest.mark.parametrize("square_obj, rectangle_obj, expected_area", [
        (Square(2), Rectangle(2, 4), 12),
        (Square(4), Rectangle(3, 6), 34),
        (Square(10), Rectangle(4, 8), 132),
    ], ids=str)
    def test_square_add_rectangle_area(self, square_obj, rectangle_obj, expected_area):
        area = square_obj.add_area(rectangle_obj)
        assert area == expected_area

    @pytest.mark.parametrize("square_obj, circle_obj, expected_area", [
        (Square(2), Circle(2), 16.57),
        (Square(4), Circle(4), 66.27),
        (Square(10), Circle(10), 414.16),
    ], ids=str)
    def test_square_add_circle_area(self, square_obj, circle_obj, expected_area):
        area = round(square_obj.add_area(circle_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("square_obj, triangle_obj, expected_area", [
        (Square(2), Triangle(2, 5, 6), 8.68),
        (Square(4), Triangle(6, 6, 6), 31.59),
        (Square(10), Triangle(10, 12, 10), 148),
    ], ids=str)
    def test_square_add_triangle_area(self, square_obj, triangle_obj, expected_area):
        area = square_obj.add_area(triangle_obj)
        assert area == expected_area

    @pytest.mark.parametrize("square_obj, other_obj", [
        (Square(4), Mock()),
    ], ids=str)
    def test_square_add_area_negative(self, square_obj, other_obj):
        with pytest.raises(ValueError):
            square_obj.add_area(other_obj)
