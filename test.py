import time
import subprocess
BEEP_PATH = "firmware/audio/beep.wav"
_loop_process = None

def _apply_volume(vol_percent):
    """Set system PCM volume according to 0–100 global value."""
    vol = max(0, min(100, vol_percent))
    # Adjust 'PCM' channel volume
    subprocess.call(["amixer", "set", "PCM", f"{vol}%"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_sound_loop(vol):
    """Loop beep.wav continuously until stop_sound() is called."""
    global _loop_process

    stop_sound()  # stop previous loops
    _apply_volume(vol)

    # Loop using bash: while true; do aplay BEEP; done
    _loop_process = subprocess.Popen(
        ["bash", "-c", f"while true; do aplay -q {BEEP_PATH}; done"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(_loop_process)

def stop_sound():
    """Stops the looped sound if it's running."""
    global _loop_process
    if _loop_process is not None:
        _loop_process.terminate()
        _loop_process = None
play_sound_loop(50)
time.sleep(1)
stop_sound()
