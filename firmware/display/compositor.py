import time
from firmware import settings 

class Compositor:
    def __init__(self, matrix, layers):
        self.matrix = matrix
        self.layers = layers
        self.last_time = time.time()
        self.last_brightness = settings.get_brightness() 
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
            current_brightness = settings.get_brightness()
            if current_brightness != self.last_brightness:
                self.matrix.matrix.brightness = current_brightness
                self.last_brightness = current_brightness
            # Swap display buffer
            canvas = self.matrix.matrix.SwapOnVSync(canvas)
            # Maintain target FPS
            elapsed = time.time() - start
            if elapsed < frame_duration:
                print("waiting") 
                time.sleep(frame_duration - elapsed)
    def update_layer(self, new_layers):
        self.layers = new_layers
