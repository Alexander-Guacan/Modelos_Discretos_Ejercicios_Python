from abc import ABC, abstractmethod

class Trapezoid(ABC):
    """Trapezoid object

    Methods:
        area
    """

    _angle: float

    @abstractmethod
    def area(self) -> float:
        """_summary_ Calculates the area of Trapezoid

        Returns:
            float: _description_ Area of trapezoid
        """