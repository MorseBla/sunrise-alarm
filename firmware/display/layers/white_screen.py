# firmware/display/layers/white_screen.py

from firmware.display.layers.base import Layer

class WhiteScreen(Layer):
    def __init__(self, width=32, height=32):
        super().__init__()
        self.width = width
        self.height = height

    def update(self, canvas, dt):
        # fill entire canvas with white (255,255,255)
        for y in range(self.height):
            for x in range(self.width):
                canvas.SetPixel(x, y, 255, 255, 255)

