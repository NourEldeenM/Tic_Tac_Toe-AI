WINNING_COMBINATIONS = [
    [[0,0], [0,1], [0,2]],  # Row 1
    [[1,0], [1,1], [1,2]],  # Row 2
    [[2,0], [2,1], [2,2]],  # Row 3
    [[0,0], [1,0], [2,0]],  # Column 1
    [[0,1], [1,1], [2,1]],  # Column 2
    [[0,2], [1,2], [2,2]],  # Column 3
    [[0,0], [1,1], [2,2]],  # Diagonal \
    [[0,2], [1,1], [2,0]],  # Diagonal /
]

class Board:
    def __init__(self):
        self.grid = [['.' for _ in range(3)] for _ in range(3)]
    
    def is_valid_move(self, x, y):
        if (0 <= x < 3 and 0 <= y < 3 and self.grid[x][y] == '.'):
            return True
        return False

    def check_win(self, player):
        for combo in WINNING_COMBINATIONS:
            if all(self.grid[x][y] == player for x,y in combo):
                return True
        return False
    
    def check_draw(self):
        for row in self.grid:
            if '.' in row:
                return False
        return True
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()
        
        
                
            
        
        
                
