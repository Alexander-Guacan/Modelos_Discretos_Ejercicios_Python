# Import library and decorator for create an abstract class
from abc import ABC, abstractmethod

class IShape(ABC):
    """Shape interface

    Methods:
        area
        perimeter
    """

    @abstractmethod
    def area(self) -> float:
        """Returns the area of shape

        Returns:
            float: _description_ Area of shape
        """

    @abstractmethod
    def perimeter(self) -> float:
        """Returns perimeter of shape

        Returns:
            float: _description_ Perimeter of shape
        """