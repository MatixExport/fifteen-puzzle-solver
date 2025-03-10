from collections import deque

import numpy as np

from Solver import Solver


class BfsSolver(Solver):

    def __init__(self, board=None, max_depth=15):
        super().__init__(board)
        self.max_depth = max_depth

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
        for letter in board.get_all_moves():
            if board.move(letter):
                que.append((self.table_as_tuple(board), letter))
                board.reverse_move(letter)
        upper_level_nodes = len(que)

        self.notify("processed", 1)
        self.notify("visited", upper_level_nodes + 1)
        self.notify("depth", depth)

        while que:
            og_tab = que.popleft()
            board.table = np.asarray(og_tab[0])
            self.notify("processed", 1)
            if board.is_solved():
                return og_tab[1]
            upper_level_nodes -= 1
            if upper_level_nodes == 0:
                depth += 1
                self.notify("depth", depth)
                depth_increased = True

            board.find_empty_index()

            if depth > self.max_depth:
                return False

            for letter in board.get_all_moves():
                if board.reverse_letter(letter) != og_tab[1][-1]:
                    if board.move(letter):
                        self.notify("visited", 1)
                        que.append((self.table_as_tuple(board), og_tab[1] + letter))
                        board.reverse_move(letter)

            if depth_increased:
                upper_level_nodes = len(que)
                depth_increased = False


            board.table = np.asarray(og_tab[0])
