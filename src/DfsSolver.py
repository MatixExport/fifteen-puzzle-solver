import time
from src.Index import Index
from src.ObserverMixin import ObserverMixin
from src.Solver import Solver


class DfsSolver(Solver,ObserverMixin):

    def __init__(self, board=None):
        self.board = board

    def set_board(self, board):
        self.board = board

    def solve(self):
        return self.dfs(self.board, 0, None)

    def dfs(self, board, depth, prohibited_move):
        if board.is_solved():
            return []
        if depth < 15:
            for move in board.get_available_moves():
                if move != prohibited_move:
                    if board.move(move):
                        temp = self.dfs(board, depth + 1, board.reverse_letter(move))
                        if temp != False:
                            temp.append(prohibited_move)
                            return reversed(temp) if depth == 0 else temp
                        board.reverse_move(move)

            return False
        return False
