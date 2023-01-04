# Imports class to create a cylinder object
from Cylinder import Cylinder, Rectangle, Circle
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

def create_cylinder() -> Cylinder:
    """Creates a cylinder object with input data by keyboard

    Returns:
        Cylinder: _description_ Cylinder object
    """
    # Enters radious and height of cylinder
    radius = input_float("Ingrese el radio de la tapa superior o inferior del cilindro: ")
    height = input_float("Ingrese la altura del cilindro: ")
    # Creates circle and rectangle objects
    circle = Circle(radius)
    rectangle = Rectangle(circle.perimeter(), height)

    return Cylinder(circle, rectangle)

def print_area_cylinder(cylinder: Cylinder) -> None:
    """Prints cylinder area

    Args:
        cylinder (Cylinder): _description_
    """
    print(f"Area del cilindro: {cylinder.area()}")

def main() -> None:
    # Print area of cylinder that was created
    print_area_cylinder(create_cylinder())

if __name__ == "__main__":
    main()