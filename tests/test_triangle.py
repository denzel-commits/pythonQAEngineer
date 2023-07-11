import pytest
from mock import Mock
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize("side_a, side_b, side_c, expected_name", [
        (1, 2, 3, "Triangle"),
    ])
    def test_triangle_name(self, side_a, side_b, side_c, expected_name):
        triangle_obj = Triangle(side_a, side_b, side_c)
        assert triangle_obj.name == expected_name

    @pytest.mark.parametrize("side_a, side_b, side_c, expected_area, expected_perimeter", [
        (13, 14, 15, 84, 42),
        (5, 5, 5, 10.83, 15),
        (7, 12, 12, 40.17, 31),
        (3.5, 3.5, 3.5, 5.3, 10.5),
    ])
    def test_triangle(self, side_a, side_b, side_c, expected_area, expected_perimeter):
        triangle_obj = Triangle(side_a, side_b, side_c)
        assert triangle_obj.area == expected_area
        assert triangle_obj.perimeter == expected_perimeter

    @pytest.mark.parametrize("side_a, side_b, side_c", [
        (-13, 14, 15),
        (3, -9, 12),
        (7, 9, -28),
        (7, 9, 0),
        (0, 0, 0),
        (1, 1, -1),
        (1, "1", 1),
    ])
    def test_triangle_negative(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize("triangle_obj, rectangle_obj, expected_area", [
        (Triangle(2, 5, 6), Rectangle(2, 4), 12.68),
        (Triangle(6, 6, 6), Rectangle(3, 6), 33.59),
        (Triangle(10, 12, 10), Rectangle(4, 8), 80),
    ], ids=str)
    def test_triangle_add_rectangle_area(self, triangle_obj, rectangle_obj, expected_area):
        area = triangle_obj.add_area(rectangle_obj)
        assert area == expected_area

    @pytest.mark.parametrize("triangle_obj, circle_obj, expected_area", [
        (Triangle(13, 14, 15), Circle(2), 96.57),
        (Triangle(5, 5, 5), Circle(4), 61.1),
        (Triangle(3.5, 3.5, 3.5), Circle(10), 319.46),
    ], ids=str)
    def test_triangle_add_circle_area(self, triangle_obj, circle_obj, expected_area):
        area = round(triangle_obj.add_area(circle_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("square_obj, triangle_obj, expected_area", [
        (Triangle(2, 5, 6), Square(2), 8.68),
        (Triangle(6, 6, 6), Square(4), 31.59),
        (Triangle(10, 12, 10), Square(10), 148),
    ], ids=str)
    def test_triangle_add_square_area(self, triangle_obj, square_obj, expected_area):
        area = triangle_obj.add_area(square_obj)
        assert area == expected_area

    @pytest.mark.parametrize("triangle_obj, other_obj", [
        (Triangle(13, 14, 15), Mock()),
    ], ids=str)
    def test_triangle_add_area_negative(self, triangle_obj, other_obj):
        with pytest.raises(ValueError):
            triangle_obj.add_area(other_obj)
