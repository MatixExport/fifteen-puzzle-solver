from collections import deque

import numpy as np

from Index import Index
from ObservableMixin import ObservableMixin
from Solver import Solver


class BfsSolver(Solver, ObservableMixin):

    def __init__(self, board=None):
        super().__init__()
        self.board = board

    def set_board(self,board):
        self.board = board

    def table_as_tuple(self,board):
        return tuple(map(tuple, board.table))

    def solve(self):
        return self.bfs(self.board)

    def bfs(self,board):
        print(board.table)
        que = deque()
        for letter in board.get_available_moves():
            if board.move(letter):
                que.append((self.table_as_tuple(board), letter))
                board.reverse_move(letter)

        while que:
            og_tab = que.popleft()
            board.table = np.asarray(og_tab[0])
            board.find_empty_index()
            if board.is_solved():
                print(og_tab[0])
                print(og_tab[1])
                return og_tab[1]
            for letter in board.get_available_moves():
                if board.move(letter):
                    que.append((self.table_as_tuple(board), og_tab[1] + letter))
                    board.reverse_move(letter)

            board.table = np.asarray(og_tab[0])
