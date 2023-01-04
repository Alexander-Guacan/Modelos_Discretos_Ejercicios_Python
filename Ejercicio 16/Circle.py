# Import math library for PI value and trigonometric functions
import math

class Circle:
    """Geometric figure delimited by a circumference

    Attributes:
        __radius: float
        

    Methods:
        area
        perimeter
        diameter

    """

    __radius: float

    def __init__(self, radius: float) -> None:
        """Default constructor

        Args:
            radius (float): _description_ Radius of circle
        """
        # Initializes attributes
        self.__radius = radius

    def area(self) -> float:
        """Returns the area measure

        Returns:
            float: _description_ area
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self) -> float:
        """Returns the perimeter

        Returns:
            float: _description_ perimeter
        """
        return 2 * math.pi * self.__radius
    
    def diameter(self) -> float:
        """Returns the diameter

        Returns:
            float: _description_ diameter
        """
        return 2 * self.__radius