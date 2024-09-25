import tkinter as tk
from tkinter import messagebox

# Tic Tac Toe game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Game")

        # Initialize variables
        self.board = [""] * 9  # 3x3 board as a list
        self.current_player = "X"
        self.buttons = []

        # Colors for X and O
        self.x_color = "#ff6347"  # Tomato red for X
        self.o_color = "#4682b4"  # Steel blue for O
        self.winner_line_color = "#32cd32"  # Lime green for winner line

        # Create a canvas for drawing the winner line
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Create the reset button
        reset_button = tk.Button(self.root, text="Restart Game", command=self.reset_game, font=("Arial", 14))
        reset_button.pack(pady=20)

        # Create the Tic Tac Toe grid
        self.create_grid()

    # Create the grid of buttons for the game
    def create_grid(self):
        # Clear previous buttons (if resetting)
        self.buttons = []

        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 40, "bold"), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.place(x=(i % 3) * 130 + 40, y=(i // 3) * 130 + 40, width=120, height=120)
            self.buttons.append(button)

    # Handle button click
    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            # Set the player's move on the board
            self.board[index] = self.current_player
            color = self.x_color if self.current_player == "X" else self.o_color
            self.buttons[index].config(text=self.current_player, fg=color)

            # Check for a win or a draw after the move
            if self.check_winner():
                self.draw_winner_line()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"

    # Disable buttons after the game is over
    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    # Check for a winner
    def check_winner(self):
        # Winning combinations in a 3x3 Tic Tac Toe grid
        self.winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                     (0, 4, 8), (2, 4, 6)]  # Diagonals

        for combo in self.winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                self.winning_combo = combo
                return True
        return False

    # Draw the winning line for the winning combination
    def draw_winner_line(self):
        # Coordinates of the center of each button
        coords = {
            0: (100, 100), 1: (230, 100), 2: (360, 100),
            3: (100, 230), 4: (230, 230), 5: (360, 230),
            6: (100, 360), 7: (230, 360), 8: (360, 360),
        }

        start = coords[self.winning_combo[0]]
        end = coords[self.winning_combo[2]]

        # Draw the winner line on top of the buttons
        self.canvas.create_line(start[0], start[1], end[0], end[1], fill=self.winner_line_color, width=10)

    # Reset the game for a new round
    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.canvas.delete("all")  # Clear any lines drawn
        self.create_grid()

# Main function to start the game
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Adjust the window size
    game = TicTacToe(root)
    root.mainloop()
