print("""
Welcome to the battleship Game!
You as the user can play this game against the computer,
which determines the location of one ship randomly.
You have FOUR turns. Enjoy The Game (Hopefully)! 
""")
from time import sleep
sleep(5)
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

#print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
def battleship():
  """
  This function is defined as the battleship game that we all know and love.
  The ocean is a 5 x 5 grid. The user has 4 turns. Enjoy( hopefully)!
  """
  turn = 0
  sleep(2)
  for i in range(4):
    turn = i 
    guess_row = \
    int(input("Guess Row (Type an integer between 0 to 4 and press enter/return): "))
    guess_col = \
    int(input("Guess Col (Type an integer between 0 to 4 and press enter/return): "))
    if guess_row == ship_row \
    and guess_col == ship_col:
      print("Congratulations! You sunk my battleship!")
      board[ship_row][ship_col] = "S"
      print("The ship's location Row X Column is:(%d,%d)"%(ship_row + 1,ship_col + 1))
      print_board(board)
      print("Turn", turn + 1)
      break
    else:
      if (guess_row < 0 or guess_row > 4)\
      or (guess_col < 0 or guess_col > 4):
        print\
        ("Oops, That's Not Even in the Ocean!")
        sleep(2)
        print("Turn", turn + 1)
        if turn == 3:
          print("Game Over")
          board[ship_row][ship_col] = "S"
          print("The ship's location Row X Column is:(%d,%d)"%(ship_row + 1,ship_col + 1))
          print_board(board)   
      elif (board[guess_row][guess_col] \
         == "X"):
        board[guess_row][guess_col] = "X"
        print_board(board)
        print\
        ("You guessed that one already.")
        print("Turn", turn + 1)
        if turn == 3:
          print("Game Over")
          board[ship_row][ship_col] = "S"
          print("The ship's location Row X Column is:(%d,%d)"%(ship_row + 1,ship_col + 1))
          print_board(board)
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        print("Turn", turn + 1)
        if turn == 3:
          print("Game Over")
          board[ship_row][ship_col] = "S"
          print("The ship's location Row X Column is:(%d,%d)"%(ship_row + 1,ship_col + 1))
          print_board(board)
battleship()
