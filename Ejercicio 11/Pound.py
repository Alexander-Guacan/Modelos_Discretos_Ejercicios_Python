from WeightUnit import WeightUnit

class Pound(WeightUnit):
    """Weight unit

    Methods:
        __init__
    """
    
    def __init__(self, weight: float) -> None:
        """Default constructor

        Args:
            weight (float): _description_ Amount of weight
        """
        super().__init__(2.20462, weight)