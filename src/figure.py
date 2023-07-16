from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, other_object: 'Figure'):
        if not isinstance(other_object, Figure):
            raise ValueError

        return self.area + other_object.area
