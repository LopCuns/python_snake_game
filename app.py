"""Snake game"""

import tkinter as tk
from webbrowser import open as wopen
from game.game import init_game
from constants.tk_constants import ROOT
from constants.tk_constants import MAIN_WIDTH
# Create upper text
welcome = tk.Label(ROOT, text='Snake game made by jlopcuns')
# Create the button frame
buttons = tk.Frame(ROOT, width=MAIN_WIDTH)
BUTTONS_FONT = ('Helvetica', 10, 'bold')
# Create the start button
start_game_btn = tk.Button(
    buttons, text='Start/Restart the game', font=BUTTONS_FONT, command=init_game, bg='#abf7bf')
# Create the github button
github_btn = tk.Button(
    buttons, text='Check out my github!', bg='#f5f5f5',
    command=lambda: wopen('https://github.com/LopCuns/'),
    font=BUTTONS_FONT
)
# Exit button
exit_btn = tk.Button(
    buttons, text='Exit the game',
    command=ROOT.destroy, bg='#f7abbb', font=BUTTONS_FONT
)
# Display the buttons in its frame grid
github_btn.grid(column=0, row=0, padx=10)
start_game_btn.grid(column=1, row=0, padx=10)
exit_btn.grid(column=2, row=0, padx=10)
# Display the elements in a grid
welcome.grid(column=0, row=0)
buttons.grid(column=0, row=1)
# Display ROOT in the middle of screen
ROOT.update()
ROOT_WIDTH = ROOT.winfo_width()
ROOT_HEIGHT = ROOT.winfo_height()
X_ALIGN = int((ROOT.winfo_screenwidth() - ROOT_WIDTH) / 2)
Y_ALIGN = int((ROOT.winfo_screenheight() - ROOT_HEIGHT) / 2)
ROOT.geometry(
    f'{ROOT_WIDTH}x{ROOT_HEIGHT}+{X_ALIGN}+{Y_ALIGN}'
)
# Start the ROOT loop
ROOT.mainloop()
