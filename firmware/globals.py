import time
import json
import os
SETTINGS_FILE = "/home/admin/Desktop/real/sunrise-alarm/website/data/settings.json"
rot = 0

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

def load_settings():
    """Load the settings JSON safely and return a dict."""
    time.sleep(0.01)
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
