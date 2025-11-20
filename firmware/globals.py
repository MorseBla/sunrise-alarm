import time
import json
import os

rot = 0

def getRot():
    global rot
    return rot
def updateRot(newValue):
    global rot
    rot = newValue

def getTime():
    return time.localtime()

def load_alarms(filename="/Users/blakemorse/Desktop/sunrise-alarm/website/data/alarms.json"):
    # Expand ~ manually (Python won't expand it inside a string)
    filename = os.path.expanduser(filename)

    with open(filename, "r") as f:
        data = json.load(f)     # <-- data is a LIST

    # Return only enabled alarms
    return [a["time"] for a in data if a.get("enabled", True)]

def checkAlarm(filename="/Users/blakemorse/Desktop/sunrise-alarm/website/data/alarms.json"):
    print("checking alarm")

    now = time.localtime()
    current_time = f"{now.tm_hour:02d}:{now.tm_min:02d}"

    alarms = load_alarms(filename)

    if current_time in alarms:
        print("ALARM")


