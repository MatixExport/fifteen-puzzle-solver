from collections import deque

import numpy as np

from Index import Index
from ObservableMixin import ObservableMixin
from Solver import Solver


class BfsSolver(Solver, ObservableMixin):

    def __init__(self, board=None, max_depth=15):
        super().__init__()
        self.board = board
        self.max_depth = max_depth

    def set_board(self, board):
        self.board = board

    def set_max_depth(self, depth):
        self.max_depth = depth

    def table_as_tuple(self, board):
        return tuple(map(tuple, board.table))

    def solve(self):
        return self.bfs(self.board)

    def bfs(self, board):
        depth = 1
        depth_increased = False

        que = deque()
        for letter in board.get_available_moves():
            if board.move(letter):
                que.append((self.table_as_tuple(board), letter))
                board.reverse_move(letter)

        upper_level_nodes = len(que)


        while que:
            og_tab = que.popleft()
            upper_level_nodes -= 1
            if upper_level_nodes == 0:
                depth += 1
                depth_increased = True
            board.table = np.asarray(og_tab[0])
            board.find_empty_index()
            if board.is_solved():
                return og_tab[1]

            if depth >= self.max_depth:
                return False

            for letter in board.get_available_moves():
                if board.move(letter):
                    que.append((self.table_as_tuple(board), og_tab[1] + letter))
                    board.reverse_move(letter)

            if depth_increased:
                upper_level_nodes = len(que)

            board.table = np.asarray(og_tab[0])
