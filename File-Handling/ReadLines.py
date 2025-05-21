# Read specific lines from a file in Python

filename = 'your_file.txt'

user_input = input("Enter line numbers to read (comma-separated): ")
lines_to_read = [int(num.strip()) for num in user_input.split(',') if num.strip().isdigit()]

with open(filename, 'r') as file:
    for i, line in enumerate(file, start=1):
        if i in lines_to_read:
            print(f"Line {i}: {line.strip()}")
            
# Code by Harshit