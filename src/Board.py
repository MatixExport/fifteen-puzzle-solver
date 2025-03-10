import random
import time

import numpy as np

from Index import Index


class Board:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.table = None
        self.order_str = "UDLR"
        self.empty_field_index = Index(0, 0)
        self.order_dict = {
            "L": self.get_l_move,
            "R": self.get_r_move,
            "D": self.get_d_move,
            "U": self.get_u_move
        }
        self.reverse_dict = {
            "L": "R",
            "R": "L",
            "U": "D",
            "D": "U"

        }

    def set_order(self, order_str):
        self.order_str = str.upper(order_str)

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

    # It is used only in dfs
    # and only to simulate visiting nodes
    # and its horrible
    def get_available_moves(self):
        moves = []
        for letter in self.order_str:
            if self.order_dict[letter]():
                moves.append(letter)
        return moves

    def get_all_moves(self):
        return self.order_str

    def get_l_move(self):
        if self.empty_field_index.x - 1 >= 0:
            return Index(self.empty_field_index.x - 1, self.empty_field_index.y)
        return None

    def get_r_move(self):
        if self.empty_field_index.x + 1 <= self.width - 1:
            return Index(self.empty_field_index.x + 1, self.empty_field_index.y)
        return None

    def get_u_move(self):
        if self.empty_field_index.y - 1 >= 0:
            return Index(self.empty_field_index.x, self.empty_field_index.y - 1)
        return None

    def get_d_move(self):
        if self.empty_field_index.y + 1 <= self.height - 1:
            return Index(self.empty_field_index.x, self.empty_field_index.y + 1)
        return None

    def move(self, letter):
        index = self.order_dict[letter]()
        if index:
            self.table[self.empty_field_index.y, self.empty_field_index.x], self.table[index.y, index.x] = self.table[
                index.y, index.x], self.table[self.empty_field_index.y, self.empty_field_index.x]
            self.empty_field_index = index
            return True
        return False

    def reverse_move(self, letter):
        self.move(self.reverse_letter(letter))

    def reverse_letter(self, letter):
        return self.reverse_dict[letter]

    def make_moves(self, moves):
        for move in moves:
            self.move(move)

    def reverse_moves(self, moves):
        for move in reversed(moves):
            self.move(move)

    def is_solved(self):
        temp = np.reshape(self.table, (self.width * self.height))
        if temp[-1] == 0:
            return np.all(temp[:-2] < temp[1:-1])
        return False

    def read_from_file(self, filename):
        file = open(filename)
        first = file.readline().strip().split()
        self.height = int(first[0])
        self.width = int(first[1])

        temp_array = []

        for line in file:
            temp_row = []
            for x in line.strip().split():
                temp_row.append(int(x))
            temp_array.append(temp_row)
        file.close()

        self.table = np.array(temp_array)
        self.find_empty_index()
