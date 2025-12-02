import os
import time
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from firmware.display.layers.base import Layer  # adjust path if needed


class PNGAnimationLayer(Layer):
    def __init__(self, folder, width=32, height=32):
        super().__init__()
        self.folder = folder
        self.frame_delay = 10.0
        self.width = width
        self.height = height
        self.frames = []
        self.last_time = time.time()
        self.current_frame = 0

        # Load and preprocess all frames
        self._load_frames()

    def _load_frames(self):
        """Load all PNGs in the folder, sort them by filename, and resize."""
        files = sorted(f for f in os.listdir(self.folder) if f.lower().endswith(".png"))
        if not files:
            print(f"[WARN] No PNGs found in {self.folder}")
            return

        for file in files:
            path = os.path.join(self.folder, file)
            img = Image.open(path).convert("RGB")
            img = img.resize((self.width, self.height), Image.LANCZOS)
            self.frames.append(img)

        print(f"[INFO] Loaded {len(self.frames)} frames from {self.folder}")

    def update(self, canvas, dt):
        """Draw the current frame and advance based on FPS."""
        if not self.frames:
            return

        now = time.time()
        if now - self.last_time >= self.frame_delay and self.current_frame < len(self.frames) - 1:
            self.last_time = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)

        frame = self.frames[self.current_frame]
        canvas.SetImage(frame)

