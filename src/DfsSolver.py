import time
from Index import Index
from ObservableMixin import ObservableMixin
from Solver import Solver


class DfsSolver(Solver):

    def __init__(self, board=None, max_depth=15):
        super().__init__(board)
        self.max_depth = max_depth

    def set_max_depth(self, depth):
        self.max_depth = depth

    def solve(self):
        self.notify("visited", 1)
        solution = self.dfs(self.board, 0, "")[::-1]
        return solution

    def dfs(self, board, depth, prohibited_move):
        self.notify("depth", depth)
        self.notify("processed", 1)
        if board.is_solved():
            return ""
        if depth < self.max_depth:
            available_moves = board.get_available_moves()
            self.notify("visited", len(available_moves)-1)
            for move in available_moves:
                if move != prohibited_move:
                    board.move(move)
                    temp = self.dfs(board, depth + 1, board.reverse_letter(move))
                    if temp != False:
                        temp += move
                        return temp
                    board.reverse_move(move)
            return False
        return False
