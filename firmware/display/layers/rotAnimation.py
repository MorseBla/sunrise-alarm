from .base import Layer
import math
from firmware import globals 

def scale_col(val, lo, hi):
    if val < lo:
        return 0
    if val > hi:
        return 255
    return 255 * (val - lo) / (hi - lo)


def rotate(x, y, sin, cos):
    return x * cos - y * sin, x * sin + y * cos
class RotatingBlockGenerator(Layer):
    def __init__(self):
        self.width = 32
        self.height = 32
        self.cent_x = self.width / 2
        self.cent_y = self.height / 2
        self.deg_to_rad = math.pi / 180

        display_square = min(self.width, self.height) * 0.5
        self.min_display = self.cent_x - display_square / 2
        self.max_display = self.cent_x + display_square / 2

    def update(self, canvas, dt):
        rotation = (globals.getRot() + 1) % 360
        globals.updateRot(rotation)

        angle = rotation * self.deg_to_rad
        sin_t = math.sin(angle)
        cos_t = math.cos(angle)

        # loop over every destination pixel
        for y_out in range(self.height):
            for x_out in range(self.width):
                # compute which source (x, y) this pixel corresponds to
                x_src = cos_t * (x_out - self.cent_x) + sin_t * (y_out - self.cent_y) + self.cent_x
                y_src = -sin_t * (x_out - self.cent_x) + cos_t * (y_out - self.cent_y) + self.cent_y

                # check if that source coordinate lies within your square
                if (self.min_display <= x_src < self.max_display and
                    self.min_display <= y_src < self.max_display):
                    # simple color function based on source coords
                    valx = int(255 * (x_src - self.min_display) / (self.max_display - self.min_display))
                    valy = int(255 * (y_src - self.min_display) / (self.max_display - self.min_display))
                    canvas.SetPixel(x_out, y_out, valx, 255 - valy, valy)
                else:
                    canvas.SetPixel(x_out, y_out, 0, 0, 0)


# Main function
if __name__ == "__main__":
    rotating_block_generator = RotatingBlockGenerator()
    if (not rotating_block_generator.process()):
        rotating_block_generator.print_help()
