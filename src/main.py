import argparse

from BfsSolver import BfsSolver
from Board import Board
from DfsSolver import DfsSolver
from AstarSolver import AstarSolver

msg = "Program for finding integral of given functions."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument('Strategy', help='bfs - breadth-first search/dfs - depth-first search/astr - A*')
    parser.add_argument('Parameter', help='Additional parameter for algorithm - '
                                          'A*(hamm, manh) bfs/dfs(permutation of LRUD letters)')
    parser.add_argument('Source', help='Name of file containing starting puzzle')
    parser.add_argument('Output', help='Name of file that the result will be saved to')
    parser.add_argument('Output_info', help='Name of file that will contain additional information')
    parser.add_argument("-d","--depth",type=int, help="max depth, used in dfs and bfs")

    args = parser.parse_args()
    max_depth = 15

    if args.depth:
        max_depth = args.depth

    board = Board()
    board.read_from_file(args.Source)
    output = open(args.Output, "w+")

    if args.Strategy == "dfs":
        board.set_order(args.Parameter)
        solver = DfsSolver(board)
        solver.set_max_depth(max_depth)
        if solution := solver.solve():
            output.write(str(len(solution)) + "\n")
            output.write(solution)
        else:
            output.write("-1")

    if args.Strategy == "bfs":
        board.set_order(args.Parameter)
        solver = BfsSolver(board)
        solver.set_max_depth(max_depth)
        if solution := solver.solve():
            output.write(str(len(solution)) + "\n")
            output.write(solution)
        else:
            output.write("-1")

    if args.Strategy == "astr":
        if args.Parameter == "hamm":
            solver = AstarSolver(board, AstarSolver.hamming_dist)
        else:
            solver = AstarSolver(board, AstarSolver.manhattan_dist)

        if solution := solver.solve():
            output.write(str(len(solution)) + "\n")
            output.write(solution)
            print(board)
        else:
            output.write("-1")
