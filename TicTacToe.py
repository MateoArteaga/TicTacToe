"""
Introduction: Ponder and Prove
Author: Mateo Arteaga
"""

#to see the playing board
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()
#to end the main loop
def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing!")
        return True
    else: return False    
#to check if input is valid
def check_input(user_input):
    # Check if input is a number
    if not isnumber(user_input): return False
    user_input = int(user_input)
    # Check if input is between 1 and 9
    if not inbounds(user_input): return False
    return True

def isnumber(user_input):
    if not user_input.isnumeric():
        print("That is not a number")
        return False
    else: return True

def inbounds(user_input):
    if user_input > 9 or user_input < 1:
        print("Please enter a number between 1 and 9")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("This position is already taken")
        return True
    else: return False
#to convert number input into coordinates
def position(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row, col)
#to put the number input onto the visible playing board
def put_on_board(coords, board, letter_use):
    row = coords [0]
    col = coords [1]
    board [row] [col] = f"{letter_use}"
#to play with x and o
def current_user(user):
    if user: return "x"
    else: return "o"
#to see if someone won
def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True            
    return False

def check_diag(user, board):
    if board [0] [0] == user and board [1] [1] == user and board [2] [2] == user: return True
    elif board [0] [2] == user and board [1] [1] == user and board [2] [0] == user: return True
    else: return False

def main():
    board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
    ]

    turns = 0
    user = True
    print("1 2 3 \n4 5 6 \n7 8 9")
    while True:
        active_user = current_user(user)
        print_board(board)
        user_input = input("Where do you want to go? (1-9) (q to quit):")
        if quit(user_input) : break
        if not check_input(user_input) :
            print("please try again")
            continue
        user_input = int(user_input) - 1
        coords = position(user_input)
        if istaken(coords, board):
            print ("please try again")
            continue
        put_on_board(coords, board, active_user)
        if iswin(active_user, board):
            print(f"{active_user} Won!")
            print_board(board)
            replay = input("play again?(y/n):")
            if replay == "y":
                board = [
                    ["_", "_", "_"],
                    ["_", "_", "_"],
                    ["_", "_", "_"]
                ]
                turns = 0
                continue
            else: break
            
            

        turns += 1
        if turns == 9:
            print("Its a Draw!")
            print_board(board)
            replay = input('play again?(y/n):')
            if replay == "y":
                board = [
                    ["_", "_", "_"],
                    ["_", "_", "_"],
                    ["_", "_", "_"]
                ]
                turns = 0
                continue
            else: break
        user = not user

main()
