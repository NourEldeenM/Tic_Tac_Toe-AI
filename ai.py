from board import Board

def evaluate(board: Board, ai_symbol: str, human_symbol: str):
    if board.check_win(ai_symbol):
        return 1
    if board.check_draw():
        return 0
    if board.check_win(human_symbol):
        return -1
    return None


def minimax(board: Board, is_maximizing: bool, ai_symbol: str, human_symbol: str):
    score = evaluate(board, ai_symbol, human_symbol)
    if score is not None:
        return score
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board.grid[i][j] == '.':
                    board.grid[i][j] = ai_symbol
                    score = minimax(board, False, ai_symbol, human_symbol)
                    board.grid[i][j] = '.'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board.grid[i][j] == '.':
                    board.grid[i][j] = human_symbol
                    score = minimax(board, True, ai_symbol, human_symbol)
                    board.grid[i][j] = '.'
                    best_score = min(score, best_score)
        return best_score
        
def best_move(board: Board, ai_player: str, human_player: str):
    best_score = float('-inf')
    move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board.grid[i][j] == '.':
                board.grid[i][j] = ai_player
                score = minimax(board, False, ai_player, human_player)
                board.grid[i][j] = '.'
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move