from collections import deque

import numpy as np

from src.Index import Index
from src.ObserverMixin import ObserverMixin
from src.Solver import Solver


class BfsSolver(Solver,ObserverMixin):

    def __init__(self, board=None):
        self.board = board

    def set_board(self,board):
        self.board = board

    def table_as_tuple(self,board):
        return tuple(map(tuple, board.table))

    def solve(self):
        return self.bfs(self.board)

    def bfs(self,board):
        que = deque()
        for letter in board.get_available_moves():
            board.move(letter)
            que.append((self.table_as_tuple(board), letter))
            board.reverse_move(letter)

        while que:
            og_tab = que.popleft()
            board.table = np.asarray(og_tab[0])
            board.find_empty_index()
            if board.is_solved():
                return og_tab[1]
            for letter in board.get_available_moves():
                if board.move(letter):
                    que.append((self.table_as_tuple(board), og_tab[1] + letter))
                    board.reverse_move(letter)

            board.table = np.asarray(og_tab[0])
