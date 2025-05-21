# Group similar elements into Matrixs

def group_similar_elements(matrix):
    groups = {}
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            groups.setdefault(val, []).append((i, j))
    return groups

if __name__ == "__main__":
    matrix = [
        [1, 2, 2],
        [3, 1, 2],
        [1, 3, 3]
    ]
    grouped = group_similar_elements(matrix)
    for value, positions in grouped.items():
        print(f"Element {value}: Positions {positions}")
        

# Code by Harshit