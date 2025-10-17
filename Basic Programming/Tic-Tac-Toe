
# --- 1. The Game Board ---
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# --- 2. Function to Display the Board ---
def display_board(board):
  print("\n")
  for i, row in enumerate(board):
    print(" | ".join(row))
    if i < 2:
      print("---------")

# --- 3. Function to Handle a Player's Turn ---
def handle_turn(player):
  """Gets player input, validates it, and updates the board."""
  print(f"\nPlayer {player}'s turn.")
  
  while True:
    try:
      row = int(input("Enter row (1-3): ")) - 1
      col = int(input("Enter column (1-3): ")) - 1

      if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
        board[row][col] = player
        break
      else:
        print("That spot is invalid or already taken. Try again.")
    except ValueError:
      print("Please enter a number (1, 2, or 3).")

# --- 4. NEW: Function to Check for a Winner ---
def check_winner(board):
  """Checks for a win condition (rows, columns, diagonals)."""
  # Check rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return row[0]
  # Check columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
      return board[0][col]
  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
    return board[0][2]
  return None

# --- 5. NEW: Function to Check for a Tie ---
def check_tie(board):
  """Checks if the board is full."""
  for row in board:
    for cell in row:
      if cell == ' ':
        return False # If any cell is empty, it's not a tie
  return True

# --- 6. The Main Game Loop Function ---
def play_game():
  """Runs the main game loop."""
  current_player = 'X'
  print("Welcome to Tic-Tac-Toe!")

  while True:
    display_board(board)
    handle_turn(current_player)
    
    winner = check_winner(board)
    if winner:
      display_board(board)
      print(f"\nCongratulations! Player {winner} wins!")
      break

    if check_tie(board):
      display_board(board)
      print("\nIt's a tie!")
      break
      
    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'

# --- Start the Game ---
play_game()
