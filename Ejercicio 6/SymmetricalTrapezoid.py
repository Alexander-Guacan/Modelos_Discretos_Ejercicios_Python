# Import trapezoid class
from Trapezoid import Trapezoid
# Import math library
import math

class SymmetricalTrapezoid(Trapezoid):
    """A trapezoid is called symmetrical when its consecutive sides are of equal size

    Attributes:
        __diagonal_A: float
        __diagonal_B: float
        __area: float

    Methods:
        constructor_diagonal
        constructor_sides_angle
        area
    """
    __diagonal_A: float
    __diagonal_B: float
    __area: float
        

    @classmethod
    def constructor_diagonals(cls, main_diagonal: float, secondary_diagonal: float):
        """Creates a symmetrical trapezoid object

        Args:
            main_diagonal (float): _description_ main diagonal measure
            secondary_diagonal (float): _description_ secondary diagonal measure

        Returns:
            _type_: _description_ Symmetrical trapezoid object
        """
        # Creates a new instance of symmetrical trapezoid class
        symmetrical_trapezoid = cls.__new__(cls)

        # Initializes attributes
        symmetrical_trapezoid.__diagonal_A = main_diagonal
        symmetrical_trapezoid.__diagonal_B = secondary_diagonal
        symmetrical_trapezoid.__area = symmetrical_trapezoid.__diagonal_A * symmetrical_trapezoid.__diagonal_B / 2

        return symmetrical_trapezoid

    @classmethod
    def constructor_sides_angle(cls, side_A: float, side_B: float, angle: float):
        """Creates a symmetrical trapezoid object

        Args:
            side_A (float): _description_ Any side of trapezoid
            side_B (float): _description_ Side adjacent to side_A that is uneven
            angle (float): _description_ Angle between side_A and side_B in radian

        Returns:
            _type_: _description_ Symmetrical trapzeoid object
        """
        # Creates a new instance of symmetrical trapezoid class
        symmetrical_trapezoid = cls.__new__(cls)

        # Initializes attributes
        symmetrical_trapezoid._angle = angle
        symmetrical_trapezoid.__area = side_A * side_B * math.sin(angle)

        return symmetrical_trapezoid

    def area(self) -> float:
        """Returns the area of trapezoid

        Returns:
            float: _description_ Area measure
        """
        return self.__area