# Week6Day3Lessons5 - Preparation for Project 3
# John Kowal  -  WALTER$
#
def did_I_win_2_down(player, board):
    n = len(board)
    
    for row in range(n - 2):
        for col in range(n - 2):
            if (board[row][col] == player and
                board[0][2] == player and
                board[1][2] == player and
                board[2][2] == player):
                return True
    
    for row in range(n - 2):
        for col in range(2, n):
            if (board[row][col] == player and
                board[0][2] == player and
                board[1][2] == player and
                board[2][2] == player):
                return True

    return False

print(did_I_win_2_down("X", [['O', 'O', 'X'], \
                             ['O', 'X', 'O'], \
                             ['X', 'O', 'O']]))

print(did_I_win_2_down("O", [['O', 'O', 'X'], \
                             ['O', 'X', 'O'], \
                             ['X', 'O', 'O']]))

print(did_I_win_2_down("X", [['O', 'O', 'X'], \
                             ['O', 'O', 'X'], \
                             ['O', 'O', 'X']]))

print(did_I_win_2_down("O", [['O', 'O', 'X'], \
                             ['O', 'O', 'X'], \
                             ['O', 'O', 'X']]))

