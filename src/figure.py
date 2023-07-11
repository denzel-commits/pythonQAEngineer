from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_object: 'Figure'):
        if not isinstance(other_object, Figure):
            raise ValueError

        return self.get_area() + other_object.get_area()
