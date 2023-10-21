from dataclasses import dataclass

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age

# instead all of this up there I can use data class, works the same

@dataclass
class Person:
    name: str
    age: int

p1 = Person('Patrick', 31)
print(p1)
p2 = Person('Patrick', 31)
print(p1 == p2)


