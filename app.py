"""Snake game"""

import tkinter as tk
from webbrowser import open as wopen
from game.game import init_game
from constants.tk_constants import root
from constants.tk_constants import MAIN_WIDTH
# Create upper text
welcome = tk.Label(root, text='Snake game made by jlopcuns')
# Create the button frame
buttons = tk.Frame(root, width=MAIN_WIDTH)
# Create the start button
start_game_btn = tk.Button(buttons, text='Start/Restart the game', command=init_game,bg='#abf7bf')
# Create the github button
github_btn = tk.Button(
    buttons, text='Check out my github!', bg='#f5f5f5',
    command=lambda: wopen('https://github.com/LopCuns/')
)
# Exit button
exit_btn = tk.Button(buttons,text='Exit the game',command=root.destroy,bg='#f7abbb')
# Display the buttons in its frame grid
github_btn.grid(column=0, row=0, padx=10)
start_game_btn.grid(column=1, row=0, padx=10)
exit_btn.grid(column=2, row=0, padx=10)
# Display the elements in a grid
welcome.grid(column=0, row=0)
buttons.grid(column=0, row=1)
# Start the root loop
root.mainloop()
