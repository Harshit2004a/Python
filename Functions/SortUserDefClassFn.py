# Sorting objects of user defined class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]

print("Sorted by age:", sorted(people, key=lambda p: p.age))
print("Sorted by name:", sorted(people, key=lambda p: p.name))

# Code by Harshit
