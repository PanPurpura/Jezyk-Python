
import tkinter as tk   # Py3
from tkinter import GROOVE, ttk
import random

options = ["Paper", "Rock", "Scissors"]
player_win = 0
computer_win = 0

root = tk.Tk()   
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=2)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.title("Papier-Rock-Scissors")  

root.geometry("{}x{}+{}+{}".format(400, 200, 500, 200))
root.resizable(width=False, height=False)   
root.config(bg = "grey")


screen = tk.Frame(root, bg="grey", borderwidth=3, pady=10)
buttons = tk.Frame(root, bg="grey", borderwidth=3, pady=10)
scores = tk.Frame(root, bg="grey", borderwidth=3, pady=10)

scores.grid(row=0, column=2, columnspan=3)
screen.grid(row=0, column=1, rowspan=2)
buttons.grid(row=2, column=1, rowspan=1)

screen.rowconfigure(0, weight = 1)
screen.rowconfigure(1, weight = 1)

label = tk.Label(screen, text="Player vs Computer", bg="blue", fg="yellow", borderwidth=3, relief="raised", font=("Arial", 20))
label.grid(row = 0, column = 0, pady=(7, 7) ,sticky=tk.N)
label2 = tk.Label(screen, text="Draw", borderwidth=3, relief="raised", bg="blue", fg="yellow", font=("Arial", 12))
label2.grid(row = 1, column = 0, pady=(5, 5), sticky=tk.S)

scores.rowconfigure(0, weight = 1)

label1 = tk.Label(scores, text="Player {} : {} Computer".format(0, 0) ,bg="blue", fg="yellow", borderwidth=3, relief="raised")
label1.grid(row = 1, column = 0)

def paper():
    global computer_win
    global player_win
    player = "Paper"
    idx = random.randint(0, len(options)-1)
    computer = options[idx]
    if computer == "Paper":
        label.config(text = player + " vs " + computer)
        label2.config(text = "Draw")
    elif computer == "Rock":
        player_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Player won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))
    else:
        computer_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Computer won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))

def rock():
    global computer_win
    global player_win
    player = "Rock"
    idx = random.randint(0, len(options)-1)
    computer = options[idx]
    if computer == "Rock":
        label.config(text = player + " vs " + computer)
        label2.config(text = "Draw")
    elif computer == "Scissors":
        player_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Player won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))
    else:
        computer_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Computer won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))

def scissors():
    global computer_win
    global player_win
    player = "Scissors"
    idx = random.randint(0, len(options)-1)
    computer = options[idx]
    if computer == "Scissors":
        label.config(text = player + " vs " + computer)
        label2.config(text = "Draw")
    elif computer == "Paper":
        player_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Player won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))
    else:
        computer_win += 1
        label.config(text = player + " vs " + computer)
        label2.config(text = "Computer won!")
        label1.config(text = "Player {} : {} Computer".format(player_win, computer_win))
        

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)
buttons.columnconfigure(2, weight=1)
buttons.columnconfigure(3, weight=1)

button = tk.Button(buttons,
    text="Paper",
    width=5,
    height=2,
    bg="darkblue",
    fg="yellow",
    borderwidth=3,
    relief="raised",
    command=paper
)
button.grid(row = 0, column = 0, padx=10)
button1 = tk.Button(buttons,
    text="Rock",
    width=5,
    height=2,
    bg="darkblue",
    fg="yellow",
    borderwidth=3,
    relief="raised",
    command=rock
)
button1.grid(row = 0, column = 1, padx=10)
button2 = tk.Button(buttons,
    text="Scissors",
    width=5,
    height=2,
    bg="darkblue",
    borderwidth=3,
    relief="raised",
    fg="yellow",
    command=scissors
)
button2.grid(row = 0, column = 2, padx=10)
button3 = tk.Button(buttons,
    text="Close",
    width=5,
    height=2,
    bg="darkblue",
    fg="yellow",
    borderwidth=3,
    relief="raised",
    command=exit
)
button3.grid(row = 0, column = 3, padx=10)

root.mainloop()   