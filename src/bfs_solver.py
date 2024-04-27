from collections import deque

import numpy as np

from src.Index import Index


def solve(board):
    return bfs2(board)


def bfs(board):
    que = deque()

    for move in board.get_available_moves().values():
        que.append([move])

    while len(que) > 0:
        moves = que.popleft()

        original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
        for move in moves:
            board.move(move)
        if board.is_solved():
            return True
        pos_moves = board.get_available_moves().values()
        if len(pos_moves) > 0:
            for pos_move in pos_moves:
                if pos_move != original_position:
                    moves.append(pos_move)
                    que.append(moves)
                    moves = moves[:-1]

        for move in reversed(moves):
            board.move(move)


def table_as_tuple(board):
    return tuple(map(tuple, board.table))


def bfs2(board):
    que = deque()
    for letter,move in board.get_available_moves().items():
        original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
        board.move(move)
        que.append((table_as_tuple(board), letter))
        board.move(original_position)

    while que:
        og_tab = que.popleft()
        board.table = np.asarray(og_tab[0])
        board.find_empty_index()
        original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
        if board.is_solved():
            return og_tab[1]
        pos_moves = board.get_available_moves()
        if len(pos_moves.values()) > 0:
            for letter,pos_move in pos_moves.items():
                if pos_move != original_position:
                    original_position2 = Index(board.empty_field_index.x, board.empty_field_index.y)
                    board.move(pos_move)
                    que.append((table_as_tuple(board), og_tab[1] + letter))
                    board.move(original_position2)

        board.table = np.asarray(og_tab[0])