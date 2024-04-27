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


def a_star(self, h):
    start = [self.empty_field_index]
    open_set = PriorityQueue()
    open_set.put((h(self), start))
    # cena dotarcia do danego stanu boarda
    gscore = {str(self.table.flatten()): 0}
    # cena dotarcia do danego stanu boarda + przewidywana cena dojścia od tego stanu do końca
    fscore = {str(self.table.flatten()): h(self)}

    while not open_set.empty():
        current = open_set.get()[1]
        self.make_moves(current)

        if self.is_solved():
            self.reverse_moves(current)
            result_string = ""
            for move in current[1:]:
                dic = self.get_available_moves()
                value = list(dic.keys())[list(dic.values()).index(move)]
                self.move(move)
                result_string += value
            return result_string

        current_gscore = gscore[str(self.table.flatten())]

        for move in self.get_available_moves().values():

            original_position = Index(self.empty_field_index.x, self.empty_field_index.y)
            self.move(move)

            path = copy.deepcopy(current).copy()
            path.append(move)

            if not str(self.table.flatten()) in gscore:
                gscore[str(self.table.flatten())] = float('inf')

            neighbour_gscore = current_gscore + 1
            if neighbour_gscore < gscore[str(self.table.flatten())]:
                gscore[str(self.table.flatten())] = neighbour_gscore
                fscore[str(self.table.flatten())] = neighbour_gscore + h(self)

                open_set.put((neighbour_gscore + h(self), path))

            self.move(original_position)

        self.reverse_moves(current)
    return False
