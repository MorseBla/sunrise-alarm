import time
from rgbmatrix import graphics

class ClockOverlay(Layer):
    def __init__(self, font_path="/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf"):
        self.font = graphics.Font()
        self.font.LoadFont(font_path)
        self.color = graphics.Color(255, 255, 255)
        self.last_draw = 0
        self.text_cache = ""

    def update(self, canvas, dt):
        now = time.localtime()
        current_text = time.strftime("%H:%M:%S", now)
        
        # Redraw only if text changed to save time
        if current_text != self.text_cache:
            self.text_cache = current_text
            self.last_draw = time.time()

        # Position (bottom-right corner)
        #x = canvas.width - len(current_text)*8 - 2
        x = 2
        y = canvas.height - 2

        graphics.DrawText(canvas, self.font, x, y, self.color, current_text)

