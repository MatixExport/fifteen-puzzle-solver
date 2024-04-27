from unittest import TestCase

import numpy as np

from src.Board import Board
from src.Index import Index
import dfs_solver


class TestBoard(TestCase):
    def test_dfs(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        dfs_solver.solve(board2)
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) , board2.table)

        dfs_solver.solve(board1)
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]) , board1.table)\


    def test_bfs(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        board2.bfs2()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        board1.bfs2()
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)


    def test_ast_humming(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))

        board2.a_star(board2.hamming_dist)
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        board1.a_star(board1.hamming_dist)
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)


    def test_ast_manhattan(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))

        board2.a_star(board2.manhattan_dist)
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        board1.a_star(board1.manhattan_dist)
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)



