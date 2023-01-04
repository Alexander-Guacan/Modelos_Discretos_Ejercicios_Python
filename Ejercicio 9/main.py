# Import maxsize value from sys library
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

def calculate_pythagoras(coefficients: list[float]) -> float:
    """Returns value of Pythagoras equation

    Args:
        coefficients (list[float]): _description_ Coefficients in Pythagoras equation

    Returns:
        float: _description_ Result of Pythagoras equation
    """
    # Variable where save the result of Pythagoras equation
    pythagoras = 0

    # Replaces each coefficients in Pythagoras equation
    for coefficient in coefficients:
        pythagoras += coefficient ** 2

    return pythagoras

def enter_coefficients(dimention: int) -> list[float]:
    """Enters coefficients values of Pythagoras equation

    Args:
        dimention (int): _description_ Amount of coefficients in equation

    Returns:
        list[float]: _description_ Values of coefficients
    """
    # List where save values of each coefficients of equation
    coefficients = list[float]()

    # Enters each coefficients in coefficients list
    for i in range(dimention):
        coefficients.append(input_float(f"Ingrese coeficiente {i + 1}: "))

    return coefficients

def main() -> None:
    # Enters dimention or amount of coefficients in the equations
    dimention = input_int("Ingrese la dimension de la figura: ")
    print(f"Pitagoras = {calculate_pythagoras(enter_coefficients(dimention).copy())}")

if __name__ == "__main__":
    main()