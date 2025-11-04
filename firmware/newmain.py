from firmware.display.matrix import MatrixController
from firmware.display.layers.animation import RainbowAnimation
from firmware.display.layers.clock import ClockOverlay
from firmware.display.compositor import Compositor
from firmware.display.layers.rotAnimation import RotatingBlockGenerator 
import time


def getTime():
    return time.localtime()

def load_alarms(filename="alarms.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [a["time"] for a in data.get("alarms", [])]

def checkAlarm(filename="alarms.json"):
    print("checking alarm")
    now = time.localtime()
    current_time = f"{now.tm_hour:02d}:{now.tm_min:02d}"
    alarms = load_alarms(filename)
    if current_time in alarms:
        print("ALARM")
    
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

