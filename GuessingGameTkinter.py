import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    global Guess, Chance
    Guess = random.randint(1, 100)
    Chance = 0
    result_label.config(text="")
    input_entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    guess_input.set("")


def check_guess():
    global Chance
    Guessed = int(guess_input.get())
    Chance += 1
    remaining_chances = 5 - Chance

    if Guessed == Guess:
        result_label.config(text="You guessed it right!", bg="white")
        messagebox.showinfo("Result", "Congratulations, You Won!")
    elif Guessed > Guess:
        result_label.config(text="You guessed it High, Chances left : {}".format(remaining_chances), bg="white")
    else:
        result_label.config(text="You guessed it Low, Chances left : {}".format(remaining_chances), bg="white")

    if Chance == 5 and Guessed != Guess:
        input_entry.config(state=tk.DISABLED)
        guess_button.config(state=tk.DISABLED)
        messagebox.showinfo("Result", "You are out of chances.\nThe number was " + str(Guess))

def restart_game():
    play_game()
    guess_input.set("")

root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x300")
root.config(bg="white")

Guess = 0
Chance = 0

title_label = tk.Label(root, text="Welcome to Guessing Game", font=("Times New Roman", 20, "bold"), bg="white")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="You have 5 chances to guess.\nIf you guess it right, you win.\nIf you guess it wrong, you lose.", font=("Times New Roman", 16), bg="white")
instruction_label.pack(pady=10)

play_button = tk.Button(root, text="Start Game", command=play_game, bg="white")
play_button.pack()

guess_input = tk.StringVar()
input_entry = tk.Entry(root, textvariable=guess_input, state=tk.DISABLED, bg="white")
input_entry.pack()

guess_button = tk.Button(root, text="Check Guess", command=check_guess, state=tk.DISABLED, bg="white")
guess_button.pack()

result_label = tk.Label(root, text="", font=("Times New Roman", 16))
result_label.pack(pady=10)

root.mainloop()