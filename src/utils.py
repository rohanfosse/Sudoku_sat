import random

def is_valid(board, row, col, num):
    """Check if it's valid to place num at board[row][col]."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    """Solve the Sudoku using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    """Find an empty cell in the board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_sudoku(board):
    """Print the Sudoku board with borders."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print('.', end=" ")
            else:
                print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

def save_sudoku_to_file(board, filename):
    """Save the Sudoku board to a file."""
    with open(filename, 'w') as file:
        for row in board:
            file.write(" ".join(str(num) if num != 0 else "." for num in row) + "\n")

def generate_full_board():
    """Generate a fully solved Sudoku board."""
    board = [[0] * 9 for _ in range(9)]
    fill_diagonal_boxes(board)
    fill_remaining(board, 0, 3)
    return board

def fill_diagonal_boxes(board):
    """Fill the diagonal 3x3 boxes with random numbers."""
    for i in range(0, 9, 3):
        fill_box(board, i, i)

def fill_box(board, row, col):
    """Fill a 3x3 box with random numbers."""
    nums = list(range(1, 10))
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums.pop()

def fill_remaining(board, i, j):
    """Fill the remaining cells of the board."""
    if j >= 9 and i < 8:
        i += 1
        j = 0
    if i >= 9 and j >= 9:
        return True
    if i < 3:
        if j < 3:
            j = 3
    elif i < 6:
        if j == (i // 3) * 3:
            j += 3
    else:
        if j == 6:
            i += 1
            j = 0
            if i >= 9:
                return True
    for num in range(1, 10):
        if is_valid(board, i, j, num):
            board[i][j] = num
            if fill_remaining(board, i, j + 1):
                return True
            board[i][j] = 0
    return False

def remove_cells(board, num_holes):
    """Remove cells to create a puzzle with a unique solution."""
    while num_holes > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = board[row][col]
        board[row][col] = 0
        copy_board = [row[:] for row in board]
        if not solve_sudoku(copy_board):
            board[row][col] = backup
        else:
            num_holes -= 1
    return board
