# Write a dictionary to a file in Python

import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open("output.json", "w") as file:
    json.dump(data, file)
    
# Code by Harshit