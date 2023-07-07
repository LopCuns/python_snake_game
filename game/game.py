"""Snake game code"""

import tkinter as tk
from classes.snake import Snake
from classes.apple import Apple
from constants.tk_constants import ROOT, MAIN_WIDTH
from constants.game_constants import CANVAS_BG, PART_WIDTH, GAME_SPEED, GAME_DELAY
# Create the game frame
game = tk.Frame(ROOT, width=MAIN_WIDTH, height=MAIN_WIDTH)
# Display game frame in the grid
game.grid(column=0, row=2)
# Create the canvas and pack it the ROOT
main_canvas = tk.Canvas(game, widt=MAIN_WIDTH, height=MAIN_WIDTH, bg=CANVAS_BG)
main_canvas.pack()


def game_over(score):
    """Function to be executed when user loses"""
    # Generate the game over text
    main_canvas.create_text(
        (main_canvas.winfo_reqwidth() - 4) / 2,
        (main_canvas.winfo_reqheight() - 4) / 2,
        text=f'Game Over\n Score:{score}',
        fill='red', font=('Helvetica', 30, 'bold'), justify='center'
    )
    # End the game loop
    game.quit()


# initialise the game

def init_game():
    """Function to initialize the game"""
    # Clear the canvas
    main_canvas.delete('all')
    # Snake draw
    game_snake = Snake(main_canvas, PART_WIDTH)
    # Apple draw
    game_apple = Apple(main_canvas, PART_WIDTH)
    # Set the event to controll the snake movement

    def controls(event):
        """Controller to move snake"""
        # Change snake direction according to keyboard click
        allowed_keys = ('Up', 'Down', 'Left', 'Right')
        # Unallowed consecutive actions (if one is performed snake cracks)
        unallowed_sequences = (
            ('Up', 'Down'),
            ('Down', 'Up'),
            ('Left', 'Right'),
            ('Right', 'Left')
        )
        pressed_key = event.keysym
        # Prevent user from pressing a key that is not a control
        if pressed_key not in allowed_keys:
            return game_over(game_snake.get_length())
        # Avoid snake head crack
        if (game_snake.moving_to, pressed_key) in unallowed_sequences and \
                game_snake.get_length() > 1:
            return
        game_snake.moving_to = pressed_key
    # Create the moving snake loop function

    def game_loop():
        """Loop to move snake"""
        # If the apple is reached
        if game_apple.coords in [[coord[0], coord[1]] for coord in game_snake.coords]:
            # Increase the snake length
            game_snake.coords.append(
                game_snake.create_part(
                    game_snake.coords[-1][0],
                    game_snake.coords[-1][1]
                )
            )
            # Change apple position
            game_apple.change_position()
        # Execute the snake movement according to current direction and
        # if the movement results in a game over condition, end the game
        if game_snake.movements[game_snake.moving_to]() == 'over':
            return game_over(game_snake.get_length())
        # Repeat the game loop
        game.after(GAME_SPEED, game_loop)
    # Bind the game controls
    ROOT.bind('<Key>', controls)
    # Start the game after a second
    game.after(GAME_DELAY, game_loop)
    game.mainloop()
