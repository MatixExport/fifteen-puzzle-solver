import random
import time

import numpy as np

from src.Index import Index


class Board:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.iteration = 0
        self.table = None
        self.order_str = "UDLR"
        self.empty_field_index = Index(0, 0)
        self.order_dict = {
            "L":self.get_l_move,
            "R":self.get_r_move,
            "D":self.get_d_move,
            "U":self.get_u_move
        }

    def generate_random(self):
        self.table = np.arange(self.width * self.height)
        random.shuffle(self.table)
        self.table = np.reshape(self.table, (self.height, self.width))
        self.find_empty_index()

    def set_order(self,order_str):
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

    def get_available_moves(self):
        temp = {}
        for char in self.order_str:
            self.order_dict[char](temp)
        return temp



    def get_l_move(self,dict):
        if self.empty_field_index.x - 1 >= 0:
            dict["L"] = Index(self.empty_field_index.x - 1, self.empty_field_index.y)


    def get_r_move(self,dict):
        if self.empty_field_index.x + 1 <= self.width - 1:
            dict["R"] = Index(self.empty_field_index.x + 1, self.empty_field_index.y)

    def get_d_move(self,dict):
        if self.empty_field_index.y - 1 >= 0:
            dict["D"] = Index(self.empty_field_index.x, self.empty_field_index.y - 1)

    def get_u_move(self,dict):
        if self.empty_field_index.y + 1 <= self.height - 1:
            dict["U"] = Index(self.empty_field_index.x, self.empty_field_index.y + 1)


    def move(self, index):
        self.table[self.empty_field_index.y, self.empty_field_index.x], self.table[index.y, index.x] = self.table[
            index.y, index.x], self.table[self.empty_field_index.y, self.empty_field_index.x]
        self.empty_field_index = index

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
