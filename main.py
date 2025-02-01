from PyBank import Bank, Person

bank = Bank("Banca Transilvania")

persoana_1 = Person("Ionescu", "Cristi", 123456789)
persoana_2 = Person("Popescu", "Andrei", 234567891)
persoana_3 = Person("Dumitru", "Elena", 345678912)
persoana_4 = Person("Georgescu", "Mihai", 456789123)
persoana_5 = Person("Mihaescu", "Marin", 987654321)

bank.register_employee(persoana_1)
bank.register_employee(persoana_2)
bank.register_employee(persoana_3)
bank.register_employee(persoana_4)
bank.register_employee(persoana_5)

bank.print_all_employee()