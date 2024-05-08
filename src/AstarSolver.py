import copy
import math
from queue import PriorityQueue

import numpy as np

from ObservableMixin import ObservableMixin
from Solver import Solver


class AstarSolver(Solver, ObservableMixin):

    def __init__(self, board=None, heuristic=None):
        super().__init__()
        self.board = board
        self.heuristic = heuristic
        if self.heuristic is None:
            self.heuristic = AstarSolver.manhattan_dist

    def set_board(self, board):
        self.board = board

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    @staticmethod
    def hamming_dist(board):
        temp = np.reshape(board.table, (board.width * board.height))
        solved = [i for i in range(len(temp) - 1)]
        solved.append(0)
        hamming = 0
        for i, j in zip(solved, temp):
            if i != j:
                hamming += 1
        return hamming

    @staticmethod
    def manhattan_dist(board):
        sum = 0
        for row in range(board.height):
            for col in range(board.width):
                val = board.table[row][col]
                correct_row = math.ceil(val / board.height) - 1
                correct_col = (val - correct_row * board.height) - 1
                if val == 0:
                    correct_row = board.height - 1
                    correct_col = board.width - 1
                sum += abs(correct_row - row) + abs(correct_col - col)
        return sum

    def table_as_tuple(self, table):
        return tuple(map(tuple, table))

    def solve(self):
        return self.astar(self.board, self.heuristic)

    def astar(self, board, h):
        open_set = PriorityQueue()
        open_set.put((h(board), self.table_as_tuple(board.table), ""))
        self.notify("visited", 1)
        # cena dotarcia do danego stanu boarda
        gscore = {self.table_as_tuple(board.table): 0}
        # cena dotarcia do danego stanu boarda + przewidywana cena dojścia od tego stanu do końca

        while not open_set.empty():
            current_tuple = open_set.get()
            self.notify("processed", 1)
            current_board = current_tuple[1]
            board.set_table(np.asarray(current_board))

            if board.is_solved():
                return current_tuple[2]

            current_gscore = gscore[current_board]

            for move in board.get_all_moves():

                if board.move(move):

                    neighbour_tuple = self.table_as_tuple(board.table)
                    neighbour_gscore = current_gscore + 1
                    if (neighbour_tuple not in gscore) or (neighbour_gscore < gscore[neighbour_tuple]):
                        gscore[neighbour_tuple] = neighbour_gscore
                        self.notify("visited", 1)
                        path = current_tuple[2] + move
                        self.notify("depth",len(path))
                        open_set.put((neighbour_gscore + h(board), neighbour_tuple, path))
                    board.reverse_move(move)
            board.set_table(np.asarray(current_board))
        return False
