# StevenStudy
Steven and Blake's dedicated study repo.

# Best Practices:

"You will learn about four best practices to make sure that your code can serve a dual purpose:"

  - Put most code into a function or class.
  - Use __name__ to control execution of your code.
  - Create a function called main() to contain the code you want to run.
  - Call other functions from main().

We already have it set up this way but I finally just read that [Real Python link](https://realpython.com/python-main-function/) and I get it now. Legit good article 


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