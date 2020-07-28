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
  q1 = input("How many rows would you like on your board? (3-6)")
  q1options = [3, 4, 5, 6]
  while q1 not in q1options:
    print("That wasn't a valid selection. Choose a number between 3 and 6.")
    q1 = input("How many rows would you like on your board? (3-6)")
  board_size = q1
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