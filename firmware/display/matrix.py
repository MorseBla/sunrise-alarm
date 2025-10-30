from rgbmatrix import RGBMatrix, RGBMatrixOptions

class MatrixController:
    def __init__(self, rows=64, cols=64, chain=1, parallel=1, brightness=100, mapping='adafruit-hat'):
        self.options = RGBMatrixOptions()
        self.options.rows = rows
        self.options.cols = cols
        self.options.chain_length = chain
        self.options.parallel = parallel
        self.options.hardware_mapping = mapping
        self.options.brightness = brightness
        self.options.drop_privileges = False  # stay as root if needed

        self.matrix = RGBMatrix(options=self.options)
        self.canvas = self.matrix.CreateFrameCanvas()

    def clear(self):
        self.canvas.Clear()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def set_pixel(self, x, y, r, g, b):
        self.canvas.SetPixel(x, y, r, g, b)

    def show(self):
        self.canvas = self.matrix.SwapOnVSync(self.canvas)

