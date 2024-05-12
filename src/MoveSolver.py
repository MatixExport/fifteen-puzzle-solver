from Solver import Solver


class MoveSolver(Solver):
    def __init__(self, board=None, moves=None):
        self.board = board
        self.moves = moves

    def set_board(self, board):
        self.board = board

    def set_moves(self, moves):
        self.moves = moves

    def solve(self):
        # print(self.moves)
        for move in self.moves:
            # print(move)
            self.board.move(move)
