import tkinter as tk
from tkinter import messagebox

def new_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    draw_board()
    if current_player == "O":
        computer_move()

def draw_board():
    for i in range(9):
        row, col = divmod(i, 3)
        board_btn[i]["text"] = board[i]
        board_btn[i]["state"] = "normal" if board[i] == " " else "disabled"

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
            if current_player == "O":
                computer_move()

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

def computer_move():
    index = best_move()
    make_move(index)

def best_move():
    best_score = -float('inf')
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alpha_beta_minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def alpha_beta_minimax(board, depth, is_max, alpha, beta):
    result = game_result(board)
    if result != "ongoing":
        return score_result(result)

    if is_max:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alpha_beta_minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alpha_beta_minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def game_result(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    if " " not in board:
        return "draw"
    return "ongoing"

def score_result(result):
    if result == "O":
        return 1
    elif result == "X":
        return -1
    else:
        return 0

root = tk.Tk()
root.title("Tic Tac Toe")
board_btn = [tk.Button(root, text=" ", font=('normal', 40), width=4, height=2, command=lambda i=i: make_move(i)) for i in range(9)]
for i in range(9):
    row, col = divmod(i, 3)
    board_btn[i].grid(row=row, column=col)
board = [" " for _ in range(9)]
current_player = "X"

new_game()

root.mainloop()
