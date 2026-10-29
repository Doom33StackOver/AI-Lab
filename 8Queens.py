def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col, n):
    # Check the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the lower diagonal on the left
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the same row on the left
    for j in range(col):
        if board[row][j]:
            return False

    return True


def solve_n_queens(board, col, n):
    # All queens have been placed
    if col >= n:
        return True

    # Try placing a queen in each row
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print("Solution for 8 Queens Problem:")
    print_board(board)
else:
    print("No solution exists.")


'''
Solution for 8 Queens Problem:
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .
'''
