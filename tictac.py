#Fully Adjustable Tic Tac Toe Game
from time import sleep

official_board = []
board_copy = []
game_status = "Unfinished"
A = ""
B = ""
board_size = 0

def start_game():
  #Function to run game
  print("Hi! Welcome to DB Geiger's new ADJUSTABLE tic tac toe game!")
  input("Press Enter to continue...")
  # Asks the user for the size of the board and sets board_size
  q1 = input("How many rows would you like on your board? (3-6)")
  q1options = [3, 4, 5, 6]
  while q1 not in q1options:
    print("That wasn't a valid selection. Choose a number between 3 and 6.")
    q1 = input("How many rows would you like on your board? (3-6)")
  board_size = q1
  #With board_size, creates the squares on official_board
  for n in range(q1**2):
    official_board.append(n + 1)
  #Asks user if they want to be X or 0 and sets variables A and B
  q2 = input("Would you like to be 'X' or 'O'?")
  q2options = ["X", "x", "O", "x"]
  while q2 not in q2options:
    print("That wasn't a valid selection. Choose X or O.")
    q2 = input("Would you like to be 'X' or 'O'?")
  if q2 in q2options[:2]:
    A = "X"
    B = "O"
  else:
    A = "O"
    B = "X"
  return

def print_board():
  #Prints the official board for user
  for n in range(board_size):
    print(official_board[(n * board_size): ((n * board_size) + board_size)])
  return