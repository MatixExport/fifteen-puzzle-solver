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
        temp = np.reshape(self.table, (self.width * self.height))
        if temp[-1] == 0:
            return np.all(temp[:-2] < temp[1:-1])
        return False


    def recurse(self, depth, prohibited_move):
        if self.is_solved():
            return True
        # i=0
        if depth < 15:
            for move in self.get_available_moves().values():
                if move != prohibited_move:
                    # i+=1
                    # print(self)
                    self.move(move)
                    # print("Robie Ruch: z",self.empty_field_index)
                    # print("Do: ",move)
                    original_position = Index(self.empty_field_index.x, self.empty_field_index.y)

                    if self.depth_recursion(depth + 1, original_position):
                        return True
                    # print("Odwracam Ruch do", original_position, "\n")
                    self.move(original_position)
                    #
                    # print(self)
                # else:
                #     print("Move prohibited: ", prohibited_move)
            return False
        return False
