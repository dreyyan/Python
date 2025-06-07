class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@google.com'
    def display_full_name(self):
        return 'First Name: {}\nLast Name: {}'.format(self.first_name, self.last_name)
    def display_salary(self):
        return 'Salary($): {}'.format(self.salary)
    def display_email(self):
        return 'Email: {}'.format(self.email.lower())

emp1 = Employee("Adrian", "Tan", 800)
emp2 = Employee("Charles", "Grey", 800)

print(emp1.display_full_name())
print(emp1.display_salary())
print(emp1.display_email())