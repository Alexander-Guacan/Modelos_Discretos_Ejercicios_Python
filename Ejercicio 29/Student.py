class Student:
    """Class that contain the grades of any student and can calculates his stadistics

    Attributes:
        __grades: list[float]
        __max_grade: float
    
    Methods:
        add_grade
        average
        total
        percentage
    """

    __grades: list[float]
    __max_grade: float

    def __init__(self, max_grade: float) -> None:
        """Default constructor

        Args:
            max_grade (float): _description_ Maximum grade by which all subjects are evaluated
        """
        self.__max_grade = max_grade
        self.__grades = list[float]()
        

    def add_grade(self, grade: float) -> None:
        """Adds grade to list of grades

        Args:
            grade (float): _description_ Grade of subject
        """
        # Verifies if grades are in valid range
        if grade >= 0 and grade <= self.__max_grade:
            self.__grades.append(grade)

    def average(self) -> float:
        """Number taken as a representative of a list of numbers

        Returns:
            float: _description_ Average
        """
        average = self.total()

        return average / len(self.__grades)

    def total(self) -> float:
        """Sum of all grades of student

        Returns:
            float: _description_ Total sum
        """
        total = 0

        # Scrolling down the list
        for grade in self.__grades:
            total += grade

        return total

    def percentage(self) -> float:
        """Percentage completed of total grades for all subjects

        Returns:
            float: _description_ Percentaje
        """
        return (self.total() / (self.__max_grade * len(self.__grades))) * 100