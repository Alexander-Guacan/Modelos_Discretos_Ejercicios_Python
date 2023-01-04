# Importing IShape interface
from IShape import IShape

class Rectangle(IShape):
    """Rectangle class that can calculates him area and perimeters

    Attributes:
        base: float
        height: float

    Methods:
        __init__
        area        
        perimeter
    """

    __base: float
    __height: float

    def __init__(self, base: float, height: float) -> None:
        """Default constructor

        Args:
            base (float): _description_ Base measure of rectangle
            height (float): _description_ Height measure of rectangle
        """

        # Initializing attributes
        self.__base = base
        self.__height = height

    def area(self) -> float:
        """Calculates area of rectangle

        Returns:
            float: _description_ Area of rectangle
        """
        return self.__base * self.__height

    def perimeter(self) -> float:
        """Calculates perimeter of rectangle

        Returns:
            float: _description_ Perimeter of rectangle
        """
        return 2 * (self.__base + self.__height)