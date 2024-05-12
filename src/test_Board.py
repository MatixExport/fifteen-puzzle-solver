from unittest import TestCase

import numpy as np

from AstarSolver import AstarSolver
from BfsSolver import BfsSolver
from Board import Board
from DfsSolver import DfsSolver
from MoveSolver import MoveSolver
from src.Logger import Logger


class TestBoard(TestCase):
    def test_dfs(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        DfsSolver(board2).solve()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        DfsSolver(board1).solve()
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]), board1.table)

    def test_bfs(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        BfsSolver(board2).solve()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        BfsSolver(board1).solve()
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)

    def test_ast_humming(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))

        AstarSolver(board2, AstarSolver.hamming_dist).solve()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        AstarSolver(board1, AstarSolver.hamming_dist).solve()
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)

    def test_ast_manhattan(self):
        board1 = Board()
        board2 = Board()
        board1.set_table(np.array([[1, 2, 3, 4], [5, 6, 11, 7], [9, 10, 0, 8], [13, 14, 15, 12]]))
        board2.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))

        AstarSolver(board2, AstarSolver.manhattan_dist).solve()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board2.table)

        AstarSolver(board1, AstarSolver.manhattan_dist).solve()
        assert np.array_equal(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]),
                              board1.table)

    def test_board(self):
        board = Board()
        board.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        board.move("L")
        assert np.array_equal(np.array([[0, 1, 5], [4, 3, 2], [7, 8, 6]]), board.table)
        board.reverse_move("L")
        assert np.array_equal(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]), board.table)

    def is_solution(self, initial_board, solution):
        solver = MoveSolver(initial_board, solution)
        solver.solve()
        assert initial_board.is_solved() == True

    def solver_test(self,solver):
        board = Board()
        test_board = Board()
        test_board.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        board.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        solver.set_board(board)
        solution = solver.solve()
        assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), board.table)
        self.is_solution(test_board, solution)

    def test_classes(self):
        self.solver_test(BfsSolver())
        self.solver_test(AstarSolver(None,AstarSolver.manhattan_dist))
        self.solver_test(AstarSolver(None, AstarSolver.hamming_dist))
        self.solver_test(DfsSolver())

    def test_logger(self):
        board = Board()
        board.set_table(np.array([[1, 0, 5], [4, 3, 2], [7, 8, 6]]))
        solver = AstarSolver(board,AstarSolver.manhattan_dist)
        logger = Logger()
        logger.set_solver(solver)
        logger.recorded_solve()
        print(logger.elapsed_time)

    def test_asymmetrical_boards(self):
        board = Board()
        board.set_table(np.array([[1, 2], [0, 4], [3, 5]]))
        solver = AstarSolver(board, AstarSolver.hamming_dist)
        solver.set_board(board)
        solver.solve()
        assert np.array_equal(np.array([[1, 2], [3, 4], [5, 0]]), board.table)



