import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {player_choice}\nComputer: {computer_choice}\n\n{result}"
    )

    score_label.config(
        text=f"Player: {player_score}    Computer: {computer_score}"
    )

def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    result_label.config(text="Choose Rock, Paper, or Scissors!")
    score_label.config(text="Player: 0    Computer: 0")



root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")
root.configure(bg="#2c3e50")


title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="#2c3e50",
    fg="white"
)
title.pack(pady=15)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors!",
    font=("Arial", 14),
    bg="#2c3e50",
    fg="white"
)
result_label.pack(pady=20)


button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack()

rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)


score_label = tk.Label(
    root,
    text="Player: 0    Computer: 0",
    font=("Arial", 14, "bold"),
    bg="#2c3e50",
    fg="yellow"
)
score_label.pack(pady=25)

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    width=15,
    command=reset
)
reset_btn.pack(pady=10)

root.mainloop()