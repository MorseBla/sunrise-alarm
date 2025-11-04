import time
from display.matrix import MatrixController

def main():
    matrix = MatrixController(rows=32, cols=32, chain=1)

    # Fill screen with a color sweep
    for x in range(matrix.options.cols + 1):
        for y in range(matrix.options.cols):
            for z in range(x):
                #matrix.set_pixel(z, y, z % 256, y % 256, (z*y) % 256)
                matrix.set_pixel(z, y, 255,255,255 )
             
        
        matrix.show()
        time.sleep(0.01)

    # Keep the display static
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

