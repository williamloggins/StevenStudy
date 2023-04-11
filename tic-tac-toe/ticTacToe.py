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

def game_flow():
    turn = 'X'
    for i in range(9):
        print_board(game_board, turn)
        position = player_position()
        board_update(position, turn)
        turn = player_turn(turn)


def print_board(locations, turn):
    """
    This function prints the game board in a presentable way
    
    :param int locations:
    :param str turn:
    :rtype None
    """
    print(locations['7'] + '|' + locations['8'] + '|' + locations['9'])
    print('-+-+-')
    print(locations['4'] + '|' + locations['5'] + '|' + locations['6'])
    print('-+-+-')
    print(locations['1'] + '|' + locations['2'] + '|' + locations['3'])
    print('Turn for ' + turn + '. Move on which space?')

def player_position():
# check it input is either "i" or numbers 1-9. if so, proceed. if not, send back for error message
    position = input()
    return position

def board_update(position, turn):
# check if board position is empty. if empty, proceed. if not, send back to game loop and provide error message regarding invalid spot
    game_board[position] = turn

def player_turn(turn):
    return "X" if turn == "O" else "O"

def check_winner():
    pass

if __name__ == "__main__":
    main()