from LenghtUnit import LenghtUnit

class Kilometer(LenghtUnit):
    """Kilometer lenght, inheritance of LenghtUnit class

    Methods:
        __init__
    """
    def __init__(self, lenght = .0) -> None:
        """Default constructor

        Args:
            lenght (float, optional): _description_. Lenght measure. Defaults to .0.
        """
        super().__init__(0.001)
        self._lenght = lenght