import numpy as np

from Board import Board
from src.Index import Index

if __name__ == "__main__":
    board = Board(4, 4)

    board.generate_random()

    board.set_table(np.array([[1, 6, 2, 4], [5, 13, 3, 7], [10, 0, 11, 8], [9, 14, 15, 12]]))
    print(board.is_solved())

    board.depth_recursion(0, Index(0, 0))

    print(board.is_solved())
    print(board)
