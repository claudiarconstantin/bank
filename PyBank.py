from enum import Enum

class Job(Enum):
    OPERATOR = "operator"
    CONTABIL = "contabil"
    MANAGER = "manager"
    PROGRAMATOR = "programator"
    SECRETAR = "secretar"
    ASISTENTA = "asistenta"
    DOCTOR = "doctor"
    MECANIC = "mecanic"

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
        if not isinstance(job, Job):
            raise ValueError("Job invalid!Jobul trebuie sa aiba una din valorile acceptate.")
        self.job = job

    def print_details(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}, Job: {self.job.value}")

    def print_my_job(self):
        print(f"My job is {self.job.value}.")

class Bank:
    def __init__(self, name):
        self.name = name
        self.arhiva = []

    def register_employee(self, person):
        if not isinstance(person, Employee):
            print("Doar angajatii cu un job valid pot fi inregistrati!")
            return

        if person.job not in Job:
            print(f"Job invalid. Persoana nu a putut fi inregistrata.")
            return

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