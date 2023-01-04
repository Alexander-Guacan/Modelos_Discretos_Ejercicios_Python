from abc import ABC, abstractmethod

class IShape(ABC):
    """Shape interface

    Methods:
        area
        perimeter
    """

    @abstractmethod
    def area(self) -> float:
        """_summary_ Returns the area of shape

        Returns:
            float: _description_ Area of shape
        """

    @abstractmethod
    def perimeter(self) -> float:
        """_summary_ Returns perimeter of shape

        Returns:
            float: _description_ Perimeter of shape
        """