import pytest
from mock import Mock
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle


class TestCircle:
    @pytest.mark.parametrize("radius, expected_name", [
        (3, "Circle"),
    ])
    def test_circle_name(self, radius, expected_name):
        circle_obj = Circle(radius)
        assert circle_obj.name == expected_name

    @pytest.mark.parametrize("radius, expected_area, expected_perimeter", [
        (13, 530.93, 81.68),
        (5, 78.54, 31.42),
        (7, 153.94, 43.98),
        (3.5, 38.48, 21.99),
    ])
    def test_circle(self, radius, expected_area, expected_perimeter):
        circle_obj = Circle(radius)
        assert circle_obj.area == expected_area
        assert circle_obj.perimeter == expected_perimeter

    @pytest.mark.parametrize("radius", [-1, 0, "3"])
    def test_circle_negative(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize("circle_obj, rectangle_obj, expected_area", [
        (Circle(2), Rectangle(2, 4), 20.57),
        (Circle(4), Rectangle(3, 6), 68.27),
        (Circle(10), Rectangle(4, 8), 346.16),
    ], ids=str)
    def test_circle_add_rectangle_area(self, circle_obj, rectangle_obj, expected_area):
        area = round(circle_obj.add_area(rectangle_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("circle_obj, triangle_obj, expected_area", [
        (Circle(2), Triangle(13, 14, 15), 96.57),
        (Circle(4), Triangle(5, 5, 5), 61.1),
        (Circle(10), Triangle(3.5, 3.5, 3.5), 319.46),
    ], ids=str)
    def test_circle_add_triangle_area(self, circle_obj, triangle_obj, expected_area):
        area = round(circle_obj.add_area(triangle_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("circle_obj, square_obj, expected_area", [
        (Circle(2), Square(2), 16.57),
        (Circle(4), Square(4), 66.27),
        (Circle(10), Square(10), 414.16),
    ], ids=str)
    def test_circle_add_square_area(self, circle_obj, square_obj, expected_area):
        area = round(circle_obj.add_area(square_obj), 2)
        assert area == expected_area

    @pytest.mark.parametrize("circle_obj, other_obj", [
        (Circle(13), Mock()),
    ], ids=str)
    def test_circle_add_area_negative(self, circle_obj, other_obj):
        with pytest.raises(ValueError):
            circle_obj.add_area(other_obj)
