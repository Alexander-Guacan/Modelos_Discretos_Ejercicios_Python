# Import maxsize value from sys library
from sys import maxsize as max_value
import math

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

def calculate_remaining_angle(angle_A: float, angle_B: float) -> float:
    """Calculates the third angle remaining in a triangle

    Args:
        angle_A (float): _description_ Any angle of triangle in radians
        angle_B (float): _description_ Any angle of triangle in radians

    Returns:
        float: _description_
    """
    return math.pi - angle_A - angle_B

def main() -> None:
    # Enters two angles knowns of triangle
    angle_A = input_float("Ingresar el primer angulo del triangulo: ")
    angle_B = input_float("Ingresar el segundo angulo del triangulo: ")

    # Print remaining angle of triangle
    print(f"El tercer angulo del triangulo es: {calculate_remaining_angle(angle_A, angle_B)}")

if __name__ == "__main__":
    main()