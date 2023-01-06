# Importing Invertion class
from Invertion import Invertion
from sys import maxsize as max_value

def input_int(message: str, min = 0, max = max_value) -> int:
    """_summary_ Input integer data by keyboard in a range and controls exceptions

    Args:
        message (str): _description_ String to print before to input data by keyboard
        min (int, optional): _description_. Minimum value for a valid integer data. Defaults to 0.
        max (_type_, optional): _description_. Maximum value for a valid integer data. Defaults to sys.maxsize.

    Returns:
        int: _description_
    """

    # Variable that indicates if input data is right
    successful_entry = False

    # Variable that save the value entered by keyboard
    value = int()

    # Enters data until will be right
    while not successful_entry:
        try:
            # Enter data by keyboard
            value = int(input(message))
            # Verifies if data is right
            successful_entry = True if value >= min and value <= max else False

            # Printing error message when value is out of bounds
            if not successful_entry: print(f"Ingrese valor entre {min} y {max}\n")

        # Catch ValueError exception
        except ValueError:
            # Printing error message
            print("ERROR [ Ingrese un valor numerico ]\n")

    return value


def enter_invertion_data() -> Invertion:
    """_summary_ Creates an Invertion object

    Returns:
        Invertion: _description_ Object that contains data for calculates the capital invertion
    """

    # Input inversion value by keyboard
    invertion = input_int("Ingresar inversion: ")
    # Input annual invertion rate value by keyboard
    annual_invertion_rate = input_int("Ingresar tasa de interes anual: ")
    # Input years value by keyboard
    years = input_int("Ingresar anios de inversion: ")

    return Invertion(invertion, annual_invertion_rate, years)

def print_invertion_calculate() -> None:
    """_summary_ Printing capital invertion value calculate on Invertion object
    """
    print("\nCapital por inversion:", enter_invertion_data().calculate())

def main() -> None:
    """_summary_ Main function
    """
    print_invertion_calculate()

if __name__ == "__main__":
    # Calling main function
    main()