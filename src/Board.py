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
        temp = {}
        if self.empty_field_index.x - 1 >= 0:
            temp["L"] = (self.empty_field_index.x - 1, self.empty_field_index.y)
        if self.empty_field_index.x + 1 <= self.width - 1:
            temp["R"] = (self.empty_field_index.x + 1, self.empty_field_index.y)
        if self.empty_field_index.y - 1 >= 0:
            temp["D"] = (self.empty_field_index.x, self.empty_field_index.y - 1)
        if self.empty_field_index.y + 1 <= self.height - 1:
            temp["U"] = (self.empty_field_index.x, self.empty_field_index.y + 1)

        return temp

    def move(self, x, y):
        self.find_empty_index()
        self.table[self.empty_field_index.y, self.empty_field_index.x], self.table[y,x] = self.table[y,x], self.table[self.empty_field_index.y, self.empty_field_index.x]

    def is_solved(self):
        self.find_empty_index()

        if not np.all(self.table[:-1,0] < self.table[1:,0]):
            return False
        for row in self.table[:-1]:
            if not np.all(row[:-1] < row[1:]):
                return False
        if self.table[-1,-1] == 0:
            last_row = self.table[-1]
            return np.all(last_row[:-2] < last_row[1:-1])
        return False



    def recurse(self, depth):
        if depth == 20:
            return False