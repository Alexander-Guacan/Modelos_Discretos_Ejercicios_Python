# Import Rectangle class and IShape interface
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

def create_rectangle() -> Rectangle:
    """Creates and rectangle object with base and height measures

    Returns:
        Rectangle: _description_ Object created with data input by keyboard
    """

    # Enters measure of the base of rectangle
    base = input_float("Ingrese la medida de la base del rectangulo: ")
    # Enters measure of the height of rectangle
    height = input_float("Ingrese la altura del rectangulo: ")

    # Creates a rectangle object
    return Rectangle(base, height)

def print_area_and_perimeter(shape: IShape) -> None:
    """Prints area and perimeter measures of any object that implements the IShape interface

    Args:
        shape (IShape): _description_ Any object that implements the IShape interface
    """

    # Prints perimeter and area of a generic IShape object
    print(f"Perimetro de la figura = {shape.perimeter()}")
    print(f"Area de la figura = {shape.area()}")
    

def main() -> None:
    # Enters rectangle data and prints him perimeter and area measures
    print_area_and_perimeter(create_rectangle())

if __name__ == "__main__":
    main()