# Convert class object to JSON in Python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

person = Person("Alice", 30)

person_json = json.dumps(person.to_dict())
print(person_json)

# Code by Harshit