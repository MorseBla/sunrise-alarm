# firmware/audio/sound.py

import pygame
import threading
import time
import os

from firmware.globals import get_volume

SOUND_DIR = "firmware/sounds"

pygame.mixer.init()

LOOP_CHANNEL = pygame.mixer.Channel(0)
ONCE_CHANNEL = pygame.mixer.Channel(1)

_running = False
_loop_thread = None



def _load_sounds():
    """Load all .wav/.mp3/.ogg audio files from SOUND_DIR."""
    sounds = []
    for file in sorted(os.listdir(SOUND_DIR)):
        if file.lower().endswith((".wav", ".mp3", ".ogg")):
            path = os.path.join(SOUND_DIR, file)
            sounds.append(pygame.mixer.Sound(path))
    return sounds


SOUNDS = _load_sounds()



def _apply_volume(sound):
    """Apply global volume from 0–100 to a pygame Sound object."""
    vol_percent = get_volume()  # from settings.json
    vol = max(0.0, min(1.0, vol_percent / 100.0))
    sound.set_volume(vol)


def play_sound_once(idx):
    """Play a sound once in the background without blocking."""
    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return

    sound = SOUNDS[idx]
    _apply_volume(sound)

    def _worker():
        ONCE_CHANNEL.play(sound, loops=0)
        # thread exits immediately

    threading.Thread(target=_worker, daemon=True).start()



def play_sound_loop(idx):
    """Play a sound in a loop until stop_sound() is called."""
    global _running, _loop_thread

    stop_sound()  # stop any existing looped sound

    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return

    sound = SOUNDS[idx]
    _apply_volume(sound)
    _running = True

    def _loop():
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

