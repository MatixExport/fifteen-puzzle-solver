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
        self.table = np.reshape(self.table, (self.width, self.height))
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
