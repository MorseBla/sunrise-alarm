import time
from rgbmatrix import graphics
from .base import Layer
from firmware import globals

class ClockOverlay2(Layer):
    def __init__(self, font_path="/home/admin/Desktop/sunrise-alarm/firmware/display/fonts/4x6.bdf"): #5x8 or 6x12
    #def __init__(self, font_path="/home/admin/Desktop/sunrise-alarm/firmware/display/fonts/6x12.bdf"): #5x8 or 6x12
        self.font = graphics.Font()
        self.font.LoadFont(font_path)
        self.color = graphics.Color(255, 255, 255)
        #self.color = graphics.Color(0, 0, 0)
        self.last_draw = 0
        self.text_cache = ""
        self.font_width = 4
        self.font_height = 6
        self.background_color = 0

    def update(self, canvas, dt):
        #now = time.localtime()
        now = globals.getTime()
        current_text = time.strftime("%H:%M:%S", now)
        #print(current_text)
        current_text = current_text[:-3]
        # Redraw only if text changed to save time
        if current_text != self.text_cache:
            self.text_cache = current_text
            self.last_draw = time.time()
            globals.checkAlarm()

        # Position (bottom-right corner)
        #x = canvas.width - len(current_text)*8 - 2
        x = 7
        #y = canvas.height/2  + self.font_height/2
        y = canvas.height - 1 -1 
        #y = self.font_height +1
        text_width = len(current_text) * self.font_width

        pad = 0
        rect_x0 = x -1
        rect_y0 = y - self.font_height 
        rect_x1 = x + text_width - 1 
        rect_y1 = y 

        
        rect_x0 = max(0, rect_x0)
        rect_y0 = int(max(0, rect_y0))
        rect_x1 = min(canvas.width - 1, rect_x1)
        rect_y1 = int(min(canvas.height - 1, rect_y1))
       

        for xx in range(rect_x0, rect_x1 + 1):
            for yy in range(rect_y0, rect_y1 + 1):
                canvas.SetPixel(xx, yy, self.background_color, self.background_color, self.background_color)

        graphics.DrawText(canvas, self.font, x, y, self.color, current_text)

