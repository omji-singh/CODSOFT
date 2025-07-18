import tkinter as tk
from tkinter import ttk, messagebox
import random

class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.resizable(False, False)
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        self.build_ui()

    def build_ui(self):
        frm = ttk.Frame(self, padding=10)
        frm.grid()

        ttk.Label(frm, text="Choose your move:").grid(row=0, column=0, columnspan=3, pady=5)

        ttk.Button(frm, text="Rock", command=lambda: self.play("Rock")).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frm, text="Paper", command=lambda: self.play("Paper")).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(frm, text="Scissors", command=lambda: self.play("Scissors")).grid(row=1, column=2, padx=5, pady=5)

        self.label_user = ttk.Label(frm, text="Your choice: -")
        self.label_user.grid(row=2, column=0, columnspan=3, pady=5)

        self.label_computer = ttk.Label(frm, text="Computer choice: -")
        self.label_computer.grid(row=3, column=0, columnspan=3, pady=5)

        self.label_result = ttk.Label(frm, text="Result: -", font=("Arial", 12, "bold"))
        self.label_result.grid(row=4, column=0, columnspan=3, pady=10)

        self.label_score = ttk.Label(frm, text="Your score: 0    Computer score: 0")
        self.label_score.grid(row=5, column=0, columnspan=3, pady=5)

        ttk.Button(frm, text="Play Again", command=self.reset_round).grid(row=6, column=0, columnspan=3, pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        self.label_user.config(text=f"Your choice: {user_choice}")
        self.label_computer.config(text=f"Computer choice: {computer_choice}")

        result = self.determine_winner(user_choice, computer_choice)

        if result == "win":
            self.user_score += 1
            result_text = "You win!"
        elif result == "lose":
            self.computer_score += 1
            result_text = "You lost!"
        else:
            result_text = "It's a tie!"

        self.label_result.config(text=f"Result: {result_text}")
        self.label_score.config(
            text=f"Your score: {self.user_score}    Computer score: {self.computer_score}"
        )

    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
        ):
            return "win"
        else:
            return "lose"

    def reset_round(self):
        self.label_user.config(text="Your choice: -")
        self.label_computer.config(text="Computer choice: -")
        self.label_result.config(text="Result: -")

if __name__ == "__main__":
    RPSApp().mainloop()
