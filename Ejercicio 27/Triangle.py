import math

class Triangle:
    """Triengle object

    Attributes:
        base: float
        height: float
        angle: float
        area: float

    Methods:
        get_base
        get_height
        get_angle
        area
    """

    __base: float
    __height: float
    __angle: float
    __area: float

    @classmethod
    def constructor_area(cls, area: float):
        """Constructor that initialize area attribute

        Args:
            area (float): _description_ Area measure of triangle object
        """

        # Initializes area attribute
        triangle = cls.__new__(cls)
        triangle.__area = area
        return triangle
    
    @classmethod
    def constructor_base_height(cls, base: float, height: float):
        """Initialize base and height attributes and calculates him area measure

        Args:
            base (float): _description_ Measure of side of rectangle where indicates the base of height measure
            height (float): _description_ Measure of line that start in a vertix and finish in him opposite side
        """

        triangle = cls.__new__(cls)
        # Calculates area
        triangle.__area = (base * height) / 2

        return triangle

    @classmethod
    def constructor_sides_angle(cls, side_A: float, side_B: float, angle: float):
        """Initialize area and angle attributes from two sides and the angle between them

        Args:
            side_A (float): _description_ Any side of triangle
            side_B (float): _description_ Adyacent side to side_A
            angle (float): _description_ Angle between side_A and side_B (in radians)
        """

        triangle = cls.__new__(cls)
        # Calculates area
        triangle.__area = 1 / 2 * side_A * side_B * math.sin(angle)
        return triangle

    @classmethod
    def constructor_sides(cls, side_A: float, side_B: float, side_C: float):
        triangle = cls.__new__(cls)
        semiperimeter = (side_A + side_B + side_C) / 2
        triangle.__area = math.sqrt(semiperimeter * (semiperimeter - side_A) * (semiperimeter - side_B) * (semiperimeter - side_C))
        return triangle

    def get_base(self) -> float:
        """Returns base attribute measure

        Returns:
            float: _description_ Base attribute
        """
        return self.__base

    def get_height(self) -> float:
        """Returns height attribute measure

        Returns:
            float: _description_ Height attribute
        """
        return self.__height

    def get_angle(self) -> float:
        """Returns angle attribute measure

        Returns:
            float: _description_ Angle attribute
        """
        return self.__angle

    def area(self) -> float:
        """Returns angle attribute measure

        Returns:
            float: _description_ Angle attribute
        """
        return self.__area