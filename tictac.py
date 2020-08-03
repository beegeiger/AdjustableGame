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
  global official_board
  global A
  global B
  global board_size
  global game_status
  print("Print 1.1")
  start_game()
  print("Print 1.2")
  if B == "X":
    computer_turn()
  while game_status == "Unfinished":
    user_turn()
    st = check_state(official_board)
    if st != "Unfinished":
      game_status = st
      break
    sleep(1)
    computer_turn()
    st = check_state(official_board)
    if st != "Unfinished":
      game_status = st
    sleep(1)
  print("Print 1.3")
  if A == "X" and game_status == "X win" or A == "O" and game_status == "O win":
    print("Congradulations Human, You have bested me!")
  elif game_status == "Tie":
    print("Ahh! I guess we are evenly matched! Next time I will get you!")
  else:
    print("Hahahah human, I have bested you!")
  print("Print 1.4")
  return

def start_game():
  """Function to run game"""
  print("Hi! Welcome to DB Geiger's new ADJUSTABLE tic tac toe game!")
  # input("Press Enter to continue...")
  # Asks the user for the size of the board and sets board_size
  print("Print 2.1")
  q1 = int(input("How many rows would you like on your board? (3-6)"))
  q1options = [3, 4, 5, 6]
  while q1 not in q1options:
    print("That wasn't a valid selection. Choose a number between 3 and 6.")
    q1 = input("How many rows would you like on your board? (3-6)")
  print("Print 2.2")
  global board_size
  board_size = q1
  #With board_size, creates the squares on official_board
  global official_board
  print("Print 2.3")
  for n in range(q1**2):
    official_board.append(n + 1)
  #Asks user if they want to be X or 0 and sets variables A and B
  q2 = input("Would you like to be 'X' or 'O'?")
  q2options = ["X", "x", "O", "o"]
  print("Print 2.4")
  while q2 not in q2options:
    print("That wasn't a valid selection. Choose X or O.")
    q2 = input("Would you like to be 'X' or 'O'?")
  print("Print 2.5")
  global A
  global B
  if q2 in q2options[:2]:
    A = "X"
    B = "O"
  else:
    A = "O"
    B = "X"
  return

def user_turn():
  print("Enter a number 1-9 available on the board.")
  print("Print 3.1")
  global official_board
  global A
  global B
  global board_size
  print_board()
  val = input()
  entry_val = False
  print("Print 3.2")
  while entry_val == False:
      if len(val) > 1 or val.isdigit() == False:
          print("That was not a valid entry. Please enter a number 1-9 available on the board.")
          val = input()
      elif official_board[int(val) - 1] == "X" or official_board[int(val) - 1] == "O":
          print("That square has already been taken. Please enter a number 1-9 STILL OPEN on the board.")
          val = input()
      else:
          entry_val = True
  print("Print 3.3")
  official_board[int(val) - 1] = A
  print("Your Choice: ")
  print_board()
  return

def computer_turn():
  global official_board
  global A
  global B
  global board_size
  print("Print 4.1")
  opts = check_options(official_board)
  print("Print 4.2")
  for y in range(len(official_board)):
    if str(official_board[y]).isalpha():
      opts[y] = -999999999999999999999999999999
  print("Print 4.3")
  highest = max(opts)
  loc = opts.index(highest)
  official_board[loc] = B
  print("Here is my response to your move!")
  print_board()
  return

def print_board():
  """Prints the official board for user"""
  #Loops through and prints rows of the board
  print("Print 5.1")
  global official_board
  print("PRINT_BOARD CALLED")
  for n in range(board_size):
    print(official_board[(n * board_size): ((n * board_size) + board_size)])
  return


def create_options(board):
  """Creates an array of all methods to score"""
  global official_board
  global A
  global B
  global board_size
  global score_options
  print("Print 6.1")
  options = []
  diag1 = []
  diag2 = []
  print("Print 6.2")
  for n in range(board_size):
    column = []
    options.append(board[(n * board_size): ((n * board_size) + board_size)])
    diag1.append(board[n * (board_size + 1)])
    diag2.append(board[(n + 1) * (board_size - 1)])
    for p in range(board_size):
      column.append(board[(p * board_size) + n])
    options.append(column)
  print("Print 6.3")
  options.append(diag1)
  options.append(diag2)
  score_options = options
  print("Print 6.4", options)
  return


def check_state(board):
  print("Print 7.1")
  global score_options
  global board_size
  create_options(board)
  print("Print 7.2")
  for opt in score_options:
    print("Print 7.21", opt)
    if opt.count("X") == board_size:
      print("Print 7.22")
      return "X win"
    elif opt.count("O") == board_size:
      print("Print 7.25")
      return "O win"
  print("Print 7.3")
  if board.count("X") + board.count("O") == (board_size * board_size):
        return "Tie"
  return "Unfinished"

def check_options(board):
  print("Print 8.1")
  global A
  global B
  global board_size
  board_copy = []
  board_copy_copy = []
  chances = []
  print("Print 8.2")
  for n in range(board_size * board_size):
    print("Print 8.3")
    chances.append(0)
  for y in range(board_size):
    print("Print 8.4")
    board_copy = list(board)
    if str(board_copy[y]).isdigit():
      print("Print 8.5")
      board_copy[y] = B
      cur_state = check_state(board_copy)
      multiplier = ((board_size * board_size) - (board_copy.count("X") + board_copy.count("O")))
      if cur_state != "Unfinished":
        print("Print 8.6")
        if cur_state == "X win" or cur_state == "Y win":
          chances[y] += (50 * multiplier)
        elif cur_state == "Tie":
          chances[y] += (multiplier)
      else:
        print("Print 8.7")
        for z in range(board_size):
          board_copy_copy = list(board_copy)
          if str(board_copy_copy[z]).isdigit():
            print("Print 8.8")
            board_copy_copy[z] = A
            cur_stateB = check_state(board_copy_copy)
            multiplier = ((board_size * board_size) - (board_copy_copy.count("X") + board_copy_copy.count("O")))
            print("Print 8.9")
            if cur_stateB != "Unfinished":
              if cur_stateB == "X win" or cur_stateB == "Y win":
                chances[y] -= (50 * multiplier)
              elif cur_stateB == "Tie":
                chances[y] += (multiplier)
            else:
              chances[y] += sum(check_options(board_copy_copy))
  return chances

run_game()