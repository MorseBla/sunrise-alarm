import time
import json

SETTINGS_FILE = "/home/admin/Desktop/real/sunrise-alarm/website/data/settings.json"
#--------------------settings------------------
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
