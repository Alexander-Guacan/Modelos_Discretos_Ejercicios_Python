def input_worker_data() -> None:
    """_summary_ Enters of worker data (hours worked and price by hour)
    """
    # Initialize variable with incorrect data
    hours_worked = -1
    
    # Enter value until that greather or equals than zero
    while hours_worked < 0:
        # Input data by keyboard
        hours_worked = int(input("Horas trabajadas: "))

    # Initialize variable with incorrect data
    price_by_hour_worked = -1

    # Enter value until that greather than zero
    while price_by_hour_worked <= 0:
        # Input data by keyboard
        price_by_hour_worked = int(input("Coste por hora: "))

def main() -> None:
    """_summary_ Main function where program will be start
    """

    # Variable that indicate if is right input data
    successful_entry = False

    # Data will be entered until no exception is triggered.
    while (not successful_entry):
        try:
            # Calling function for enter worker data
            input_worker_data()
            # Data was be entered succesfully
            successful_entry = True
        except ValueError:
            # Printing message when ValueError excepction is cathed
            print("\nERROR [ INGRESE UN DATO NUMERICO ]\n")

    # Printing message when data is enter succesfully
    print("\nIngreso de datos exitoso")
        
# Verifying if this module is the main
if __name__ == "__main__":
    # Calling main function
    main()