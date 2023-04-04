def main():
    firstIntro()
    playGame()

def firstIntro():
    print('Well hello mother fucka, press "I" to see instructions')
    print("Otherwise, press any other key to play Tic Tac Toe.")
    userInput = input()
    if userInput.upper() == "I":
        instructions()
    # TODO Add message saying continuing to game 


# A Dictionary used to store values to represent the game board
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

# This function prints the game board in a presentable way
def printBoard(locations):
    print(locations['7'] + '|' + locations['8'] + '|' + locations['9'])
    print('-+-+-')
    print(locations['4'] + '|' + locations['5'] + '|' + locations['6'])
    print('-+-+-')
    print(locations['1'] + '|' + locations['2'] + '|' + locations['3'])

# TODO Ask User if they want to see this
# TODO Flesh out instrcutions
def instructions():
    print("These are the board spaces:")
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')
    print(" ")


    
# Handles the player turn and functionality of the game
# TODO seperate player handling from game handling
# TODO Let player enter "I" during player choice to call instructions
def playGame():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        position = input()
        theBoard[position] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    


# TODO
# who wins code
# add turn counter, "if turn is >= 5, then run check function"
# exception handling (numbers only, 1-9)
# make game object oriented



if __name__ == "__main__":
    main()
