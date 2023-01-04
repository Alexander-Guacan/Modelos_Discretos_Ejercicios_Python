# Imports hierarchy of Trapezoid family
from AsymmetricTrapezoid import AsymmetricTrapezoid
from SymmetricalTrapezoid import SymmetricalTrapezoid
from Trapezoid import Trapezoid
# Import triangle class
from Triangle import Triangle
# Import maxsize value from sys library
from sys import maxsize as max_value
# Import os library
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

def create_asymmetric_trapezoid_directly() -> AsymmetricTrapezoid:
    """Creates an assymetric trapezoid with measures input by keyboard (area measures of triangles)

    Returns:
        AsymmetricTrapezoid: _description_ Asymetric Trapezoid creates with area measures of triangles
    """

    # Enters the area measures of triangles
    area_triangle_A = input_float("Ingrese el area del primer triangulo: ")
    area_triangle_B = input_float("Ingrese el area del segundo triangulo: ")
    # Returns an assymmetric trapezoid object
    return AsymmetricTrapezoid.constructor_direct(area_triangle_A, area_triangle_B)

def create_asymmetric_trapezoid_with_base_and_height() -> AsymmetricTrapezoid:
    """Creates an assymetric trapezoid with measures input by keyboard (base and heights measures of triangles)

    Returns:
        AsymmetricTrapezoid: _description_ Asymetric Trapezoid creates with base and heights measures of triangles
    """
    # Enters the base and height measures of triangles
    height_triangle_A = input_float("Ingrese la altura del primer triangulo: ")
    height_triangle_B = input_float("Ingrese la altura del segundo triangulo: ")
    base = input_float("Ingrese la base comun del primer y segundo triangulo: ")

    # Returns an assymmetric trapezoid object
    return AsymmetricTrapezoid.constructor_triangle(Triangle.constructor_base_height(base, height_triangle_A), Triangle.constructor_base_height(base, height_triangle_B))

def create_asymmetric_trapezoid_with_sides_and_angle() -> AsymmetricTrapezoid:
    """Creates an assymetric trapezoid with measures input by keyboard (sides and angle measures of trapezoid)

    Returns:
        AsymmetricTrapezoid: _description_ Asymetric Trapezoid creates with sides and angle measures of trapezoid
    """
    # Enters sides and angle measures of assymetric trapezoid
    side_A = input_float("Ingrese el lado A: ")
    side_B = input_float("Ingrese el lado B: ")
    side_C = input_float("Ingrese el lado C: ")
    side_D = input_float("Ingrese el lado D: ")
    angle = input_float("Ingrese angulo entre lado A y B (radianes): ")

    # Returns an assymmetric trapezoid object
    return AsymmetricTrapezoid.constructor_sides_angle(side_A, side_B, side_C, side_D, angle)

def create_symmetrical_trapezoid_with_diagonals() -> SymmetricalTrapezoid:
    """Creates a symmetrical trapezoid with measures input by keyboard (diagonals of trapezoid)

    Returns:
        AsymmetricTrapezoid: _description_ Asymetric Trapezoid creates with diagonals of trapezoid
    """
    # Enters diagonal measures of symmetrical trapezoid
    diagonal_A = input_float("Ingrese la diagonal principal: ")
    diagonal_B = input_float("Ingrese la diagonal secundaria: ")

    # Returns a symmetrical trapezoid object
    return SymmetricalTrapezoid.constructor_diagonals(diagonal_A, diagonal_B)

def create_symmetrical_trapezoid_with_sides_and_angle() -> SymmetricalTrapezoid:
    """Creates a symmetrical trapezoid with measures input by keyboard (dispair sides and one angle of trapezoid)

    Returns:
        AsymmetricTrapezoid: _description_ Asymetric Trapezoid creates with dispair sides and one angle of trapezoid
    """
    # Enters dispairs sides and angle measures of symmetrical trapezoid
    side_A = input_float("Ingrese el primer lado: ")
    side_B = input_float("Ingrese el segundo lado: ")
    angle = input_float("Ingrese el angulo entre el primer y segundo lado (radianes): ")
    
    # Returns a symmetrical trapezoid object
    return SymmetricalTrapezoid.constructor_sides_angle(side_A, side_B, angle)

def print_trapezoid_area(trapezoid: Trapezoid) -> None:
    """Print area measure of any object that inheritance of Trapezoid class

    Args:
        trapezoid (Trapezoid): _description_ Any object that inheritance of Trapezoid class
    """
    # Print area measure of any object that inheritance of Trapezoid class
    print(f"Area del trapezoide = {trapezoid.area()}")

def menu_asymmetric_trapezoid() -> None:
    """Manage the assymetric trapezoid menu
    """
    
    # Variable that verifies if the user select exit option
    exit = False

    # Keeps execute of this menu until select exit option
    while not exit:
        # Clear terminal console
        os.system("cls")

        # Print menu options
        print(
            "CALCULAR AREA DE UN TRAPEZOIDE",
            "\n1.- Area de triangulos"
            "\n2.- Base y altura de los triangulos"
            "\n3.- Lados del trapezoides y un angulo"
            "\n4.- Salir"
        )

        # Enters option of menu
        option = input_int("\nIngrese una opcion: ")

        # Selects the action by option
        match option:
            # Area of trapezoid with area measures of triangles
            case 1:
                print_trapezoid_area(create_asymmetric_trapezoid_directly())
                # Pause execution of program
                os.system("pause > nul")

            # Area of trapezoid with base and heights of triangles
            case 2:
                print_trapezoid_area(create_asymmetric_trapezoid_with_base_and_height())
                # Pause execution of program
                os.system("pause > nul")
            # Area of trapezoid with sides of him and angle between two sides
            case 3:
                print_trapezoid_area(create_asymmetric_trapezoid_with_sides_and_angle())
                # Pause execution of program
                os.system("pause > nul")
            # Has selected exit option
            case 4:
                exit = True
            # Option selected out of bounds of options menu
            case _:
                pass

def menu_symmetrical_trapezoid() -> None:
    """Manage the symmetrical trapezoid menu
    """
    # Variable that verifies if the user select exit option
    exit = False

    # Keeps execute of this menu until select exit option
    while not exit:
        # Clear terminal console
        os.system("cls")
        # Print menu options
        print(
            "CALCULAR AREA DE UN TRAPEZOIDE",
            "\n1.- Diagonales del trapezoide"
            "\n2.- Lados dispares y angulo entre ellos"
            "\n3.- Salir"
        )

        # Enters option of menu
        option = input_int("\nIngrese una opcion: ")

        # Select the action by option
        match option:
            # Area of trapezoid with diagonals measures
            case 1:
                print_trapezoid_area(create_symmetrical_trapezoid_with_diagonals())
                # Pause execution of program
                os.system("pause > nul")
            # Area of trapezoid with sides and angle
            case 2:
                print_trapezoid_area(create_symmetrical_trapezoid_with_sides_and_angle())
                # Pause execution of program
                os.system("pause > nul")
            # Has selected exit option
            case 3:
                exit = True
            # Option selected out of bounds of options menu
            case _:
                pass

def main() -> None:
    """Manage the main menu
    """
    # Variable that verifies if the user select exit option
    exit = False

    # Keeps execute of this menu until select exit option
    while not exit:
        # Clear terminal console
        os.system("cls")
        # Print menu options
        print(
            "CALCULAR AREA DE UN TRAPEZOIDE",
            "\n1.- Trapezoide asimetrico"
            "\n2.- Trapezoide simetrico"
            "\n3.- Salir"
        )

        # Enters option of menu
        option = input_int("\nSeleccione su tipo de trapezoide: ")

        # Select the action by option
        match option:
            # Enters the asymmetric trapezoid menu
            case 1:
                menu_asymmetric_trapezoid()

            # Enters the symmetrical trapezoid menu
            case 2:
                menu_symmetrical_trapezoid()

            # Has select the exit option
            case 3:
                exit = True

            # Option selected out of bounds of options menu
            case _:
                pass

            
if __name__ == "__main__":
    main()