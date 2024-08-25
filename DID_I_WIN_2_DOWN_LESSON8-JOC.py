# Week6Day3Lesson8 - Preparation for Project 3
# John Kowal  -  WALTER$
#
def did_I_win_2_down(player, board):
    did_win = True
    for i in range(len(board)):
        col_win = True
        for x in range (len(board[i])):
            col_win &= player == board[x][i]
        print("\t", i, col_win, "or", did_win)
        did_win = col_win # did_win = did_win or col_win
    return did_win

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])




def main():
    boards = [[['X', 'O', 'O']] * 3,
              [['X', 'O', 'X'], ['O'] * 3,  ['O', 'X', 'O']],
              [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']],
              [['O', 'O', 'X']] * 3]

    for b in boards:
        print()
        print_2D_board(b)
        print()
        print("X won?",did_I_win_2_down("X", b))
        print("O won?",did_I_win_2_down("O", b))
        print("=" * 15)

if __name__ == "__main__":
    main()
