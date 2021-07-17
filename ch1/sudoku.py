from dokusan import generators
import numpy as np


class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.blocks = {}
        block = []
        i = 0
        j = 0
        block_count = 1
        # import pdb
        # pdb.set_trace()
        while j <= len(grid) - 3:
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    block.append((row, col))
            self.blocks[str(block_count)] = tuple(block)
            block = []
            block_count += 1
            i += 3
            if i == 9:
                i = 0
                j += 3

    def find_row(self, i):
        return self.grid[i]

    def find_col(self, j):
        return [row[j] for row in self.grid]

    def find_block(self, i, j):
        block_values = []
        for block in self.blocks.values():
            if (i, j) in block:
                for coordinate in block:
                    block_values.append(
                        self.grid[coordinate[0]][coordinate[1]])
                return block_values

    def get_grid(self):
        return self.grid

    def __str__(self):
        return str(self.grid)


class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.grid[i][j] == '0':
                    for num in self.possible(i, j):
                        self.sudoku.grid[i][j] = str(num)
                        self.solve()
                        self.sudoku.grid[i][j] = '0'
                    return
        print('Answer:', self.sudoku, sep='\n')

    @ staticmethod
    def check_row(row):
        return [i for i in range(1, 10) if str(i) not in row]

    @ staticmethod
    def check_col(col):
        return [i for i in range(1, 10) if str(i) not in col]

    @ staticmethod
    def check_sqr(sqr):
        return [i for i in range(1, 10) if str(i) not in sqr]

    def possible(self, i, j):
        row_possible = set(self.check_row(self.sudoku.find_row(i)))
        col_possible = set(self.check_col(self.sudoku.find_col(j)))
        block_possible = set(self.check_sqr(
            self.sudoku.find_block(i, j)))
        possible_num = row_possible.intersection(
            col_possible, block_possible)
        return possible_num


grid = np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9, 9)
my_sudoku = Sudoku(grid)
solver = SudokuSolver(my_sudoku)
print(grid, end='\n\n\n')
solver.solve()
