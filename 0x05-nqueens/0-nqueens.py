#!/usr/bin/python3
"""The N queens puzzle"""
import sys


def print_solution(board):
    """Prints the coordinates of the queens"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """Checks if a queen can be placed at a given position"""
    # Check the left side of the current row
    for c in range(col):
        if board[row][c] == 1:
            return False
    # Check the anti diagonal on the left side
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    # Check the main diagonal on the left side
    for r, c in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    return True


def solve_nqueens(board, col):
    """Solves the N queens puzzle"""
    if col == len(board):
        print_solution(board)
        return True
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1)
            board[row][col] = 0
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for col in range(N)] for row in range(N)]
    solve_nqueens(board, 0)
