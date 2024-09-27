Project Overview:
This project is a simple implementation of the classic Tic-Tac-Toe game using Python and the Tkinter library. The game allows two players, X and O, to play against each other on a 3x3 grid.

Game Features:
-A 3x3 grid for playing the game
-Two players, X and O, can play against each other
-The game checks for a winner after each move
-The game can be reset for a new round
-A winner line is drawn to highlight the winning combination

How to Play:
-Run the game by executing the Python script
-The game window will appear with a 3x3 grid and a "Restart Game" button
-Player X makes the first move by clicking on an empty cell
-Player O makes their move by clicking on an empty cell
-The game checks for a winner after each move
-If a player wins, a winner line is drawn and a message box appears to announce the winner
-If all cells are filled and no player has won, the game is a draw
-Click the "Restart Game" button to start a new round.

How to Run the Game:
To run the game, simply execute the tic_tac_toe.py file using Python.

Code Structure:
The code is organized into a single Python file, tic_tac_toe.py. The file contains a TicTacToe class that encapsulates the game logic. The class has several methods for creating the game grid, handling button clicks, checking for a winner, and drawing the winner line.

Code Explanation
Here is a brief explanation of the code:

TicTacToe class=
This class represents the Tic Tac Toe game and contains the main game logic. It initializes the game board, creates the GUI components, and handles the game flow.

create_grid method-
This method creates the 3x3 grid of buttons for the game.

on_button_click method-
This method handles the button click event, updates the game board, and checks for a win or a draw.

check_winner method-
This method checks for a winner by verifying the winning combinations in the 3x3 grid.

draw_winner_line method-
This method draws the winning line for the winning combination.

reset_game method-
This method resets the game for a new round.

Dependencies:
-Python 3.x
-Tkinter library (included with Python)
