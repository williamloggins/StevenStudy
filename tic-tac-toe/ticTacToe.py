def main():
    first_intro()
    game_flow()

def first_intro():
    print('Well hello, press "I" to see instructions')
    print("Otherwise, press any other key to play Tic Tac Toe.")
    userInput = input()
    if userInput.upper() == "I":
        instructions()
    # TODO Add message saying continuing to game 

# A Dictionary used to store values to represent the game board
game_board = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}

def instructions():
    print("These are the board spaces:")
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')
    print(" ")

def playGame():
    turn = 'X'
    for i in range(9):
        print_board(game_board)
        print('Turn for ' + turn + '. Move on which space?')
        position = input()
        game_board[position] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def game_flow():
#TODO this should handle player input
    turn = 'X'
    for i in range(9):
        print_board(game_board, turn)
        position = player_position()
        board_update(position, turn)
        turn = player_turn(turn)

# This function prints the game board in a presentable way
def print_board(locations, turn):
    print(locations['7'] + '|' + locations['8'] + '|' + locations['9'])
    print('-+-+-')
    print(locations['4'] + '|' + locations['5'] + '|' + locations['6'])
    print('-+-+-')
    print(locations['1'] + '|' + locations['2'] + '|' + locations['3'])
    print('Turn for ' + turn + '. Move on which space?')

def player_position():
#TODO add validations here
    position = input()
    return position

def board_update(position, turn):
#TODO this should handle updating the board
    game_board[position] = turn

def player_turn(turn):
#TODO add validations here
    return "X" if player_turn == "O" else "O"

def check_winner():
    pass

if __name__ == "__main__":
    main()

# TODO
# who wins code
# add turn counter, "if turn is >= 5, then run check function"
# exception handling (numbers only, 1-9)
# make game object oriented
# make it to where user can type I anytime
# while there is no winner, keep going
# Handles the player turn and functionality of the game
# TODO seperate player handling from game handling
# TODO Player turn 
# TODO game handling function
# TODO check winner function
# TODO handle winner function
# TODO Let player enter "I" during player choice to call instructions

