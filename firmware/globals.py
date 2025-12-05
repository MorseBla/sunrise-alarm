import time
import json
import os
from firmware.display.matrix import MatrixController
from firmware.display.layers.animation import RainbowAnimation
from firmware.display.layers.clock import ClockOverlay
from firmware.display.layers.clock2 import ClockOverlay2
from firmware.display.compositor import Compositor
from firmware.display.layers.rotAnimation import RotatingBlockGenerator 
from firmware.display.layers.png_animation import PNGAnimationLayer
from firmware.display.layers.white_screen import WhiteScreen 
from firmware.display.layers.display_image import imageLayer 
from firmware.display.layers.black_screen import BlackScreen 
from firmware import led 
from firmware.audio import sound

SETTINGS_FILE = "/home/admin/Desktop/real/sunrise-alarm/website/data/settings.json"
rot = 0
state = 0
layer = 0
def getRot():
    global rot
    return rot
def updateRot(newValue):
    global rot
    rot = newValue

def getTime():
    return time.localtime()

def load_alarms(filename="/home/admin/Desktop/real/sunrise-alarm/website/data/alarms.json"):
    time.sleep(0.01)
    # Expand ~ manually (Python won't expand it inside a string)
    filename = os.path.expanduser(filename)

    with open(filename, "r") as f:
        data = json.load(f)     # <-- data is a LIST

    # Return only enabled alarms
    return [a["time"] for a in data if a.get("enabled", True)]

def checkAlarm(filename="/home/admin/Desktop/real/sunrise-alarm/website/data/alarms.json"):
    print("checking alarm")

    now = time.localtime()
    current_time = f"{now.tm_hour:02d}:{now.tm_min:02d}"

    alarms = load_alarms(filename)

    if current_time in alarms:
        print("ALARM")
        update_display(1)

def load_settings():
    """Load the settings JSON safely and return a dict."""
    time.sleep(0.1)
    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)
    return data

def get_volume():
    """Return the volume value from the JSON (default 100 if missing)."""
    data = load_settings()
    return data.get("volume", 100)

def get_brightness():
    """Return the brightness value from the JSON (default 100 if missing)."""
    data = load_settings()
    return data.get("brightness", 100)




matrix = MatrixController(rows=32, cols=32, chain=1)
layer0 = [
        ClockOverlay()
        ]
layer1 = [
    RainbowAnimation(matrix.options.cols, matrix.options.rows),
    RotatingBlockGenerator(),
    ClockOverlay()
]
layer2 = [
        imageLayer(image_file="firmware/display/animations/image1.png")
        ]
layer3 = [
        BlackScreen()
        ]
layer4 = [
    PNGAnimationLayer(folder="firmware/display/animations/sunrise1", width=32, height=32),
    ClockOverlay2()
]
layers= [layer0, layer1, layer2, layer3, layer4]
compositor = Compositor(matrix, layers[0])
red, green, blue, white = led.init()
def start(idx):
    global compositor 
    global state
    #state = 1
    #compositor.update_layer(layers[idx])
    volume_percent = get_volume()
    sound.play_sound_loop(0, volume_percent)
    #compositor.run(fps=30)

def update_leds(percent):
    global white
    white.ChangeDutyCycle(percent)

def led_off():
    global red, green, blue, white
    red.ChangeDutyCycle(0)
    green.ChangeDutyCycle(0)
    blue.ChangeDutyCycle(0)
    white.ChangeDutyCycle(0)

     
def update_display(idx):
    global compositor 
    compositor.update_layer(layers[idx])

def change_state(new_state): #state 0 = default state; state 1 = alarm state
    global state 
    if (state != new_state):
        if (new_state == 1):
            update_display(4) #alarm state
        else:
            update_display(0)
        state = new_state
    

def next_layer(): #change layer to next(state has to = 0)
    global layer 
    global state 
    if state == 0:
        layer = layer + 1
        if layer > 3:
            layer = 0
        update_display(layer)

def turn_off_alarm():
   change_state(0)
   led_off()
   #sound_off
