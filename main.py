gameboard = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
num_selection = [1,2,3,4,5,6,7,8,9]
rows = 3
cols = 3
game_start = True
counter = 0

print("""
 ______  ____   __      ______   ____    __      ______   ___     ___ 
|      ||    | /  ]    |      | /    |  /  ]    |      | /   \   /  _]
|      | |  | /  /     |      ||  o  | /  /     |      ||     | /  [_ 
|_|  |_| |  |/  /      |_|  |_||     |/  /      |_|  |_||  O  ||    _]
  |  |   |  /   \_       |  |  |  _  /   \_       |  |  |     ||   [_ 
  |  |   |  \     |      |  |  |  |  \     |      |  |  |     ||     |
  |__|  |____\____|      |__|  |__|__|\____|      |__|   \___/ |_____|
                                                                      """)

def game_board():
    for x in range(rows):
        print("\n-------------")
        #prevents the partitions to print to a new line
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" |")
    print("\n-------------")

def place_x_o(num, shape):
    num -= 1
    if num == 0:
        gameboard[0][0] = shape
    elif num == 1:
        gameboard[0][1] = shape
    elif num == 2:
        gameboard[0][2] = shape
    elif num == 3:
        gameboard[1][0] = shape
    elif num == 4:
        gameboard[1][1] = shape
    elif num == 5:
        gameboard[1][2] = shape
    elif num == 6:
        gameboard[2][0] = shape
    elif num == 7:
        gameboard[2][1] = shape
    elif num == 8:
        gameboard[2][2] = shape

def check_input(cell, shape):
    if cell in num_selection:
        place_x_o(cell, shape)
        num_selection.remove(cell)
    else:
        print("Invalid input. Please only enter a number within the range")

def check_winner(gameboard):
    # row1
    if gameboard[0][0] == 'X' and gameboard[0][1] == 'X' and gameboard[0][2] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][0] == 'O' and gameboard[0][1] == 'O' and gameboard[0][2] == 'O':
        print("Player 2 wins.")
        return True
    # row2
    elif gameboard[1][0] == 'X' and gameboard[1][1] == 'X' and gameboard[1][2] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[1][0] == 'O' and gameboard[1][1] == 'O' and gameboard[1][2] == 'O':
        print("Player 2 wins.")
        return True
    # row3
    elif gameboard[2][0] == 'X' and gameboard[2][1] == 'X' and gameboard[2][2] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[2][0] == 'O' and gameboard[2][1] == 'O' and gameboard[2][2] == 'O':
        print("Player 2 wins.")
        return True
    # col1
    elif gameboard[0][0] == 'X' and gameboard[1][0] == 'X' and gameboard[2][0] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][0] == 'O' and gameboard[1][0] == 'O' and gameboard[2][0] == 'O':
        print("Player 2 wins.")
        return True
    # col2
    elif gameboard[0][0] == 'X' and gameboard[1][1] == 'X' and gameboard[2][1] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][0] == 'O' and gameboard[1][1] == 'O' and gameboard[2][1] == 'O':
        print("Player 2 wins.")
        return True
    # col3
    elif gameboard[0][2] == 'X' and gameboard[1][2] == 'X' and gameboard[2][2] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][2] == 'O' and gameboard[1][2] == 'O' and gameboard[2][2] == 'O':
        print("Player 2 wins.")
        return True
    # diag1
    elif gameboard[0][0] == 'X' and gameboard[1][1] == 'X' and gameboard[2][2] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][1] == 'O' and gameboard[1][1] == 'O' and gameboard[2][2] == 'O':
        print("Player 2 wins.")
        return True
    # diag2
    elif gameboard[0][2] == 'X' and gameboard[1][1] == 'X' and gameboard[2][0] == 'X':
        print("Player 1 wins.")
        return True
    elif gameboard[0][2] == 'O' and gameboard[1][1] == 'O' and gameboard[2][0] == 'O':
        print("Player 2 wins.")
        return True


while game_start:
    # Player 1 turn
    if counter % 2 == 0:
        game_board()
        cell = int(input(f"Player 1 is X. Choose a number between 1-9: "))
        check_input(cell,'X')
        counter += 1
        game_over = check_winner(gameboard)
        if game_over:
            break
    #Player 2 turn
    else:
        game_board()
        cell = int(input(f"Player 2 is O. Choose a number between 1-9: "))
        check_input(cell,'O')
        counter += 1
        game_over = check_winner(gameboard)
        if game_over:
            break

game_board()
""" This will serve as a reference for the players
----------
| 1| 2| 3|
----------
| 4| 5| 6|
----------
| 7| 8| 9|
----------"""