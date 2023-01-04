# Import class to create student and him report
from StudentReport import StudentReport, Student
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

def create_student() -> Student:
    """Creates a student object

    Returns:
        Student: _description_ Student object
    """
    # Enters max grade by subject
    max_grade = input_float("Ingrese la nota maxima por materias: ")

    return Student(max_grade)

def add_grades_at_student(student: Student) -> None:
    """Adds grade at the list of grades of a specified student

    Args:
        student (Student): _description_
    """
    
    student.add_grade(input_float("Ingrese la nota de la materia: "))

def show_report_student(student: Student) -> None:
    """Shows stadistics of a specified student on console

    Args:
        student (Student): _description_ Student to show his stadistics
    """
    StudentReport.show(student)

def main() -> None:
    # Creates student object
    student = create_student()
    
    # Variable that indicates if user don't want enters more grades
    is_end_of_grades = False
    while not is_end_of_grades:
        # Adds grade at the student
        add_grades_at_student(student)

        # Selects if want or not enter more grades
        option = ' '
        while option != 's' and option != 'n':
            option = input("Ingrese S o N para seguir ingresando numeros o no respectivamente: ").lower()

        # Doesn't enters more grades
        is_end_of_grades = option == 'n'

    # Print stadistics of student
    show_report_student(student)

if __name__ == "__main__":
    main()