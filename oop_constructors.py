class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@google.com'

emp1 = Employee("Adrian", "Tan", 800)
emp2 = Employee("Charles", "Grey", 800)