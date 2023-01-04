class Person:
    """Person class that contains basic information like name

    Attributes:
        __name: str

    Methods:
        get_name
    """

    __name: str

    def __init__(self, name: str) -> None:
        """Default constructor

        Args:
            name (str): _description_ Name of person
        """

        # Sets capitalize format
        self.__name = name.capitalize()

    def get_name(self) -> str:
        """Returns the name attribute

        Returns:
            str: _description_ Name of person object
        """
        return self.__name