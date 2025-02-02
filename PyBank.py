class Person:
    def __init__(self, nume, prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp

    def print_details(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}")

class Employee(Person):
    def __init__(self, nume, prenume, cnp, job):
        super().__init__(nume, prenume, cnp)
        self.job = job

    def print_details(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}, Job: {self.job}")

    def print_my_job(self):
        print(f"My job is {self.job}.")

class Bank:
    def __init__(self, name):
        self.name = name
        self.arhiva = []

    def register_employee(self, person):
        for p in self.arhiva:
            if p.cnp == person.cnp:
                print(f"Persoana cu CNP-ul {person.cnp} deja exista!")
                return

        self.arhiva.append(person)
        print(f"Persoana {person.nume} {person.prenume} a fost inregistrata cu success!")

    def unregister_employee(self, cnp):
        self.arhiva = [p for p in self.arhiva if p.cnp != cnp]

    def print_all_employee(self):
        for person in self.arhiva:
            person.print_details()