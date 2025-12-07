import subprocess
import time
import socket
import os 

BEEP_PATH = "/home/admin/Desktop/real2/sunrise-alarm/firmware/audio/beep.wav"
NICE_PATH = "/home/admin/Desktop/real2/sunrise-alarm/firmware/audio/nice.wav"
_loop_process = None

SOCKET_PATH = "/tmp/sunrise_audio.sock"
try:
    os.remove(SOCKET_PATH)
except:
    pass
#--------------SOUND---------------------
def _apply_volume(vol_percent):
    """Set system PCM volume according to 0–100 global value."""
    vol = max(0, min(100, vol_percent))
    # Adjust 'PCM' channel volume
    subprocess.call(["amixer", "set", "Master", f"{vol}%"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_sound_loop(vol):
    """Loop beep.wav continuously until stop_sound() is called."""
    global _loop_process

    stop_sound()  # stop previous loops
    _apply_volume(vol)

    # Loop using bash: while true; do aplay BEEP; done
    _loop_process = subprocess.Popen(
        ["bash", "-c", f"while true; do aplay -q {NICE_PATH}; done"],
        #["bash", "-c", f"while true; do aplay -q {BEEP_PATH}; done"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    #print(_loop_process)

def stop_sound():
    """Stops the looped sound if it's running."""
    print("STOPPED") 
    global _loop_process
    if _loop_process is not None:
        _loop_process.terminate()
        _loop_process = None

def run_sound():
    print("playing sound")
    play_sound_loop(60)
    time.sleep(1)
    stop_sound()
run_sound()
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(SOCKET_PATH)
#print("created tmp file")
server.listen(1)

while True:
    conn, _ = server.accept()
    cmd = conn.recv(1024).decode().strip()

    if cmd == "PLAY_SOUND":
        run_sound()
    if cmd == "STOP_SOUND":
        stop_sound()

