from Student import Student

class StudentReport:
    """Class that shows stadistics of a studen

    Method:
        show
    """

    @classmethod
    def show(cls, student: Student) -> None:
        """Shows stadistics of a student

        Args:
            student (Student): _description_ Student object
        """
        print(
            "\nREPORTE DE ESTUDIANTE",
            f"\nTotal: {student.total()}",
            f"\nPromedio: {student.average()}",
            f"\nPorcentaje: {student.percentage()}",
        )