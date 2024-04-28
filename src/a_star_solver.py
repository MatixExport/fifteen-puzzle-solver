import copy
import math
from queue import PriorityQueue

import numpy as np

from src.Index import Index


def hamming_dist(self):
    temp = np.reshape(self.table, (self.width * self.height))
    solved = [i for i in range(len(temp) - 1)]
    solved.append(0)
    hamming = 0
    for i, j in zip(solved, temp):
        if i != j:
            hamming += 1
    return hamming


def manhattan_dist(self):
    sum = 0
    for row in range(self.height):
        for col in range(self.width):
            val = self.table[row][col]
            correct_row = math.ceil(val / self.height) - 1
            correct_col = (val - correct_row * self.height) - 1
            if val == 0:
                correct_row = self.height - 1
                correct_col = self.width - 1
            sum += abs(correct_row - row) + abs(correct_col - col)
    return sum


def table_as_tuple(table):
    return tuple(map(tuple, table))


def a_star(board, h):
    open_set = PriorityQueue()
    open_set.put((h(board), table_as_tuple(board.table), ""))
    # cena dotarcia do danego stanu boarda
    gscore = {table_as_tuple(board.table): 0}
    # cena dotarcia do danego stanu boarda + przewidywana cena dojścia od tego stanu do końca

    while not open_set.empty():
        current_tuple = open_set.get()
        current = current_tuple[1]
        board.set_table(np.asarray(current))

        if board.is_solved():
            return current_tuple[2]

        current_gscore = gscore[current]

        for move in board.get_available_moves():

            if board.move(move):

                neighbour_tuple = table_as_tuple(board.table)
                neighbour_gscore = current_gscore + 1
                if (not neighbour_tuple in gscore) or (neighbour_gscore < gscore[neighbour_tuple]):
                    gscore[neighbour_tuple] = neighbour_gscore
                    open_set.put((neighbour_gscore + h(board), neighbour_tuple, current_tuple[2] + (move)))
                board.reverse_move(move)
        board.set_table(np.asarray(current))
    return False
