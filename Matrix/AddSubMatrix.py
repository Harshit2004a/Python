# Adding & Subtracting Matrix

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8, 9],
    [10, 11, 12]
]

sum_matrix = [[a + b for a, b in zip(*rows)] for rows in zip(A, B)]
diff_matrix = [[a - b for a, b in zip(*rows)] for rows in zip(A, B)]

print("Sum:", sum_matrix)
print("Difference:", diff_matrix)

# Code by Harshit