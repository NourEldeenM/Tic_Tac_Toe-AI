from board import Board
from ai import best_move

player_name = input("Enter your name: ")
ai_name = "AI"
player_symbol = input("Choose your symbol (X or O): ").upper()
ai_symbol = 'O' if player_symbol == 'X' else 'X'

board = Board()
board.display()
current_player = player_name

while True:
    print(f"{current_player}'s turn")
    
    if current_player == player_name:
        x, y = map(int, input("Enter row and column (0-2): ").split())
        if board.is_valid_move(x, y):
            board.grid[x][y] = player_symbol
        else:
            print("Invalid move. Try again.")
            continue
    else:
        x, y = best_move(board, ai_symbol, player_symbol)
        board.grid[x][y] = ai_symbol
        print(f"AI played at ({x}, {y})")

    board.display()

    if board.check_win(player_symbol if current_player == player_name else ai_symbol):
        print(f"{current_player} wins!")
        break
    if board.check_draw():
        print("It's a draw!")
        break

    current_player = ai_name if current_player == player_name else player_name
