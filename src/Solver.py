from ObservableMixin import ObservableMixin


class Solver(ObservableMixin):

    def __init__(self,board):
        super().__init__()
        self.board = board

    def set_board(self,board):
        self.board = board

    def solve(self):
        pass
