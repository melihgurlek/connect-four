# Created a list to represent board
# The reason it's sideways because when adding pieces we'll input board[x][y]
# If it wasn't sideways it would've been board[y][x]
# Also it's counter clockwise sideways so the bottom is the last place not 0
#    board = [[" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " "]]


# Printed the column numbers and top line of the board
def print_board(board):
    column_label = " "
    for label_num in range(1, len(board)+1):
        column_label += " " + str(label_num) + "  "
    print(column_label)
    print("+---" * (len(board)) + "+")

    # Prints rows
    for row in range(len(board[0])):

        row_with_pieces = ""
        for col in range(len(board)):
            row_with_pieces += ('| '+str(board[col][row])) + ' '
        print(row_with_pieces + '|')

        print('+---' * (len(board)) + '+')

# Function to check if the move is illegal


def illegal_move_check(board, move):

    # Column doesn't exist
    if move < 1 or move > (len(board)):
        return True

    # Column is full
    if board[move-1][0] != " ":
        return True

    return False


def select_position(board, column, player):
    # Checks if the move is illegal
    if illegal_move_check(board, column):
        print("Placing an " + player + " in column " +
              str(column) + " is illegal")
        print("Please select an empty column in a valid range (1-" + str(len(board)) + ")")
        print()
        return False

    # Check if the piece (character) is valid which is an X or O
    if player != "X" and player != "O":
        print("Invalid piece selection")
        print("Please use either an 'X' or an 'O' as your piece")
        print()
        return False

    # Places a piece at the bottom of the column
    for y in range(len(board[0])-1, -1, -1):
        if board[column-1][y] == ' ':
            board[column-1][y] = player
            print("Placed an " + player + " in column " + str(column))
            print()
            return True
    return False


def available_moves(board):
    # Returns columns that aren't full
    moves = []
    for i in range(1, len(board)+1):
        if not illegal_move_check(board, i):
            moves.append(i)
    return moves


def has_won(board, char):
    # Horizontal win check
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == char and board[x+1][y] == char and board[x+2][y] == char and board[x+3][y] == char:
                return True

    # Vertical win check
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == char and board[x][y+1] == char and board[x][y+2] == char and board[x][y+3] == char:
                return True

    # Diagonal win check up and right
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == char and board[x+1][y-1] == char and board[x+2][y-2] == char and board[x+3][y-3] == char:
                return True

    # Diagonal win check down and right
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == char and board[x+1][y+1] == char and board[x+2][y+2] == char and board[x+3][y+3] == char:
                return True

    return False


def end_of_game(board):
    # If True game is over
    return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0


def play_game():
    # Create board
    game_board = []
    for col in range(7):
        game_board.append([" "] * 6)

    # Start of game X is player one
    turn = "X"
    winner = False

    while(not end_of_game(game_board)):
        print_board(game_board)
        move = 0
        available = available_moves(game_board)

        # Asking for a legal move
        while(move not in available):
            move = int(input(
                "It is " + turn + "'s turn. Select a column out this options" + str(available)))

        select_position(game_board, turn)

        # Checks if one side wins the game
        if has_won(game_board, turn):
            print(turn + "won the game, congrats")
            print_board(game_board)
            winner = True
            break

        # Turn change
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    if not winner:
        print("It's a tie. Was a fantastic game.")
        print_board(game_board)


play_game()
