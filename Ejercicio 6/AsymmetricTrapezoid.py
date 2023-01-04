from Trapezoid import Trapezoid
from Triangle import Triangle
import math

class AsymmetricTrapezoid(Trapezoid):
    """They are quadrilaterals that have neither parallel sides nor axis of symmetry.
    
    Attributes:
        __triangle_A: Triangle
        __triangle_B: Triangle
        
    Methods:
        constructor_direct
        constructor_triangle
        constructor_sides_angle
        area
    """

    __triangle_A: Triangle
    __triangle_B: Triangle

    @classmethod
    def constructor_direct(cls, area_triangle_A: float, area_triangle_B: float):
        """Creates and assymetric trapezoid with area of two trangles

        Args:
            area_triangle_A (float): _description_ Area of first division triangle of trapezoid
            area_triangle_B (float): _description_ Area of second division triangle of trapezoid

        Returns:
            _type_: _description_ Assymetric trapezoid object
        """
        # Creates a new instance of asymmetrical trapezoid class
        asymmetric_trapezoid = cls.__new__(cls)

        # Initializes attributes
        asymmetric_trapezoid.__triangle_A = Triangle.constructor_area(area_triangle_A)
        asymmetric_trapezoid.__triangle_B = Triangle.constructor_area(area_triangle_B)

        return asymmetric_trapezoid

    @classmethod
    def constructor_triangle(cls, triangle_A: Triangle, triangle_B: Triangle):
        """Creates and asymmetric trapezoid

        Args:
            triangle_A (Triangle): _description_ First division triangle of trapezoid
            triangle_B (Triangle): _description_ Second division triangle of trapezoid

        Returns:
            _type_: _description_ Asymmetric trapezoid object
        """
        # Creates a new instance of asymmetrical trapezoid class
        asymmetric_trapezoid = cls.__new__(cls)

        # Initializes attributes
        asymmetric_trapezoid.__triangle_A = triangle_A
        asymmetric_trapezoid.__triangle_B = triangle_B

        return asymmetric_trapezoid

    @classmethod
    def constructor_sides_angle(cls, side_A: float, side_B: float, side_C: float, side_D: float, angle: float):
        """Creates and asymmetric

        Args:
            side_A (float): _description_ Any side of trapezoid
            side_B (float): _description_ Any side of trapezoid
            side_C (float): _description_ Any side of trapezoid
            side_D (float): _description_ Any side of trapezoid
            angle (float): _description_ Angle between side_A, and side_B in radians

        Returns:
            _type_: _description_ Asymmetric trapezoid object
        """
        # Creates a new instance of asymmetric trapezoid class
        asymmetric_trapezoid = cls.__new__(cls)

        # Initialize attributes
        asymmetric_trapezoid.__triangle_A = Triangle.constructor_sides_angle(side_A, side_B, angle)

        # Calculates the common base between two triangles that form the trapezoid
        base = math.sqrt(side_A ** 2 + side_B ** 2 - 2 * side_A * side_B * math.cos(angle))

        asymmetric_trapezoid.__triangle_B = Triangle.constructor_sides(side_C, side_D, base)

        return asymmetric_trapezoid

    def area(self) -> float:
        """Returns the area measures

        Returns:
            float: _description_ Area of trapezoid
        """
        return self.__triangle_A.area() + self.__triangle_B.area()