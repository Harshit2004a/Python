# Assigning Subsequent Rows to Matrix first row elements

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = {val: [row[i] for row in matrix[1:]] for i, val in enumerate(matrix[0])}
print(result)

# Code by Harshit