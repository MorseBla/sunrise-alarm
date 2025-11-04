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
        self.cent_y = self.height / 2 + 5

        rotate_square = min(self.width, self.height) * 1.41
        self.min_rotate = self.cent_x - rotate_square / 2
        self.max_rotate = self.cent_x + rotate_square / 2

        display_square = min(self.width, self.height) * 0.5
        self.min_display = self.cent_x - display_square / 2
        self.max_display = self.cent_x + display_square / 2

        self.deg_to_rad = 2 * 3.14159265 / 360

        # Pre calculate colors
        self.col_table = []
        for x in range(int(self.min_rotate), int(self.max_rotate)):
            self.col_table.insert(x, scale_col(x, self.min_display, self.max_display))

        

    def update(self, canvas, dt):
         
        rotation = globals.getRot()
        rotation += 1
        rotation %= 360
        globals.updateRot(rotation)
        # calculate sin and cos once for each frame
        angle = rotation * self.deg_to_rad
        sin = math.sin(angle)
        cos = math.cos(angle)

        for x in range(int(self.min_rotate), int(self.max_rotate)):
            for y in range(int(self.min_rotate), int(self.max_rotate)):
                # Our rotate center is always offset by cent_x
                rot_x, rot_y = rotate(x - self.cent_x, y - self.cent_x, sin, cos)

                if x >= self.min_display and x < self.max_display and y >= self.min_display and y < self.max_display:
                    x_col = self.col_table[x]
                    y_col = self.col_table[y]
                    canvas.SetPixel(rot_x + self.cent_x, rot_y + self.cent_y, x_col, 255 - y_col, y_col)
                else:
                    pass
                    #canvas.SetPixel(rot_x + cent_x, rot_y + cent_y, 0, 0, 0)


# Main function
if __name__ == "__main__":
    rotating_block_generator = RotatingBlockGenerator()
    if (not rotating_block_generator.process()):
        rotating_block_generator.print_help()
