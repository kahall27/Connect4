# This a Connect 4 game that can be played in the terminal on one's computer.
# The rules are:
# There are two players. They take turns.
# The first player drops a coin into a 6x7 board (height X width).
# The next player goes, and so on, until one player has four coins in a row.
# The four coins can be horizontal, vertical, or diagonally.

# Rows defined from top to bottom as seen in the description of the grid below.
# legend = ["A", "B", "C", "D", "E", "F", "G"]
# row1 = ["X", "X", "X", "X", "X", "X", "X"]
# row2 = ["X", "X", "X", "X", "X", "X", "X"]
# row3 = ["X", "X", "X", "X", "X", "X", "X"]
# row4 = ["X", "X", "X", "X", "X", "X", "X"]
# row5 = ["X", "X", "X", "X", "X", "X", "X"]
# row6 = ["X", "X", "X", "X", "X", "X", "X"]

legend = ["A", "B", "C", "D", "E", "F", "G"]

grid = [["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"]]

number_of_spaces = 42

def draw_grid(list_of_rows):
    print(" ".join(legend))
    for row in list_of_rows:
        print(" ".join(row))

def get_column(current_player):
    column_of_choice = input(current_player + ", Which column would you like to place your token in? ")
    while column_of_choice.upper() not in legend:
        print("I'm sorry, that is not a valid column. Please try again.")
        column_of_choice = input(current_player + ", Which column would you like to place your token in? ")

    # prevent placing a token in a full column
    while grid[0][legend.index(column_of_choice.upper())] != "X":
        column_of_choice = input("I'm sorry, that column is full. Please choose a new column: ")
        while column_of_choice.upper() not in legend:
            print("I'm sorry, that is not a valid column. Please try again.")
            column_of_choice = input(current_player + ", Which column would you like to place your token in? ")

    return column_of_choice.upper()


def place_token(player, column_choice):
    # new_grid = grid
    if player == "Player 1":
        token_value = "1"
    else:
        token_value = "2"
    column_index = legend.index(column_choice)
    for i in range(len(grid)):
        if grid[-1 - i][column_index] == "X":
            grid[-1 - i][column_index] = token_value
            return [-1 - i, column_index]


def check_for_winner_row(grid, player, placed_location):
    
    if player == "Player 1":
        token_value = "1"
    else:
        token_value = "2"

    row_placement = placed_location[0]
    column_placement = placed_location[1]
    if column_placement >= 3:
        start = 3
        end = 7
        while end > row_placement:
            if grid[row_placement][start:end].count(token_value) == 4:
                return True
            start -=1
            end -=1 
    else:
        start = 0
        end = 4
        while start <= row_placement:
            if grid[row_placement][start:end].count(token_value) == 4:
                return True
            start +=1
            end +=1 
    return False
            
def check_for_winner_col(grid, player, placed_location):
    
    if player == "Player 1":
        token_value = "1"
    else:
        token_value = "2"

    row_placement = 6 + placed_location[0]
    column_placement = placed_location[1]

    if row_placement > 2:
        return False
    else:
        for i in range(0 + row_placement, 4 + row_placement):
            if grid[i][column_placement] != token_value:
                return False
        return True
        

def check_for_winner_diagonal(grid):
    # Check negative slope diagonally.
    # range(3) because i refers to rows, and after you check 3 rows,
    # you don't need to keep checking since there aren't four more rows.
    # range(4) because after you go through 4 columns, there isn't enough space for four in a row anymore.
    for i in range(3):
        for j in range(4):
            if grid[i][j] == "1" or grid[i][j] == "2":
                if grid[i][j] == grid[i + 1][j + 1] and grid[i][j] == grid[i + 2][j + 2] and grid[i][j] == grid[i + 3][j + 3]:
                    return True

    # Check positive slope diagonally.
    # range(3,6) because i refers to rows, and the top three rows
    # aren't enough to hold an upward sloping line of 4 tokens.
    # range(4) because the last 3 rows once again can't hold a line of 4 tokens.
    for i in range(3, 6):
        for j in range(4):
            if grid[i][j] == "1" or grid[i][j] == "2":
                if grid[i][j] == grid[i - 1][j + 1] and grid[i][j] == grid[i - 2][j + 2] and grid[i][j] == grid[i - 3][j + 3]:
                    return True

    return False

def check_for_winner(grid, player, placed_location):
    row = check_for_winner_row(grid, player, placed_location)
    col = check_for_winner_col(grid, player, placed_location)
    diagonal = check_for_winner_diagonal(grid)
    return row or col or diagonal

def switch_player(player):
    if player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"

def welcome_to_game():
    print("Hello! Welcome to Connect Four! Player 1 goes first!")
    space_bar_pressed = input("Press enter when you are ready to begin!")
    while space_bar_pressed != "":
        space_bar_pressed = input("Press enter when you are ready to begin!")
    return False


# game loop
current_player = "Player 1"
game_over = welcome_to_game()
tokens_placed = 0

while not game_over:

    draw_grid(grid)

    column_choice = get_column(current_player)

    placed_location = place_token(current_player, column_choice)

    game_over = check_for_winner(grid, current_player, placed_location)
    if game_over:
        draw_grid(grid)
        print("Congrats {}! You win!".format(current_player))

    if grid[0].count("X") == 0: 
        draw_grid(grid)
        print("It's a tie! The game board has been filled with no winner!")
        game_over = True

    if game_over:
        print("Would you like to play again?")
        play_again = input("Press Y if yes, or N if no.").upper()
        while play_again != "Y" and play_again != "N":
            play_again = input("Press Y if yes, or N if no.").upper()
        if play_again == "Y":
            grid = [["X", "X", "X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"]]
            current_player = "Player 2"
            game_over = False
        else:
            print("Thanks for playing! Goodbye!")

    new_player = switch_player(current_player)

    current_player = new_player
