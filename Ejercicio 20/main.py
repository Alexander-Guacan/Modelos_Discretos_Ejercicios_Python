# Import hierarchy of LenghtUnit family
from LenghtUnit import LenghtUnit
from Meter import Meter
from Centimeter import Centimeter
from Kilometer import Kilometer
# Import maxsize value from sys library
from sys import maxsize as max_value
# Import os library for clear screen and pause program execution
import os

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

def transform_lenght(original_lenght: LenghtUnit, convertion_lenght: LenghtUnit) -> float:
    """Returns the transformation between lenght units

    Args:
        original_lenght (LenghtUnit): _description_ basic lenght unit
        convertion_lenght (LenghtUnit): _description_ convertion lenght unit

    Returns:
        float: _description_ Convertion result
    """
    return original_lenght.convert_to(convertion_lenght)

def menu_lenght_convertion_type(lenght: LenghtUnit) -> None:
    """Manage the lenght unit convertion menu

    Args:
        lenght (LenghtUnit): _description_ lenght unit type to convertion
    """

    # Clear screen and print menu options1
    print(
        "UNIDAD A CONVERTIR",
        "\n1.- Metro",
        "\n2.- Kilometro",
        "\n3.- Centimetro",
        "\n4.- Salir",
    )

    # Enters the option of menu
    option = input_int("\nIngrese la longitud de conversion: ")
    # Variable where save the result of convertion
    convertion = float()

    # Converts between lenght units selected
    match option:
        case 1:
            convertion = transform_lenght(lenght, Meter())

        case 2:
            convertion = transform_lenght(lenght, Kilometer())

        case 3:
            convertion = transform_lenght(lenght, Centimeter())

        case 4:
            return

        case _:
            pass

    # Prints result of convertion
    print(f"Resultado: {convertion}")
    # Pauses execution of program
    os.system("pause > nul")


def menu_lenght_types() -> None:
    """Manage the original lenght unit menu
    """

    # Variable that verifies if has pressed exit option in menu
    exit = False
    
    # Keeps execution program until press exit option
    while not exit:
        # Clear screen and print menu
        os.system("cls")
        print(
            "UNIDAD ORIGINAL",
            "\n1.- Metro",
            "\n2.- Kilometro",
            "\n3.- Centimetro",
            "\n4.- Salir",
        )

        # Input option and lenght measure
        option = input_int("\nIngresar una opcion: ")

        # Selects option and sends the lenght unit type object to the next menu
        match option:
            case 1:
                menu_lenght_convertion_type(Meter(input_float("Ingrese longitud: ")))

            case 2:
                menu_lenght_convertion_type(Kilometer(input_float("Ingrese longitud: ")))

            case 3:
                menu_lenght_convertion_type(Centimeter(input_float("Ingrese longitud: ")))

            # Disables this menu execution
            case 4:
                exit = True
            
            # Option out of bounds of menu options
            case _:
                pass
            
def main() -> None:
    menu_lenght_types()

if __name__ == "__main__":
    main()