import random

import numpy as np

from src.Index import Index


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.iteration = 0
        self.table = None
        self.empty_field_index = Index(0, 0)

    def generate_random(self):
        self.table = np.arange(self.width * self.height)
        random.shuffle(self.table)
        self.table = np.reshape(self.table, (self.height, self.width))
        self.find_empty_index()

    def set_table(self, table):
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
        self.find_empty_index()
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
        self.find_empty_index()
        self.table[self.empty_field_index.y, self.empty_field_index.x], self.table[index.y, index.x] = self.table[
            index.y, index.x], self.table[self.empty_field_index.y, self.empty_field_index.x]

    def is_solved(self):
        # if not np.all(self.table[:-1,0] < self.table[1:,0]):
        #     return False
        # for row in self.table[:-1]:
        #     if not np.all(row[:-1] < row[1:]):
        #         return False
        # if self.table[-1,-1] == 0:
        #     last_row = self.table[-1]
        #     return np.all(last_row[:-2] < last_row[1:-1])
        # return False
        temp = np.reshape(self.table, (self.width * self.height))
        if temp[-1] == 0:
            return np.all(temp[:-2] < temp[1:-1])
        return False

    def recurse(self, depth, prohibited_move):
        if self.is_solved():
            return True
        if depth < 2:
            for move in self.get_available_moves().values():
                if move != prohibited_move:
                    print("rect")
                    print(self)
                    self.move(move)
                    if self.recurse(depth + 1, self.empty_field_index):
                        return True
                    self.move(self.empty_field_index)
                    print(self)
            return False
        return False
