from PyBank import Bank, Person, Employee, Job

bank = Bank("Banca Transilvania")


persoana_1 = Employee("Ionescu", "Cristi", 123456789, Job.MANAGER)
persoana_2 = Employee("Popescu", "Andrei", 234567891, Job.CONTABIL)
persoana_3 = Employee("Dumitru", "Elena", 345678912, Job.OPERATOR)
persoana_4 = Employee("Georgescu", "Mihai", 456789123, Job.ASISTENTA)
persoana_5 = Employee("Mihaescu", "Marin", 987654321, Job.MECANIC)

bank.register_employee(persoana_1)
bank.register_employee(persoana_2)
bank.register_employee(persoana_3)
bank.register_employee(persoana_4)
bank.register_employee(persoana_5)

bank.print_all_employee()

