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

def calculate_expression() -> None:
    """Calculates the math expression: f(x) = 1/2 * (x ^ z)
    """

    # Enters 'x' and 'z' values by keyboard
    print("f(x) = 1/2 * (x ^ z)")
    base = input_float("Ingrese el valor x: ")
    exponent = input_float("Ingrese el valor z: ")

    # Calculates expression
    result = (base ** exponent) / 2

    # Printin result variable
    print(f"f(x) = {result}")

def main() -> None:
    calculate_expression()

if __name__ == "__main__":
    main()