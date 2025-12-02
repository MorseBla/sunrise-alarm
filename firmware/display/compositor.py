import time
from firmware import globals

class Compositor:
    def __init__(self, matrix, layers):
        self.matrix = matrix
        self.layers = layers
        self.last_time = time.time()
        self.last_brightness = globals.get_brightness() 
    def run(self, fps=30):
        frame_duration = 1.0 / fps
        canvas = self.matrix.canvas
        while True:
            start = time.time()
            dt = start - self.last_time
            self.last_time = start
        
            # Clear before redrawing
            canvas.Clear()

            # Update each layer in order
            for layer in self.layers:
                layer.update(canvas, dt)
            current_brightness = globals.get_brightness()
            if current_brightness != self.last_brightness:
                self.matrix.matrix.brightness = current_brightness
                self.last_brightness = current_brightness
            # Swap display buffer
            canvas = self.matrix.matrix.SwapOnVSync(canvas)

            # Maintain target FPS
            elapsed = time.time() - start
            if elapsed < frame_duration:
                time.sleep(frame_duration - elapsed)

