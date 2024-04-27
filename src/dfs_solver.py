from src.Index import Index

def solve(board):
    return dfs(board,0,None)

def dfs(board, depth, prohibited_move):
    if board.is_solved():
        return True
    if depth < 15:
        for move in board.get_available_moves().values():
            if move != prohibited_move:
                original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
                board.move(move)
                if dfs(board,depth + 1, original_position):
                    return True
                board.move(original_position)

        return False
    return False