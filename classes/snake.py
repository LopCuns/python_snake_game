"""Snake class"""

from collections import Counter
from random import choice


class Snake():
    """Class for snake in the game"""
    # Initilize the class

    def __init__(self, canvas, pwidth):
        # Snake part width
        self.pwidth = pwidth
        # Canvas that holds the game
        self.canvas = canvas
        # Snake part colors
        self.colors = ('green', 'blue', 'orange', 'yellow')
        # Snake movements by direction
        self.movements = {
            'Up': lambda: self.move_snake(0, - self.pwidth),
            'Down': lambda: self.move_snake(0, self.pwidth),
            'Left': lambda: self.move_snake(- self.pwidth, 0),
            'Right': lambda: self.move_snake(self.pwidth, 0)
        }
        # Coords of each part of the snake
        self.coords = [self.create_part(0, 0, 'green')]
        # Head coords
        self.get_head_coords = lambda: (self.coords[0][0], self.coords[0][1])
        # Snake length
        self.get_length = lambda: len(self.coords)
        # Moving direction
        self.moving_to = 'Down'

    def create_part(self, x, y, pcolor=None):
        """Create a new part"""
        part_color = pcolor if pcolor  else choice(self.colors)
        part = (x,
                y,
                self.canvas.create_rectangle(
                    x, y, x + self.pwidth, y + self.pwidth, fill=part_color
                ),
                part_color
                )
        return part

    def move_snake(self, move_x, move_y):
        """Move the snake to the given coords"""
        # Game over if snake exceeds canvas limit
        for part in reversed(self.coords):
            # Get part index
            index = self.coords.index(part)
            # Get the new x and y positions
            new_x = part[0] + \
                move_x if index == 0 else self.coords[index - 1][0]
            new_y = part[1] + \
                move_y if index == 0 else self.coords[index - 1][1]
            # If snake exceeds horizontal limit, game over
            if max(min(new_x, self.canvas.winfo_reqwidth() - 5), 0) != new_x:
                return 'over'
            # If snake exceeds vertical limit, game over
            if max(min(new_y, self.canvas.winfo_reqheight() - 5), 0) != new_y:
                return 'over'
            # Delete the current part draw from the canvas
            self.canvas.delete(part[2])
            # Create the new draw and update the coords
            self.coords[index] = (
                self.create_part(new_x, new_y, part[3])
            )
        # If two ore more snake parts are in the same position, game over
        if Counter([(coord[0], coord[1]) for coord in self.coords]).most_common(1)[0][1] > 1:
            return 'over'
        return 'continue'

