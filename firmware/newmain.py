from display.matrix import MatrixController
from display.layers.animation import RainbowAnimation
from display.layers.clock import ClockOverlay
from display.compositor import Compositor

def main():
    matrix = MatrixController(rows=64, cols=64, chain=1)
    layers = [
        RainbowAnimation(matrix.options.cols, matrix.options.rows),
        ClockOverlay()
    ]

    compositor = Compositor(matrix, layers)
    compositor.run(fps=30)

if __name__ == "__main__":
    main()

