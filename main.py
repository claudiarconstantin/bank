from PyBank import Bank, Person

bank = Bank("Banca Transilvania")

persons = [
    Person("Ionescu", "Cristi", 123456789),
    Person("Popescu", "Andrei", 234567891),
    Person("Dumitru", "Elena", 345678912),
    Person("Georgescu", "Mihai", 456789123),
    Person("Mihaescu", "Marin", 987654321)
]

for person in persons:
    bank.register_employee(person)

bank.print_all_employee()