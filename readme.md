# Snake game 

Snake game version built using [Python](https://docs.python.org/3/) and [tkinter library](https://docs.python.org/3/library/tk.html).
To code this app using tkinter I follwed the [tkinter official tutorial](https://tkdocs.com/tutorial/index.html).

# File description
 - app.py : Create window interface.
 - constants/tk_constants.py: initialize tkinter root.
 - game/game.py: Game frame, canvas and game logic.
 - classes
    - snake.py: snake class.
    - apple.py: apple class.

# Functionalities
  - When opening the game, a text saying 'Snake game by LopCuns' is seen with three buttons, one to start the game and other to go to author's github and another one to exit the game.
  - Snake moves through the canvas an when it eats an apple, it increases it's size by one part.
  - If the snake exceeds the limits of the canvas, game over.
  - If two or more snake parts are in the same position, game over.
  - If the game is over, show a text saying 'game over' and the user score.