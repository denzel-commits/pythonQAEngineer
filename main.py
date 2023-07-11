from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


def print_hi(text: str):
    """Function prints text.

    Parameters:
    text (str) -- text to print
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'{text}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello world')

    square_obj = Square(4)
    rectangle_obj = Rectangle(2, 4)
    circle_obj = Circle(4)
    triangle_obj = Triangle(4, 5, 7)

    print('perimeter = ', square_obj.perimeter)
    print('area = ', square_obj.area)

    print('circle perimeter = ', circle_obj.perimeter)
    print('circle area = ', circle_obj.area)

    print('triangle perimeter = ', triangle_obj.perimeter)
    print('triangle area = ', triangle_obj.area)

    print('add area = ', square_obj.add_area(rectangle_obj))
