#!/usr/bin/python3
"""
Interview
"""
import sys


def is_safe(board, row, col):
    """
    Helper function
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """
    Helper function
    """
    # Base case: If all queens are placed
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0

    return res


def print_solution(board):
    """
    Helper function
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def solve_nqueens(n):
    """
    Main function
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")


def validate_and_parse_args():
    """
    Validate function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


if __name__ == "__main__":
    n = validate_and_parse_args()
    solve_nqueens(n)
