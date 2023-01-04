# Import hierarchy of Coin family
from Coin import Coin
from Dollar import Dollar
from Yen import Yen
from Euro import Euro
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

def transform_coin(original_coin: Coin, convertion_coin: Coin) -> float:
    """Returns the transformation between coin units

    Args:
        original_coin (Coin): _description_ basic coin unit
        convertion_coin (Coin): _description_ convertion coin unit

    Returns:
        float: _description_ Convertion result
    """
    return original_coin.convert_to(convertion_coin)

def menu_coin_convertion_type(coin: Coin) -> None:
    """Manage the coin unit convertion menu

    Args:
        coin (Coin): _description_ coin unit type to convertion
    """

    # Clear screen and print menu options1
    print(
        "UNIDAD A CONVERTIR",
        "\n1.- Dolar estadounidense",
        "\n2.- Euro",
        "\n3.- Yen",
        "\n4.- Salir",
    )

    # Enters the option of menu
    option = input_int("\nIngrese la moneda de conversion: ")
    # Variable where save the result of convertion
    convertion = float()

    # Converts between coin units selected
    match option:
        case 1:
            convertion = transform_coin(coin, Dollar())

        case 2:
            convertion = transform_coin(coin, Euro())

        case 3:
            convertion = transform_coin(coin, Yen())

        case 4:
            return

        case _:
            pass

    # Prints result of convertion
    print(f"Resultado: {convertion}")
    # Pauses execution of program
    os.system("pause > nul")


def menu_coin_types() -> None:
    """Manage the original coin unit menu
    """

    # Variable that verifies if has pressed exit option in menu
    exit = False
    
    # Keeps execution program until press exit option
    while not exit:
        # Clear screen and print menu
        os.system("cls")
        print(
            "UNIDAD ORIGINAL",
            "\n1.- Dolar estadounidense",
            "\n2.- Euro",
            "\n3.- Yen",
            "\n4.- Salir",
        )

        # Input option and coin measure
        option = input_int("\nIngresar una opcion: ")

        # Selects option and sends the coin unit type object to the next menu
        match option:
            case 1:
                menu_coin_convertion_type(Dollar(input_float("Ingrese la cantidad de dinero: ")))

            case 2:
                menu_coin_convertion_type(Euro(input_float("Ingrese la cantidad de dinero: ")))

            case 3:
                menu_coin_convertion_type(Yen(input_float("Ingrese la cantidad de dinero: ")))

            # Disables this menu execution
            case 4:
                exit = True
            
            # Option out of bounds of menu options
            case _:
                pass
            
def main() -> None:
    menu_coin_types()

if __name__ == "__main__":
    main()