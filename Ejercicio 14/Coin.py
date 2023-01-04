class Coin:
    """Represents the money

    Attributes:
        _convertion_to_dollar: float
        _amount: float    

    Method:
        convert_to
    """

    _convertion_to_dollar: float
    _amount: float

    def __init__(self, equivalent_amount_to_dollar) -> None:
        """Default constructor

        Args:
            equivalent_amount_to_dollar (float, optional): _description_ Amount of money of this coin type for equal to one USD.
        """
        self._convertion_to_dollar = equivalent_amount_to_dollar

    def convert_to(self, coin_convertion: "Coin") -> float:
        """Returns convertion of current coin type at the type coin_convertion

        Args:
            coin_convertion (Coin): _description_ Type coin to convertion

        Returns:
            float: _description_ Coin convertion
        """
        return (self._amount * coin_convertion._convertion_to_dollar) / self._convertion_to_dollar