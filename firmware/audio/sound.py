# firmware/audio/sound.py

import subprocess
import time

BEEP_PATH = "firmware/audio/beep.wav"

# store Popen handle for looped playback
_loop_process = None


# -----------------------------
#  VOLUME HANDLING
# -----------------------------

def _apply_volume():
    """Set system PCM volume according to 0–100 global value."""
    vol = max(0, min(100, vol_percent))
    # Adjust 'PCM' channel volume
    subprocess.call(["amixer", "set", "PCM", f"{vol}%"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# -----------------------------
#  PLAY ONCE
# -----------------------------

def play_sound_once(vol):
    """Play beep.wav once (non-blocking)."""
    _apply_volume(vol)
    subprocess.Popen(["aplay", "-q", BEEP_PATH])  # -q = quiet output


# -----------------------------
#  LOOPING PLAYBACK
# -----------------------------

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


# -----------------------------
#  STOP LOOP
# -----------------------------

def stop_sound():
    """Stops the looped sound if it's running."""
    global _loop_process
    if _loop_process is not None:
        _loop_process.terminate()
        _loop_process = None

