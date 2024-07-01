# Sudoku Generator

A Sudoku puzzle generator and solver implemented in Python.

## Features

- Generate Sudoku puzzles with varying levels of difficulty (easy, medium, hard).
- Solve Sudoku puzzles.
- Save generated Sudoku puzzles to a file.

## Installation

```sh
pip install -r requirements.txt
```

## Project Structure

```
sudoku-generator/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── sudoku_generator.py
│   ├── sudoku_solver.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_sudoku_generator.py
│   ├── test_sudoku_solver.py
│   └── test_utils.py
└── examples/
    ├── easy_sudoku.txt
    ├── medium_sudoku.txt
    └── hard_sudoku.txt
```

## How the Code Works

### `src/utils.py`

This module contains utility functions used throughout the project:

- `is_valid(board, row, col, num)`: Checks if placing `num` at position `(row, col)` on the `board` is valid.
- `solve_sudoku(board)`: Solves the Sudoku puzzle using backtracking.
- `find_empty(board)`: Finds an empty cell on the Sudoku board.
- `print_sudoku(board)`: Prints the Sudoku board in a readable format.
- `save_sudoku_to_file(board, filename)`: Saves the Sudoku board to a file.
- `generate_full_board()`: Generates a fully solved Sudoku board.
- `fill_diagonal_boxes(board)`: Fills the diagonal 3x3 boxes of the board.
- `fill_box(board, row, col)`: Fills a 3x3 box with random numbers.
- `fill_remaining(board, i, j)`: Fills the remaining cells of the board.
- `remove_cells(board, num_holes)`: Removes cells from a fully solved board to create a puzzle with a unique solution.

### `src/sudoku_generator.py`

This module generates Sudoku puzzles:

- `generate_sudoku(difficulty='medium', output_file=None)`: Generates a Sudoku puzzle with the specified difficulty (easy, medium, or hard) and optionally saves it to a file.
- Main script: Generates and prints a Sudoku puzzle of the specified difficulty, and saves it to a file if specified.

### `src/sudoku_solver.py`

This module solves Sudoku puzzles:

- `main(board)`: Solves the given Sudoku puzzle and prints the solution with the time taken to solve it.
- Main script: Accepts a file containing a Sudoku puzzle as input, solves it, and prints the solution with the time taken to solve it.

### `tests/`

This folder contains unit tests for the generator and solver:

- `test_sudoku_generator.py`: Tests the Sudoku generator.
- `test_sudoku_solver.py`: Tests the Sudoku solver.
- `test_utils.py`: Tests utility functions.

### `examples/`

This folder contains example Sudoku puzzles of different difficulties.

## Usage

### Generating a Sudoku Puzzle

To generate a Sudoku puzzle, you can run the `sudoku_generator.py` script. You can specify the difficulty level and optionally specify an output file to save the puzzle.

```sh
python src/sudoku_generator.py --difficulty medium --output examples/medium_sudoku.txt
```

The generated Sudoku puzzle will be printed in the console and saved to `examples/medium_sudoku.txt` if specified.

### Solving a Sudoku Puzzle

To solve a Sudoku puzzle, you can run the `sudoku_solver.py` script with the input file containing the puzzle.

```sh
python src/sudoku_solver.py --input examples/medium_sudoku.txt
```

The script will print the original puzzle, the solved puzzle with the numbers found highlighted in red, and the time taken to solve the puzzle.

### Running Tests

To run the unit tests, you can use `unittest`:

```sh
python -m unittest discover -s tests
```

This will discover and run all tests in the `tests` folder.

## License

This project is licensed under the MIT License.
