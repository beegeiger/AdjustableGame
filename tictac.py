#Fully Adjustable Tic Tac Toe Game
from time import sleep

official_board = []
board_copy = []
game_status = "Unfinished"
A = ""
B = ""
board_size = 0
score_options = []

def run_game():
  start_game()
  if B == "X":
    computer_turn()
  while game_status == "Unfinished":
    print("JUST BEFORE USER TURN", offical_board, game_status)
        user_turn()
        st = check_state(offical_board)
        if st != "Unfinished":
            game_status = st
            break
        sleep(1)
        print("JUST BEFORE COMPUTER TURN", offical_board, game_status)
        computer_turn()
        st = check_state(offical_board)
        if st != "Unfinished":
            game_status = st
        sleep(1)
  return

def start_game():
  """Function to run game"""
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
  q2options = ["X", "x", "O", "o"]
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

def user_turn():
  print("Enter a number 1-9 available on the board.")
  print_board()
  val = input()
  entry_val = False
  while entry_val == False:
      if len(val) > 1 or val.isdigit() == False:
          print("That was not a valid entry. Please enter a number 1-9 available on the board.")
          val = input()
      elif offical_board[int(val) - 1] == "X" or offical_board[int(val) - 1] == "O":
          print("That square has already been taken. Please enter a number 1-9 STILL OPEN on the board.")
          val = input()
      else:
          entry_val = True
  offical_board[int(val) - 1] = A
  print("Your Choice: ")
  print_board()
  return

def computer_turn():
  opts = check_options(offical_board)
  for y in range(board_size * board_size):
    if str(offical_board[y]).isalpha():
      opts[y] = -999999999999999999999999999999
  highest = max(opts)
  loc = opts.index(highest)
  offical_board[loc] = B
  print("Here is my response to your move!")
  print_board()
  return

def print_board():
  """Prints the official board for user"""
  #Loops through and prints rows of the board
  for n in range(board_size):
    print(official_board[(n * board_size): ((n * board_size) + board_size)])
  return


def create_options(board):
  """Creates an array of all methods to score"""
  options = []
  diag1 = []
  diag2 = []
  for n in range(board_size):
    column = []
    options.append(board[(n * board_size): ((n * board_size) + board_size)])
    diag1.append(board[n * (board_size + 1)])
    diag2.append(board[n * (board_size - 1)])
    for p in range(board_size):
      column.append(board[(p * board_size) + n])
    options.append(column)
  options.append(diag1)
  options.append(diag2)
  score_options = options
  return

def check_state(board):
  if score_options == []:
    create_options(board)
  for opt in score_options:
    if opt.count("X") == board_size:
      return "X win"
    elif opt.count("O") == board_size:
      return "O win"
  if board.count("X") + board.count("O") == (board_size * board_size):
        return "Tie"
  return "Unfinished"

def check_options(board):
  board_copy = []
  board_copy_copy = []
  chances = []
  for n in range(board_size):
    chances.append(0)
  for y in range(board_size):
    board_copy = list(board)
    if str(board_copy[y]).isdigit():
      board_copy[y] = B
      cur_state = check_state(board_copy)
      multiplier = ((board_size * board_size) - (board_copy.count("X") + board_copy.count("O")))
      if cur_state != "Unfinished":
        if cur_state == "X win" or cur_state == "Y win":
          chances[y] += (50 * multiplier)
        else cur_state == "Tie":
          chances[y] += (multiplier)
      else:
        for z in range(board_size):
          board_copy_copy = list(board_copy)
          if str(board_copy_copy[z]).isdigit():
            board_copy_copy[z] = A
            cur_stateB = check_state(board_copy_copy)
            multiplier = ((board_size * board_size) - (board_copy_copy.count("X") + board_copy_copy.count("O")))
            if cur_stateB != "Unfinished":
              if cur_stateB == "X win" or cur_stateB == "Y win":
                chances[y] -= (50 * multiplier)
              else cur_stateB == "Tie":
                chances[y] += (multiplier)
            else:
              chances[y] += sum(check_options(board_copy_copy)
  return chances