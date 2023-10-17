
class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = (first + '.' + last + '@company.com').lower()

        Employee.num_of_emps += 1
        # class value without self. It will be all the same for all instances

    def fullname(self):
        return f'{self.first} {self.last}'

    def aplly_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # using self.raise_amount will let change that value for a single instance

    # def aplly_raise(self):
    #     self.pay = int(self.pay * Employee.raise_amount)


print('Number of employees: ' + str(Employee.num_of_emps))
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test','User',600000)

# full name and email
print(Employee.fullname(emp_1))
print(emp_1.mail)
print('-----------------------')
# pay_raise
print(emp_1.pay)
emp_1.aplly_raise()
print(emp_1.pay)
print('-----------------------')
# raise_amount
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('-----------------------')
# namespace of Employee 1
print(emp_1.__dict__)
print(Employee.__dict__)
print('-----------------------')
# changing class variable through class
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('-----------------------')
# changing class variable through instance
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('-----------------------')
# there is raise_amount in emp1 namespace so it returns that value before checking it in the class
print(emp_1.__dict__)
print('-----------------------')
# number of employees
print('Number of employees: ' + str(Employee.num_of_emps))
