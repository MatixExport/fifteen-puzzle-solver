import numpy as np

from Board import Board
from src.Index import Index

if __name__ == "__main__":
    board = Board(4, 4)
    board2 = Board(3, 3)
    board3 = Board(3, 3)



    board.set_table(np.array([[1, 6, 2, 4], [5, 13, 3, 7], [10, 0, 11, 8], [9, 14, 15, 12]]))
    board2.set_table(np.array([[1,2,3], [4,5,6], [7,0,8]]))
    board3.set_table(np.array([[2,5,3], [1,0,6], [4,7,8]]))


    board3.bfs()
    print(board3)
