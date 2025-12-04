import os
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from firmware.display.layers.base import Layer  # adjust path if needed


class imageLayer(Layer):
    def __init__(self, image_file, width=32, height=32):
        super().__init__()
        img = Image.open(image_file).convert("RGB")
        self.width = width
        self.height = height
        self.image = img.resize((width, height))

    def update(self, canvas):
        canvas.SetImage(self.image)

