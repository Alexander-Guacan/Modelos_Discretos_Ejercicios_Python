class WeightUnit:
    """Amount of matter contained in a body

    Attributes:
        _weight_in_kg: float
        _weight: float
        
    Methods:
        __init__
        convert_to
    """
    _weight_in_kg: float
    _weight: float

    def __init__(self, equivalent_weight_in_kg: float, weight: float) -> None:
        """Default constructor

        Args:
            equivalent_weight_in_kg (float): _description_ Amount of weight to equal one kilogram
            weight (float): _description_ Amount of weight contain in this object
        """
        # Initializes attributes
        self._weight_in_kg = equivalent_weight_in_kg
        self._weight = weight

    def convert_to(self, unit_of_conversion: "WeightUnit") -> float:
        # Transforms amount of weight to type of unit_of_convertion object
        return (self._weight * unit_of_conversion._weight_in_kg) / self._weight_in_kg