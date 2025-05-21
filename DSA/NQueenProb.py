# Python Program for N Queen Problem
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(board, row, col, n):
    if not hasattr(is_safe, "cols"):
        is_safe.cols = set()
        is_safe.diag1 = set()
        is_safe.diag2 = set()
    if col in is_safe.cols or (row-col) in is_safe.diag1 or (row+col) in is_safe.diag2:
        return False
    return True


# Code by Harshit