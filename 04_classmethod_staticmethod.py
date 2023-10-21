class Employee:
    num_of_emps = 0
    raise_amt = 1.04

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
        self.pay = int(self.pay * self.raise_amt)
        # using self.raise_amount will let change that value for a single instance

    # def aplly_raise(self):
    #     self.pay = int(self.pay * Employee.raise_amount)

    # creating class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # class method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print('Number of employees: ' + str(Employee.num_of_emps))
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 600000)
print("----------------------------------------------------")

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print('---------------------------------')

# usage if class method
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.mail)
print(new_emp_1.pay)
print('----------------------------------')

# class method using alternative constructor
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.mail)
print(new_emp_2.pay)
print('----------------------------------')

# static method use
import datetime

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
