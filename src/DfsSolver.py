import time
from Index import Index
from ObservableMixin import ObservableMixin
from Solver import Solver


class DfsSolver(Solver,ObservableMixin):

    def __init__(self, board=None):
        super().__init__()
        self.board = board

    def set_board(self, board):
        self.board = board

    def solve(self):
        solution = self.dfs(self.board, 0, "")[::-1]
        return solution

    def dfs(self, board, depth, prohibited_move):
        if board.is_solved():
            return ""
        if depth < 15:
            for move in board.get_available_moves():
                if move != prohibited_move:
                    if board.move(move):
                        temp = self.dfs(board, depth + 1, board.reverse_letter(move))
                        if temp != False:
                            temp += move
                            return temp
                        board.reverse_move(move)

            return False
        return False
