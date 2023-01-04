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

def evaluate_expression(a: float, b: float) -> float:
    """Evaluate the equation

    Args:
        a (float): _description_ first coefficient
        b (float): _description_ second coefficient

    Returns:
        float: _description_ Result of evaluation of equation
    """
    return (a + b ** 2) / 2.5

def main() -> None:
    # Print the expression to evaluate
    print("f(x) = (a + b^2) / 2.5")

    # Enters coefficients of equation
    a = input_float("Ingrese a: ")
    b = input_float("Ingrese b: ")

    # Print result of equation
    print(f"f(x) = {evaluate_expression(a, b)}")

if __name__ == "__main__":
    main()