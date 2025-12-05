# firmware/audio/sound.py

import pygame
import threading
import time
import os


SOUND_DIR = "firmware/audio"

pygame.mixer.init()

LOOP_CHANNEL = pygame.mixer.Channel(1)
ONCE_CHANNEL = pygame.mixer.Channel(2)

_running = False
_loop_thread = None

def _load_sounds():
    """Load all .wav/.mp3/.ogg audio files from SOUND_DIR."""
    sounds = []
    print("1")
    time.sleep(0.5) 
    for file in sorted(os.listdir(SOUND_DIR)):
        if file.lower().endswith((".wav", ".mp3", ".ogg")):
            path = os.path.join(SOUND_DIR, file)
            print(path)
            sounds.append(pygame.mixer.Sound(path))
    return sounds


SOUNDS = _load_sounds()



def _apply_volume(sound, vol_percent):
    """Apply global volume from 0–100 to a pygame Sound object."""
    vol = max(0.0, min(1.0, vol_percent / 100.0))
    sound.set_volume(vol)


def play_sound_once(idx, volume_percent):
    """Play a sound once in the background without blocking."""
    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return

    sound = SOUNDS[idx]
    _apply_volume(sound, volume_percent)

    def _worker():
        ONCE_CHANNEL.play(sound, loops=0)
        # thread exits immediately

    threading.Thread(target=_worker, daemon=True).start()



def play_sound_loop(idx, volume_percent):
    """Play a sound in a loop until stop_sound() is called."""
    global _running, _loop_thread
    stop_sound()  # stop any existing looped sound

    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return
    sound = SOUNDS[idx]
    _apply_volume(sound, volume_percent)
    _running = True

    print(idx)
    def _loop():
        print("thread started")
        LOOP_CHANNEL.set_volume(1.0)
        LOOP_CHANNEL.play(sound, loops=-1)
       
        while _running:
            time.sleep(0.1)
        LOOP_CHANNEL.stop()

    _loop_thread = threading.Thread(target=_loop, daemon=True)
    _loop_thread.start()


# stop any looping sound
def stop_sound():
    """Stop looped sound playback immediately."""
    global _running
    _running = False
    LOOP_CHANNEL.stop()
