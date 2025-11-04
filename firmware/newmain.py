from firmware.display.matrix import MatrixController
from firmware.display.layers.animation import RainbowAnimation
from firmware.display.layers.clock import ClockOverlay
from firmware.display.compositor import Compositor
from firmware.display.layers.rotAnimation import RotatingBlockGenerator 

def main():
    matrix = MatrixController(rows=32, cols=32, chain=1)
    layers = [
        RainbowAnimation(matrix.options.cols, matrix.options.rows),
        RotatingBlockGenerator(),
        ClockOverlay()
    ]

    compositor = Compositor(matrix, layers)
    compositor.run(fps=60)

if __name__ == "__main__":
    main()

