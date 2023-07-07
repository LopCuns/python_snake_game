"""Apple class"""

from random import randrange


class Apple():
    """Apple class"""

    def __init__(self, canvas, size):
        self.canvas = canvas
        # Apple size
        self.size = size
        # Set the x and y position of the apple
        self.coords = [
            randrange(0, self.canvas.winfo_reqwidth() - 4, self.size),  # x
            randrange(0, self.canvas.winfo_reqheight() - 4, self.size)  # y
        ]
        # Apple draw in the canvas
        self.draw = self.create_apple_draw()

    def change_position(self):
        """Change apple position"""
        # Change apple coordinates
        self.coords[0] = randrange(0, self.canvas.winfo_width() - 4, self.size)
        self.coords[1] = randrange(
            0, self.canvas.winfo_height() - 4, self.size)
        # Delete the current apple draw and create a new one
        self.canvas.delete(self.draw)
        self.draw = self.create_apple_draw()

    def create_apple_draw(self):
        """Create an apple in the canvas"""
        return self.canvas.create_rectangle(
            self.coords[0], self.coords[1],
            self.coords[0] + self.size, self.coords[1] + self.size,
            fill='red'
        )
