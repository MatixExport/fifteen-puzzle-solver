import time

from src.Index import Index
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print('%r  %2.22f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def solve(board):
    return dfs(board,0,None)

def dfs(board, depth, prohibited_move):
    if board.is_solved():
        return []
    if depth < 15:
        for move in board.get_available_moves().values():
            if move != prohibited_move:
                original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
                board.move(move)
                temp = dfs(board,depth + 1, original_position)
                if temp != False:
                    temp.append(prohibited_move)
                    return reversed(temp) if depth == 0 else temp
                board.move(original_position)

        return False
    return False