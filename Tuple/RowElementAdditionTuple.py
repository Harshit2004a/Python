# Row wise element addition in a tuple matrix
tuple_matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# sum elements of each row
row_sums = [sum(row) for row in tuple_matrix]

print("Tuple Matrix:")
for row in tuple_matrix:
    print(row)
print("\nRow-wise sums:", row_sums)

# Code by Harshit