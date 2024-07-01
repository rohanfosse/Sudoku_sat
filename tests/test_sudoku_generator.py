import unittest
from src.sudoku_generator import generate_sudoku
from src.utils import print_sudoku

class TestSudokuGenerator(unittest.TestCase):
    def test_generate_sudoku(self):
        puzzle = generate_sudoku('easy')
        self.assertIsNotNone(puzzle)
        print("Generated Sudoku puzzle (easy):")
        print_sudoku(puzzle)
        
        puzzle = generate_sudoku('medium')
        self.assertIsNotNone(puzzle)
        print("Generated Sudoku puzzle (medium):")
        print_sudoku(puzzle)
        
        puzzle = generate_sudoku('hard')
        self.assertIsNotNone(puzzle)
        print("Generated Sudoku puzzle (hard):")
        print_sudoku(puzzle)

if __name__ == '__main__':
    unittest.main()
