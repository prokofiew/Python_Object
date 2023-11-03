class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.com').lower()

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10  # change in developer class only

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # different way to pass base constructor
        # Employee.__init__(self, first, last, pay)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # NONE because it's better not to pass mutable datatypes such as list and dictionary as a default argument
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # adding employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print('Adding employee...')

    # removing employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print('Removing employee...')

    # printing all employees
    def print_emps(self):
        print('Manager of:')
        for emp in self.employees:
            print('--->', emp.fullname())


print("-------------------class employee-------------------------------")
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print('------------------class developer--------------------------------')
dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Test', 'User', 60000, 'java')

print(dev_1.email)
print(dev_1.prog_lang)

# altering raise amount in child class
print(dev_1.pay)
dev_1.apply_raise()
print('after raise: ' + str(dev_1.pay))

# shows structure of inheritance
# print(help(Developer))


print('---------------------MANAGER---------------------------------------------')
man_1 = Manager('Sergei', 'Prokofiev', 100000, [dev_1])
print(man_1.email)
man_1.print_emps()
# add
man_1.add_emp(dev_2)
man_1.print_emps()
# remove
man_1.remove_emp(dev_1)
man_1.print_emps()

# checking if class is an instance or subclass
print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))
print('--------------------------------')
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
