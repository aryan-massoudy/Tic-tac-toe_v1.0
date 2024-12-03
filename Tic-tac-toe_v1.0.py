import os
import random

# Function to display the game board
def display_board(board):
    """
    Clears the screen and prints the current state of the game board.
    Board positions are arranged as:
      7 | 8 | 9
     ---|---|---
      4 | 5 | 6
     ---|---|---
      1 | 2 | 3
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |')

# Function to take player input and assign markers
def player_input():
    """
    Asks Player 1 to choose 'X' or 'O'. Automatically assigns the other marker to Player 2.
    Returns a tuple (player1_marker, player2_marker).
    """
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Do you want to be 'X' or 'O'? ").upper()
    return ('X', 'O') if marker == 'X' else ('O', 'X')

# Function to place a marker on the board
def place_marker(board, marker, position):
    """
    Updates the game board at the specified position with the player's marker.
    """
    board[position] = marker

# Function to check if a player has won
def win_check(board, mark):
    """
    Checks if the given marker has any of the winning combinations.
    Returns True if there's a win, otherwise False.
    """
    return ((board[7] == board[8] == board[9] == mark) or  # Top row
            (board[4] == board[5] == board[6] == mark) or  # Middle row
            (board[1] == board[2] == board[3] == mark) or  # Bottom row
            (board[7] == board[4] == board[1] == mark) or  # Left column
            (board[8] == board[5] == board[2] == mark) or  # Middle column
            (board[9] == board[6] == board[3] == mark) or  # Right column
            (board[7] == board[5] == board[3] == mark) or  # Diagonal top-left to bottom-right
            (board[9] == board[5] == board[1] == mark))    # Diagonal top-right to bottom-left

# Function to randomly decide which player goes first
def choose_first():
    """
    Randomly selects which player goes first.
    Returns 'Player 1' or 'Player 2'.
    """
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

# Function to check if a specific board position is available
def space_check(board, position):
    """
    Checks if a specific position on the board is free.
    Returns True if the position is available, otherwise False.
    """
    return board[position] == ' '

# Function to check if the board is completely filled
def full_board_check(board):
    """
    Checks if the board is full.
    Returns True if all positions are filled, otherwise False.
    """
    return not any(space_check(board, i) for i in range(1, 10))

# Function to get a valid position input from the player
def player_choice(board):
    """
    Asks the player to select a position on the board (1-9).
    Ensures the input is valid and the position is free.
    Returns the chosen position.
    """
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose your next position (1-9): "))
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    return position

# Function to ask if players want to replay the game
def replay():
    """
    Asks players if they want to play again.
    Returns True if the input starts with 'y', otherwise False.
    """
    return input("Do you want to play again? Enter Yes or No: ").strip().lower().startswith('y')

# Main game logic
print("Welcome to Tic Tac Toe!")

while True:
    # Initialize the game board
    theBoard = [' '] * 10  # Index 0 is ignored for simplicity
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first.")

    # Check if players are ready to start
    game_on = input("Are you ready to play? Enter Yes or No: ").strip().lower().startswith('y')

    while game_on:
        # Handle Player 1's turn
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! Player 1 has won the game!")
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print("The game is a draw!")
                break
            else:
                turn = 'Player 2'

        # Handle Player 2's turn
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 has won the game!")
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print("The game is a draw!")
                break
            else:
                turn = 'Player 1'

    if not replay():
        print("Thanks for playing Tic Tac Toe! Goodbye!")
        break
