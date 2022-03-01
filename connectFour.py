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
from typing import Any

legend = ["A", "B", "C", "D", "E", "F", "G"]

grid = [["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"]]


def draw_grid(list_of_rows):
    print(" ".join(legend))
    for row in list_of_rows:
        print(" ".join(row))


def get_column():
    column_of_choice = input("Which column would you like to place your token in? ")
    while column_of_choice.upper() not in legend:
        print("I'm sorry, that is not a valid choice. Please try again.")
        column_of_choice = input("Which column would you like to place your token in? ")
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
            break


def check_for_winner():
    # Check horizontally
    for row in grid:
        if row.count("1") >= 4 or row.count("2") >= 4:
            return True

    # Check vertically
    vertical_values = [[] for i in range(7)]
    for row in grid:
        for i in range(len(row)):
            vertical_values[i].append(row[i])

    for column in vertical_values:
        if column.count("1") >= 4 or column.count("2") >= 4:
            return True

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

while not game_over:

    draw_grid(grid)

    column_choice = get_column()

    place_token(current_player, column_choice)

    game_over = check_for_winner()

    if game_over:
        draw_grid(grid)
        print("Congrats {}! You win!".format(current_player))
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
            draw_grid(grid)
            current_player = "Player 2"
            game_over = False
        else:
            print("Thanks for playing! Goodbye!")

    new_player = switch_player(current_player)

    current_player = new_player
