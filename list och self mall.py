class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Nu skapas ett objekt med id {id(self)}")

    def print_person(self):
        # Metoden behöver veta "vem" (vilket objekt)
        # som anropar den.
        # Därför skickar objektet med en referens
        # till sig själv, denna lagras i parametern self
        # Se kommentar rad 31 och 36.
        print(f"""Skriver nu ut objektet med
               Namn: {self.name}
               Ålder: {self.age}
               Objekt-id: {id(self)}""")


a_person = Person("Knatte", 5)
input("\nTryck <Enter> för att fortsätta ->")

print(f"\na_person har id-nr: {id(a_person)}")
input("\nTryck <Enter> för att fortsätta ->")

b_person = Person("Fnatte", 7)
input("\nTryck <Enter> för att fortsätta ->")

print(f"\nb_person har id-nr: {id(b_person)}")
input("\nTryck <Enter> för att fortsätta ->")

# En referens till a_person skickas med till print_person()
# Referensen syns inte i anropet.
a_person.print_person()
input("\nTryck <Enter> för att fortsätta ->")

# Givetvis skickar även b_person, och alla andra objekt,
# med denna "osynliga" referens.
b_person.print_person()