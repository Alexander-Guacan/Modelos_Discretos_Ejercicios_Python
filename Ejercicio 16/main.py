# Import circle class
from Circle import Circle
# Import maxsize value from sys library
from sys import maxsize as max_value

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

def print_circle_information(circle: Circle) -> None:
    """Prints area, diameter and perimeter of an circle

    Args:
        circle (Circle): _description_ Circle object that contains information to print
    """
    print(
        f"\nArea: {circle.area()}",
        f"\nPerimeter: {circle.perimeter()}",
        f"\nDiameter: {circle.diameter()}",
    )

def main() -> None:
    print_circle_information(Circle(input_float("Ingrese el radio del circulo: ")))

if __name__ == "__main__":
    main()