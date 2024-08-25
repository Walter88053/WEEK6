# Week6Day3Lesson5 - Preparation for Project 3
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


def check_winner(player, board):
    n = len(board)

    # Check horizontal wins
    for row in range(n):
        if all(board[row][col] == player for col in range(n)):
            return True

    # Check vertical wins
    for col in range(n):
        if all(board[row][col] == player for row in range(n)):
            return True

    # Check diagonal (top-left to bottom-right) win
    if all(board[i][i] == player for i in range(n)):
        return True

    # Check diagonal (top-right to bottom-left) win
    if all(board[i][n - 1 - i] == player for i in range(n)):
        return True

    return False


def test_tictactoe():
    boards = [
        # Player 'X' wins horizontally
        [
            ['X', 'X', 'X'],
            ['O', 'O', ' '],
            [' ', ' ', ' ']
        ],
        # Player 'O' wins vertically
        [
            ['X', 'O', 'X'],
            ['O', 'O', 'O'],
            [' ', 'X', ' ']
        ],
        # Player 'X' wins diagonally (top-left to bottom-right)
        [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', ' ', 'O']
        ],
        # Player 'O' wins diagonally (top-right to bottom-left)
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', ' ', 'X']
        ],
        # Draw (no winner)
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ],
        # Incomplete board
        [
            ['X', ' ', ' '],
            ['O', 'O', ' '],
            [' ', ' ', ' ']
        ]
    ]

    expected_results = [
        True,  # Horizontal win
        True,  # Vertical win
        True,  # Diagonal win (top-left to bottom-right)
        True,  # Diagonal win (top-right to bottom-left)
        False,  # Draw
        False  # Incomplete board (no winner yet)
    ]

    for i, board in enumerate(boards):
        result = check_winner('X', board) or check_winner('O', board)
        print(f"Board {i + 1}: {'Pass' if result == expected_results[i] else 'Fail'}")


# Run the tests
test_tictactoe()
