import copy
import math
import random

import numpy as np
from collections import deque
import heapq
from queue import PriorityQueue

from src.Index import Index


class Board:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.iteration = 0
        self.table = None
        self.empty_field_index = Index(0, 0)

    def generate_random(self):
        self.table = np.arange(self.width * self.height)
        random.shuffle(self.table)
        self.table = np.reshape(self.table, (self.height, self.width))
        self.find_empty_index()

    def set_table(self, table):
        self.height = len(table)
        self.width = len(table[0])
        self.table = table
        self.find_empty_index()

    def find_empty_index(self):
        empty_field_index = np.where(self.table == 0)
        self.empty_field_index.y = empty_field_index[0][0]
        self.empty_field_index.x = empty_field_index[1][0]
        return self.empty_field_index

    def __str__(self):
        return str(self.table)

    def get_available_moves(self):
        temp = {}
        if self.empty_field_index.x - 1 >= 0:
            temp["L"] = Index(self.empty_field_index.x - 1, self.empty_field_index.y)
        if self.empty_field_index.x + 1 <= self.width - 1:
            temp["R"] = Index(self.empty_field_index.x + 1, self.empty_field_index.y)
        if self.empty_field_index.y - 1 >= 0:
            temp["D"] = Index(self.empty_field_index.x, self.empty_field_index.y - 1)
        if self.empty_field_index.y + 1 <= self.height - 1:
            temp["U"] = Index(self.empty_field_index.x, self.empty_field_index.y + 1)

        return temp

    def move(self, index):
        self.table[self.empty_field_index.y, self.empty_field_index.x], self.table[index.y, index.x] = self.table[
            index.y, index.x], self.table[self.empty_field_index.y, self.empty_field_index.x]
        self.empty_field_index = index

    def is_solved(self):
        temp = np.reshape(self.table, (self.width * self.height))
        if temp[-1] == 0:
            return np.all(temp[:-2] < temp[1:-1])
        return False





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



    def bfs(self):
        que = deque()

        for move in self.get_available_moves().values():
            que.append([move])

        while len(que) > 0:
            moves = que.popleft()

            original_position = Index(self.empty_field_index.x, self.empty_field_index.y)
            for move in moves:
                self.move(move)
            if self.is_solved():
                return True
            pos_moves = self.get_available_moves().values()
            if len(pos_moves) > 0:
                for pos_move in pos_moves:
                    if pos_move != original_position:
                        moves.append(pos_move)
                        que.append(moves)
                        moves = moves[:-1]

            for move in reversed(moves):
                self.move(move)

    def make_moves(self, moves):
        for move in moves:
            self.move(move)

    def reverse_moves(self, moves):
        for move in reversed(moves):
            self.move(move)





    def a_star(self, h):
        start = [self.empty_field_index]
        open_set = PriorityQueue()
        open_set.put((h(),start))
        # cena dotarcia do danego stanu boarda
        gscore = {str(self.table.flatten()): 0}
        # cena dotarcia do danego stanu boarda + przewidywana cena dojścia od tego stanu do końca
        fscore = {str(self.table.flatten()): h()}

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
                    fscore[str(self.table.flatten())] = neighbour_gscore + h()

                    open_set.put((neighbour_gscore + h(),path))

                self.move(original_position)

            self.reverse_moves(current)
        return False
