import tkinter as tk

def open_single_player_game():
    import single_player

def open_two_player_game():
    import two_player

root = tk.Tk()
root.title("Tic Tac Toe Main Menu")

single_player_btn = tk.Button(root, text="Single Player", command=open_single_player_game)
single_player_btn.pack()

two_player_btn = tk.Button(root, text="Two Player", command=open_two_player_game)
two_player_btn.pack()

root.mainloop()
