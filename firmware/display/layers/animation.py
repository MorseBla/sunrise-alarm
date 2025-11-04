import time

class RainbowAnimation(Layer):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hue = 0

    def update(self, canvas, dt):
        for x in range(self.width):
            for y in range(self.height):
                r = (x + self.hue) % 256
                g = (y * 2 + self.hue) % 256
                b = ((x + y) // 2 + self.hue) % 256
                canvas.SetPixel(x, y, r, g, b)
        self.hue = (self.hue + 2) % 256

