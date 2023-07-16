from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        """This property calculates the area of a figure"""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """This property calculates the perimeter of a figure"""
        pass

    def add_area(self, other_object: 'Figure') -> int | float:
        """This method adds the area of another figure to the area of the current figure.

        Parameters:
            other_object (Figure): The figure whose area must be added.

        Returns:
            int | float: sum of the areas.

        """
        if not isinstance(other_object, Figure):
            raise ValueError

        return self.area + other_object.area
