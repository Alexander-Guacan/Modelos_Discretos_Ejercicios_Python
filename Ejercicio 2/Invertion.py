class Invertion:
    """Save invertion data and calculates capital obtained

    Attributes:
        __invertion_amount: float
        __anual_interest_rate: float
        __years: float        
    
    Methods:
        __init__
        calculate
    """
    
    # Declarates atrributes of class
    __invertion_amount: float
    __anual_interest_rate: float
    __years: float

    def __init__(self, invertion: float, annual_invertion_rate: float, years: float) -> None:
        """_summary_ Default constructor

        Args:
            invertion (float): _description_ Money to invest
            annual_invertion_rate (float): _description_ Annual Invertion rate for invertion
            years (float): _description_ Years to keep the capital of invertion
        """
        self.__invertion_amount = invertion
        self.__anual_interest_rate = annual_invertion_rate
        self.__years = years

    def calculate(self) -> float:
        return self.__invertion_amount + ((self.__invertion_amount * self.__anual_interest_rate) / 100) * self.__years