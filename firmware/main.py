import time
from display.matrix import MatrixController

def main():
    matrix = MatrixController(rows=64, cols=64, chain=1)

    # Fill screen with a color sweep
    for x in range(matrix.options.cols):
        for y in range(matrix.options.rows):
            matrix.set_pixel(x, y, x % 256, y % 256, (x*y) % 256)
        matrix.show()
        time.sleep(0.01)

    # Keep the display static
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

