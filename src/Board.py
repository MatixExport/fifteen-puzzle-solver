import random

import numpy as np
from collections import deque

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

    def depth_recursion(self, depth, prohibited_move):
        if self.is_solved():
            return True
        # i=0
        if depth < 15:
            for move in self.get_available_moves().values():
                # print(i)
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

    def check_level(self, prohibited_move):
        for move in self.get_available_moves().values():
            if move != prohibited_move:
                original_position = Index(self.empty_field_index.x, self.empty_field_index.y)
                self.move(move)

                if self.is_solved():
                    return True
                self.move(original_position)

        return False

    def wide_search(self, prohibited_move):
        if self.is_solved():
            return True

        if self.check_level(prohibited_move):
            return True

        for move in self.get_available_moves().values():
            original_position = Index(self.empty_field_index.x, self.empty_field_index.y)
            self.move(move)

            if self.check_level(original_position):
                return True
            self.move(original_position)

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

