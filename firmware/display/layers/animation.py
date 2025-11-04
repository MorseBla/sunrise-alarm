import time
import colorsys
from .base import Layer


class RainbowAnimation(Layer):
    def __init__(self, width, height, speed=0.0016):
        self.width = width
        self.height = height
        self.hue = 0
        self.speed = speed

    def update(self, canvas, dt):
        self.hue = (self.hue + self.speed) % 1.0
        r, g, b = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
        R, G, B = int(r * 255), int(g * 255), int(b * 255)

        for x in range(self.width):
            for y in range(self.height):
                canvas.SetPixel(x, y, R, G, B)
                #canvas.SetPixel(x, y, 0, 0, 0)
