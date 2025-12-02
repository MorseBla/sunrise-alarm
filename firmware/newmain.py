from firmware.display.matrix import MatrixController
from firmware.display.layers.animation import RainbowAnimation
from firmware.display.layers.clock import ClockOverlay
from firmware.display.layers.clock2 import ClockOverlay2
from firmware.display.compositor import Compositor
from firmware.display.layers.rotAnimation import RotatingBlockGenerator 
from firmware.display.layers.png_animation import PNGAnimationLayer
from firmware.display.layers.white_screen import WhiteScreen 
    
def main():
    matrix = MatrixController(rows=32, cols=32, chain=1)
    layer1 = [
        RainbowAnimation(matrix.options.cols, matrix.options.rows),
        RotatingBlockGenerator(),
        ClockOverlay()
    ]
    layer2 = [
        PNGAnimationLayer(folder="firmware/display/animations/sunrise1", width=32, height=32),
        ClockOverlay2()
    ]
    layers= [layer1, layer2]
    compositor = Compositor(matrix, layers[0])
    compositor.run(fps=30)

if __name__ == "__main__":
    main()

