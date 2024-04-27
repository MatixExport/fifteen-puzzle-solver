from src.Index import Index

def solve(board):
    return dfs(board,0,None)

def dfs(board, depth, prohibited_move):
    if board.is_solved():
        return True
    # i=0
    if depth < 15:
        for move in board.get_available_moves().values():
            # print(i)
            if move != prohibited_move:
                # i+=1
                # print(self)
                original_position = Index(board.empty_field_index.x, board.empty_field_index.y)
                board.move(move)
                # print("Robie Ruch: z",self.empty_field_index)
                # print("Do: ",move)

                if dfs(board,depth + 1, original_position, ):
                    return True
                # print("Odwracam Ruch do", original_position, "\n")
                board.move(original_position)
                #
                # print(self)
            # else:
            #     print("Move prohibited: ", prohibited_move)
        return False
    return False