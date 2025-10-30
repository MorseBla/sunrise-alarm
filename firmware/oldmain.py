import time
import threading
import json

import display
import sound

stop_event = threading.Event()


def clock_loop():
    while not stop_event.is_set():
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # TODO: actuallly implement this function then fix sytax here
        showtime(hour, minute, second))
        
        time.sleep(1 - time.time() % 1)
      
def watch_settings():
    last_mtime = 0 #mtime = modified time (time last modified)
    while not stop_event.is_set():
        mtime = os.path.getmtime("settings.json")
        if mtime != last_mtime:
            last_mtime = mtime
            update_settings()


if __name__ == "__main__":
       threading.Thread(target=clock_loop, daemon=True).start() 
       threading.Thread(target=watch_settings, daemon=True).start() 

       try:
           while True:
               time.sleep(1)
        except KeyboardInterrupt:
            stop_event.set()
