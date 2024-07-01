import argparse
from utils import print_sudoku, generate_full_board, remove_cells, save_sudoku_to_file

def generate_sudoku(difficulty='medium', output_file=None):
    """Generate a Sudoku puzzle."""
    difficulty_levels = {'easy': 35, 'medium': 45, 'hard': 55}
    num_holes = difficulty_levels.get(difficulty, 45)
    board = generate_full_board()
    puzzle = remove_cells(board, num_holes)
    
    if output_file:
        save_sudoku_to_file(puzzle, output_file)
    
    return puzzle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Sudoku puzzle.")
    parser.add_argument('--difficulty', choices=['easy', 'medium', 'hard'], default='medium',
                        help="Difficulty level of the Sudoku puzzle.")
    parser.add_argument('--output', type=str, help="File to save the generated Sudoku puzzle.")
    
    args = parser.parse_args()
    
    sudoku_puzzle = generate_sudoku(args.difficulty, args.output)
    print("Generated Sudoku puzzle:")
    print_sudoku(sudoku_puzzle)
    
    if args.output:
        print(f"Sudoku puzzle saved to {args.output}")
