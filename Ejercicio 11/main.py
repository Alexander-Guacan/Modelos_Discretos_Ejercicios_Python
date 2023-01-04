# Imports hierarchy of weight unit family
from Pound import Pound, WeightUnit
from Kilogram import Kilogram
from Gram import Gram
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

def transforms_weights(original_weight: WeightUnit, convertion_weight: WeightUnit) -> float:
    """Returns the transformation between weight units

    Args:
        original_weight (WeightUnit): _description_ basic weight unit
        convertion_weight (WeightUnit): _description_ convertion weight unit

    Returns:
        float: _description_ Convertion result
    """
    return original_weight.convert_to(convertion_weight)

def menu_weight_convertion_type(weight: WeightUnit) -> None:
    """Manage the weight unit convertion menu

    Args:
        weight (WeightUnit): _description_ weight unit type to convertion
    """

    # Clear screen and print menu options1
    print(
        "UNIDAD A CONVERTIR",
        "\n1.- Libras",
        "\n2.- Gramos",
        "\n3.- Kilogramos",
        "\n4.- Salir",
    )

    # Enters the option of menu
    option = input_int("\nIngrese la unidad de conversion: ")
    # Variable where save the result of convertion
    convertion = float()

    # Converts between weight units selected
    match option:
        case 1:
            convertion = transforms_weights(weight, Pound(0))

        case 2:
            convertion = transforms_weights(weight, Gram(0))

        case 3:
            convertion = transforms_weights(weight, Kilogram(0))

        case 4:
            return

        case _:
            pass

    # Prints result of convertion
    print(f"Resultado: {convertion}")
    # Pauses execution of program
    os.system("pause > nul")


def menu_weight_types() -> None:
    """Manage the original weight unit menu
    """

    # Variable that verifies if has pressed exit option in menu
    exit = False
    
    # Keeps execution program until press exit option
    while not exit:
        # Clear screen and print menu
        os.system("cls")
        print(
            "UNIDAD ORIGINAL",
            "\n1.- Libras",
            "\n2.- Gramos",
            "\n3.- Kilogramos",
            "\n4.- Salir",
        )

        # Input option and weight measure
        option = input_int("\nIngresar una opcion: ")

        # Selects option and sends the weight unit type object to the next menu
        match option:
            case 1:
                menu_weight_convertion_type(Pound(input_float("Ingrese el peso: ")))

            case 2:
                menu_weight_convertion_type(Gram(input_float("Ingrese el peso: ")))

            case 3:
                menu_weight_convertion_type(Kilogram(input_float("Ingrese el peso: ")))

            # Disables this menu execution
            case 4:
                exit = True
            
            # Option out of bounds of menu options
            case _:
                pass
            
def main() -> None:
    menu_weight_types()

if __name__ == "__main__":
    main()