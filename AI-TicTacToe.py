import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, 'X'):
        return -1  # X wins
    elif check_winner(board, 'O'):
        return 1   # O wins
    elif is_board_full(board):
        return 0   # It's a draw
    else:
        return None  # Game is still ongoing

# Minimax function
def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo the move
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo the move
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the computer (O)
def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to handle button clicks
def on_button_click(row, col):
    global board, player_turn

    if board[row][col] == ' ' and player_turn:
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        player_turn = False

        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            computer_move = find_best_move(board)
            board[computer_move[0]][computer_move[1]] = 'O'
            buttons[computer_move[0]][computer_move[1]].config(text='O', state=tk.DISABLED)
            player_turn = True

            if check_winner(board, 'O'):
                messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
                reset_board()
            elif is_board_full(board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                reset_board()

# Function to reset the board
def reset_board():
    global board, player_turn
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)

# Create the main Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the board and player turn
board = [[' ' for _ in range(3)] for _ in range(3)]
player_turn = True

# Create buttons for each cell in the grid
buttons = [[tk.Button(root, text='', font=('Helvetica', 24), width=3, height=1,
                      command=lambda r=i, c=j: on_button_click(r, c))
            for j in range(3)] for i in range(3)]

# Place the buttons on the grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Create a reset button
reset_button = tk.Button(root, text='Reset', command=reset_board)
reset_button.grid(row=3, column=1)

# Run the Tkinter main loop
root.mainloop()
