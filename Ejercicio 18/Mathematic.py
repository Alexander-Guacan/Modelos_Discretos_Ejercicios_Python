class Mathematic:
    """Basic operations of arithmetic mathematic

    Methods:
        addition
        substraction
        multiplication
        divition
    """

    @classmethod
    def addition(cls, values: list[float]) -> float:
        """Returns the result of addition at all list of values

        Args:
            values (list[float]): _description_ Floating point values

        Returns:
            float: _description_ Result of addition of all values
        """
        # Variable that contains the result of addition
        result = .0
        # Scrolling down the list
        for value in values:
            # Apply addition to values
            result += value

        return result

    @classmethod
    def substraction(cls, values: list[float]) -> float:
        """Returns the result of substraction at all list of values

        Args:
            values (list[float]): _description_ Floating point values

        Returns:
            float: _description_ Result of substraction of all values
        """
        # Variable that contains the result of substraction
        result = values[0]
        # Scrolling down the list
        for i in range(1, len(values)):
            # Apply substraction to values
            result -= values[i]

        return result

    @classmethod
    def multiplication(cls, values: list[float]) -> float:
        """Returns the result of multiplication at all list of values

        Args:
            values (list[float]): _description_ Floating point values

        Returns:
            float: _description_ Result of multiplication of all values
        """
        # Variable that contains the result of multiplication
        result = 1.0
        # Scrolling down the list
        for value in values:
            # Apply multiplication to values
            result *= value

        return result

    @classmethod
    def divition(cls, values: list[float]) -> float:
        """Returns the result of divition at all list of values

        Args:
            values (list[float]): _description_ Floating point values

        Returns:
            float: _description_ Result of divition of all values
        """
        # Variable that contains the result of divition
        result = values[0]
        # Scrolling down the list
        for i in range(1, len(values)):
            # Apply divition to values
            result *= values[i] ** (-1)

        return result