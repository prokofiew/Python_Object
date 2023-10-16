class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1
    def bark(self):
        print("woof")

d = Dog("Tim", 34)
print(d.name)
print(d.get_name())
print(d.get_age())

d2 = Dog("Bill", 12)
print(d2.name)
print(d2.get_name())
print(d2.get_age())