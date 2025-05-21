# Functions that accept variable length key value pair as arguments

def print_key_value_pairs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_value_pairs(Name="Alice", Age=30, Country="USA")

# Code by Harshit