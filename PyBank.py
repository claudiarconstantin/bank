class Person:
    def __init__(self, nume, prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp

    def print_details(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}")

class Bank:
    def __init__(self, name):
        self.name = name
        self.arhiva = []

    def register_employee(self, person):
        self.arhiva.append(person)

    def unregister_employee(self, cnp):
        self.arhiva = [p for p in self.arhiva if p.cnp != cnp]

    def print_all_employee(self):
        for person in self.arhiva:
            person.print_details()