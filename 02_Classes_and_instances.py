class Employee:
    def __init__(self ,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email.lower())
print(emp_2.email.lower())

# printing full name
print('1st method')
print('{} {}'.format(emp_1.first, emp_1.last))
print(f'{emp_1.first} {emp_1.last}')

print('2nd method')
print(emp_1.fullname())

print('3rd method')
print(Employee.fullname(emp_1))




