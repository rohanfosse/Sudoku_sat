import time
import argparse
from utils import solve_sudoku, print_sudoku, is_valid

def print_sudoku_with_highlight(board, original_board):
    """Print the Sudoku board with highlighted solution."""
    for i in range(9):
        for j in range(9):
            if original_board[i][j] == 0:
                print(f"\033[91m{board[i][j]}\033[0m", end=" ")  # Highlight in red
            else:
                print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

def main(board):
    print("Original Sudoku puzzle:")
    print_sudoku_with_highlight(board, board)

    start_time = time.time()
    original_board = [row[:] for row in board]
    if solve_sudoku(board):
        end_time = time.time()
        print("\nSolved Sudoku puzzle:")
        print_sudoku_with_highlight(board, original_board)
        print(f"\nSolved in {end_time - start_time:.4f} seconds.")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle.")
    parser.add_argument('--input', type=str, required=True, help="File containing the Sudoku puzzle.")
    
    args = parser.parse_args()

    # Read the Sudoku puzzle from the file
    with open(args.input, 'r') as file:
        board = []
        for line in file:
            row = [int(num) if num != '.' else 0 for num in line.split()]
            board.append(row)

    main(board)
