import time
import json

rot = 0

def getRot():
    global rot
    return rot
def updateRot(newValue):
    global rot
    rot = newValue

def getTime():
    return time.localtime()

def load_alarms(filename="~/Desktop/sunrise-alarm/firmware/alarms.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [a["time"] for a in data.get("alarms", [])]

def checkAlarm(filename="firmware/alarms.json"):
    print("checking alarm")
    now = time.localtime()
    current_time = f"{now.tm_hour:02d}:{now.tm_min:02d}"
    alarms = load_alarms(filename)
    if current_time in alarms:
        print("ALARM")
