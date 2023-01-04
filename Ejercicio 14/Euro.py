from Coin import Coin

class Euro(Coin):
    """Euro coin, inheritance of Coin class

    Methods:
        __init__
    """
    def __init__(self, amount = .0) -> None:
        """Default constructor

        Args:
            amount (float, optional): _description_. Amount of money Defaults to .0.
        """
        super().__init__(0.94)
        self._amount = amount