# Dictionary with keys as tuples (multiple inputs)

multi_input_dict = {
    ('apple', 'red'): 10,
    ('banana', 'yellow'): 5,
    ('grape', 'purple'): 8
}

# values using multiple inputs
fruit = 'apple'
color = 'red'
print(multi_input_dict[(fruit, color)])  # Output: 10

# add new entry
multi_input_dict[('orange', 'orange')] = 12

# iterating over dictionary
for (fruit, color), quantity in multi_input_dict.items():
    print(f"{fruit} ({color}): {quantity}")
    
# code by Harshit