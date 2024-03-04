import random

import numpy as np


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.iteration = 0
        self.table = None
        self.empty_field_index = None

    def generate_random(self):
        self.table = np.arange(16)
        random.shuffle(self.table)
        self.table = np.reshape(self.table, (self.width, self.height))
        self.find_empty_index()

    def find_empty_index(self):
        self.empty_field_index = np.where(self.table == 0)
        return self.empty_field_index

    def __str__(self):
        return str(self.table)

    def get_available_moves(self):
        temp = []
        if self.empty_field_index[0] - 1 >= 0:
            temp.append((self.empty_field_index[0] - 1, self.empty_field_index[1]))
        if self.empty_field_index[0] + 1 <= self.height - 1:
            temp.append((self.empty_field_index[0] + 1, self.empty_field_index[1]))
        if self.empty_field_index[1] - 1 >= 0:
            temp.append((self.empty_field_index[0], self.empty_field_index[1] - 1))
        if self.empty_field_index[1] + 1 <= self.width - 1:
            temp.append((self.empty_field_index[0],  self.empty_field_index[1] + 1))

        return temp