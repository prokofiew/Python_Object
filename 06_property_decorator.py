class Employee:

    def __init__(self, first, last):
        self.first = first.strip().title()
        self.last = last.strip().title()
        self.email = (self.first + '.' + self.last + '@company.com').lower()

    def fullname(self):
        return f'{self.first} {self.last}'


class Employee1:

    def __init__(self, first, last):
        self.first = first.strip().title()
        self.last = last.strip().title()

# when property, don't need () to call method and there is no need to change code where email attribute is called
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'.lower().strip()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'.strip().title()

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

print('----------------class without property----------------------------')
emp_1 = Employee('   john   ', 'smith   ')
print(emp_1.first)
# email without () because it's an attribute placed in constructor
print(emp_1.email)
# if it's a regular method, have to add () in code everywhere where email is called
print(emp_1.fullname())
emp_1.first = 'Jim'
print('name change: ' + emp_1.first)
# email grabs the current first name
print('-> ' + emp_1.email)
# print(emp_1.email) for email attribute in constructor
print(emp_1.fullname())


print('----------------class with property----------------------------')
emp_2 = Employee1('    maria   ', ' something')
print('name: ' + emp_2.first)
# email grabs the current first name
print(emp_2.email)
# print(emp_1.email) for email attribute in constructor
print('fullname: ' + emp_2.fullname)
emp_2.first = 'edward'
print('name change: ' + emp_2.first)
print(emp_2.email)
print(emp_2.fullname)

print('----------------------SETTER--------------------------')
# this will throw an error if there is no setter -> @fullname setter
emp_2.fullname = 'mark egg'
print('fullname change: ' + emp_2.fullname)
print(emp_2.email)
print(emp_2.fullname)

print('-------------------------"DELETER"---------------------')
del emp_2.fullname
print(emp_2.first)
print(emp_2.last)