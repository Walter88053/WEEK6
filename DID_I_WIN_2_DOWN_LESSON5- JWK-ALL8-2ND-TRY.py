# Week6Day3Lesson5 - Preparation for Project 3
# John Kowal  -  WALTER$
#
def DID_I_WIN(board, player):
    def check_line(a, b, c):
        return a == b == c == player

    for row in board:
        if check_line(row[0], row[1], row[2]):
            return True

    # Check all columns
    for col in range(3):
        if check_line(board[0][col], board[1][col], board[2][col]):
            return True

    # Check diagonals
    if check_line(board[0][0], board[1][1], board[2][2]):
        return True
    if check_line(board[0][2], board[1][1], board[2][0]):
        return True

    return False

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])

def main():
    boards = [[['X', 'O', 'O']] * 3,
              [['O', 'O', 'X']] * 3,
              [['X', 'O', 'X'], ['O'] * 3, ['O', 'X', 'O']],
              [['O', 'X', 'O'], ['X'] * 3, ['X', 'O', 'X']],
              [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']],
              [['X', 'X', 'O']] * 3]

    for b in boards:
        print()
        print_2D_board(b)
        print()
        print("X won?", DID_I_WIN(b, "X"))
        print("O won?", DID_I_WIN(b, "O"))
        print("=" * 15)

if __name__ == "__main__":
    main()

