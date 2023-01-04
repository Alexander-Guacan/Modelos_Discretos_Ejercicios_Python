from LenghtUnit import LenghtUnit

class Centimeter(LenghtUnit):
    """Centimeter lenght, inheritance of LenghtUnit class

    Methods:
        __init__
    """
    
    def __init__(self, lenght = .0) -> None:
        """Default constructor

        Args:
            lenght (float, optional): _description_. Length measure. Defaults to .0.
        """
        super().__init__(100)
        self._lenght = lenght