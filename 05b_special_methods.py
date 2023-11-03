class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.com').lower()

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # it's good to have at minimum __repr__
    # we use it to present object and how they are printed
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # more readable or the user
    def __str__(self):
        # return '{} - {}'.format(self.fullname(), self.email)
        return f'{self.fullname()} - {self.email}'

    # adding salaries of all workers
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# 1
# print(emp_1)

# direct call of special methods
# print(repr(emp_1))
# print(str(emp_1))

# 2
# behind the scenes it's calling special method __add__
print(1+2)

print(int.__add__(1,2))
print(str.__add__('a', 'b'))

# using __add__ method to add salaries
print(emp_1 + emp_2)

# 3
print(len('test'))
print('test'.__len__())

print('Length of employees name is: ' + str(len(emp_1)))
