from Person import Person

def greeting(person: Person) -> None:
    """Prints a greeting to person object

    Args:
        person (Person): _description_ Person object
    """
    # Print gretting
    print(f"Hola {person.get_name()}, bienvenido")

def main() -> None:
    # Enters the name of person
    greeting(Person(input("Ingrese su nombre: ")))

if __name__ == "__main__":
    main()