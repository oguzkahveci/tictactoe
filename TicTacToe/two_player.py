import tkinter as tk
from tkinter import messagebox

def new_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    draw_board()

def draw_board():
    for i in range(9):
        row, col = divmod(i, 3)
        board_buttons[i]["text"] = board[i]
        board_buttons[i]["state"] = "normal" if board[i] == " " else "disabled"

def make_move(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        draw_board()
        if game_check(current_player):
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            new_game()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            new_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def game_check(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

root = tk.Tk()
root.title("Tic Tac Toe")
board_buttons = [tk.Button(root, text=" ", font=('normal', 40), width=4, height=2, command=lambda i=i: make_move(i)) for i in range(9)]
for i in range(9):
    row, col = divmod(i, 3)
    board_buttons[i].grid(row=row, column=col)
board = [" " for _ in range(9)]
current_player = "X"

new_game()

root.mainloop()
