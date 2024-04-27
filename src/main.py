import numpy as np

from Board import Board
from src.Index import Index

if __name__ == "__main__":
    board = Board(2, 2)

    board.generate_random()

    board.set_table(np.array([[1,3], [2, 0]]))
    print(board.is_solved())

    board.recurse(1,None)

    print(board)
    print(board.is_solved())
