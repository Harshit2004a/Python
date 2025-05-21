# Row-wise element addition in a tuple matrix

def row_wise_addition(matrix):
    return [sum(row) for row in matrix]

tuple_matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

print("Row-wise sums:", row_wise_addition(tuple_matrix))

# Code by Harshit