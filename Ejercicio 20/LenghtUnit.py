class LenghtUnit:
    """Represents any lenght unit

    Attributes:
        _equivalent_lenght_of_meter: float
        _lenght: float    

    Method:
        convert_to
    """

    _equivalent_lenght_of_meter: float
    _lenght: float

    def __init__(self, equivalent_lenght_of_meter) -> None:
        """Default constructor

        Args:
            equivalent_lenght_of_meter (float, optional): _description_ Measure of this lenght type for equal to one meter.
        """
        self._equivalent_lenght_of_meter = equivalent_lenght_of_meter

    def convert_to(self, lenght_convertion: "LenghtUnit") -> float:
        """Returns convertion of current lenght type at the type lenght_convertion

        Args:
            lenght_convertion (LenghtUnit): _description_ Type lenght to convertion

        Returns:
            float: _description_ LenghtUnit convertion
        """
        return (self._lenght * lenght_convertion._equivalent_lenght_of_meter) / self._equivalent_lenght_of_meter