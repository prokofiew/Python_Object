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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# __str__ will be called before __repr__. If there is no __str__, repr will be called
# print(emp_1)

# direct call of special methods
print(repr(emp_1))
print(emp_1.__repr__())
# or
print(str(emp_1))
print(emp_1.__str__())

print(1 + 2)
print('a' + 'b')
