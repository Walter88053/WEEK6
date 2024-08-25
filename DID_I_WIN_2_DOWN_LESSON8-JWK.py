# Week6Day3Lesson8 - Preparation for Project 3
# John Kowal  -  WALTER$
#
def did_I_win_2_down(player, board):
    for i in range(len(board)):
        if all(board[x][i] == player for x in range(len(board))):
            return True
        else:
            return False

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
