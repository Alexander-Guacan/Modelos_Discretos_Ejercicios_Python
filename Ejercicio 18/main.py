# Import Mathematic class
from Mathematic import Mathematic
# Import maxsize value from sys library
from sys import maxsize as max_value
# Import os library for clear screen and pause program execution
import os

def input_float(message: str, min = 0, max = max_value) -> float:
    """_summary_ Input integer data by keyboard in a range and controls exceptions

    Args:
        message (str): _description_ String to print before to input data by keyboard
        min (float, optional): _description_. Minimum value for a valid integer data. Defaults to 0.
        max (_type_, optional): _description_. Maximum value for a valid integer data. Defaults to sys.maxsize.

    Returns:
        float: _description_
    """

    # Variable that indicates if input data is right
    successful_entry = False

    # Variable that save the value entered by keyboard
    value = float()

    # Enters data until will be right
    while not successful_entry:
        try:
            # Enter data by keyboard
            value = float(input(message))
            # Verifies if data is right
            successful_entry = True if value >= min and value <= max else False

            # Printing error message when value is out of bounds
            if not successful_entry: print(f"Ingrese valor entre {min} y {max}\n")

        # Catch ValueError exception
        except ValueError:
            # Printing error message
            print("ERROR [ Ingrese un valor numerico ]\n")

    return value

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

def input_values() -> list[float]:
    """Returns a list of floating point values enters by keyboard

    Returns:
        list[float]: _description_ Values enters by keyboard
    """
    # List where will save the values input by keyboard
    values = list[float]()

    # Variable that indicates if the user does not want to enter more values to the list
    is_end_of_list = False

    # Clear screen
    os.system("cls")

    # Keeps enter values while the user not select 'n' option
    while not is_end_of_list:
        # Adds new value at the list of values
        values.append(input_float("Ingrese un nuevo valor a la lista: "))

        # Selects if want or not enter more values
        option = ' '
        while option != 's' and option != 'n':
            option = input("Ingrese S o N para seguir ingresando numeros o no respectivamente: ").lower()

        # Doesn't enters more values
        is_end_of_list = option == 'n'

    return values

def main() -> None:
    # Input values by keyboard
    values = input_values()

    # Select operations to apply at the list of values
    print(f"Suma = {Mathematic.addition(values)}")        
    print(f"Resta = {Mathematic.substraction(values)}")        
    print(f"Multiplicacion = {Mathematic.multiplication(values)}")        
    print(f"Division = {Mathematic.divition(values)}")

if __name__ == "__main__":
    main()