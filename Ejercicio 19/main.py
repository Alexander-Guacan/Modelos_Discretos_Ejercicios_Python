# Import hierarchy of IShape class
from Rectangle import Rectangle, IShape
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

def print_perimeter_shape(shape: IShape) -> None:
    """Prints perimeter of any object that inheritance of IShape

    Args:
        shape (IShape): _description_ Any object son of IShape
    """
    print(f"Perimetro = {shape.perimeter()}")

def main() -> None:
    # Enters base and height for create a rectangle object
    base = input_float("Ingrese la base del rectangulo: ")
    height = input_float("Ingrese la altura del rectangulo: ")
    
    # Print perimeter of rectangle
    print_perimeter_shape(Rectangle(base, height))

if __name__ == "__main__":
    main()