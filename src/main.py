import numpy as np

from Board import Board

if __name__ == "__main__":
    board = Board(2,2)

    board.generate_random()
    # print(board)
    # print(board.find_empty_index())
    # print(board.get_available_moves())
    # print(board.move(1,1))
    board.set_table(np.array([[2,3],[ 1,0]]))
    print(board)
    print(board.is_solved())