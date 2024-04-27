import numpy as np

from Board import Board
from src.Index import Index

if __name__ == "__main__":
    board = Board()
    board2 = Board()
    board3 = Board()
    board4 = Board()



    board.set_table(np.array([[1, 6, 2, 4], [5, 13, 3, 7], [10, 0, 11, 8], [9, 14, 15, 12]]))
    board2.set_table(np.array([[1,2,3], [4,5,6], [7,0,8]]))
    board3.set_table(np.array([[2,5,3], [1,0,6], [4,7,8]]))
    board3.set_table(np.array([[5,2,7], [8,4,0], [1,3,6]]))
    board4.set_table(np.array([[1, 5, 0], [4, 3, 2], [7, 8, 6]]))
    board4.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))



    board4.bfs()
    print(board3.manhattan_dist())
    print(board3.hamming_dist())
    # print(board4)
