def initalize():
    global break_val
    break_val = False

def print_reference_board():  
    global reference_board  
    reference_board = [[],
                   ['A1', ' │ ', 'B1', ' │ ', 'C1'],
                   ['A2', ' │ ', 'B2', ' │ ', 'C2'],
                   ['A3', ' │ ', 'B3', ' │ ', 'C3'],
                   []]
    print_board(board= reference_board, num_dash= 17, row_index= 0)

def create_playing_board():
    global playing_board
    playing_board = [[' ', ' │ ', ' ', ' │ ', ' '],
                   [' ', ' │ ', ' ', ' │ ', ' '],
                   [' ', ' │ ', ' ', ' │ ', ' ']]

def print_board(board, num_dash, row_index):
    row_index = row_index
    for rows in board:
        for squares in rows:
            print(squares, end = " ")
        print()
        if row_index > 0 and row_index < 3:
            print('─'* num_dash)
        row_index += 1

def categorize_selection():
    global index_col, index_row
    if selection[0] == "A":
        index_col = 0
    elif selection[0] == "B":
        index_col = 2
    else:
        index_col = 4
    if selection[1] == "1":
        index_row = 0
    elif selection[1] == "2":
        index_row = 1
    else:
        index_row = 2

def check_board(player_1, player_2):
    global break_val
    row1 = [playing_board[0][0], playing_board[0][2], playing_board[0][4]]
    row2 = [playing_board[1][0], playing_board[1][2], playing_board[1][4]]
    row3 = [playing_board[2][0], playing_board[2][2], playing_board[2][4]]
    col1 = [playing_board[0][0], playing_board[1][0], playing_board[2][0]]
    col2 = [playing_board[0][2], playing_board[1][2], playing_board[2][2]]
    col3 = [playing_board[0][4], playing_board[1][4], playing_board[2][4]]
    diag1 = [playing_board[0][0], playing_board[1][2], playing_board[2][4]]
    diag2 = [playing_board[0][4], playing_board[1][2], playing_board[2][0]]
    for elem in [row1, row2, row3, col1, col2, col3, diag1, diag2]:
        if all(indiv_elems == "X" for indiv_elems in elem):
            print_board(board= playing_board, num_dash= 13, row_index= 1)
            print(f"\nCongratulations, {player_1}! We knew you would destroy {player_2}.")
            break_val = True
            break
        elif all(indiv_elems == "O" for indiv_elems in elem):
            print_board(board= playing_board, num_dash= 13, row_index= 1)
            print(f"\nCongratulations, {player_2}! You cruised to victory.")
            break_val = True
            break

def play_game():
    global selection, playing_board
    initalize()
    player_1 = input("Player 1 name: ")
    print(f"Welcome to the game, {player_1}! You will be playing as 'X'\n")
    player_2 = input("Player 2 name: ")
    print(f"Thanks for playing, {player_1}! You are O's\n")
    game_num = 0
    allowable_selections = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    create_playing_board()
    while game_num < 9 and break_val == False:
        print_reference_board()
        print_board(board= playing_board, num_dash= 13, row_index= 1)
        if game_num % 2 == 0:
            selection = input(f"\n{player_1}, please select a square: ")
        else:
            selection = input(f"\n{player_2}, please select a square: ")
        while selection not in allowable_selections:
            print_reference_board()
            selection = input("\nPlease enter a valid position: ")
        categorize_selection()
        if game_num % 2 == 0:
            playing_board[index_row][index_col] = "X"
        else:
            playing_board[index_row][index_col] = "O"
        allowable_selections.remove(selection)
        check_board(player_1, player_2)
        game_num += 1
    if break_val == False:
        print("Dang, the cat got the game!")
    
def new_game():
    play_again = "y"
    while play_again == "y":
        play_game()
        play_again = input("New game? y/n ")

new_game()
