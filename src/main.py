import numpy as np

from Board import Board

if __name__ == "__main__":
    board = Board(4,4)

    board.generate_random()
    print(board)
    print(board.find_empty_index())
    print(board.get_available_moves())