# firmware/audio/sound.py

import pygame
import threading
import time
import os

from firmware.globals import get_volume 

SOUND_DIR = "firmware/sounds"

pygame.mixer.init()
_current_channel = None
_running = False
_play_thread = None


def _load_sounds():
    sounds = []
    for file in sorted(os.listdir(SOUND_DIR)):
        if file.lower().endswith((".wav", ".mp3", ".ogg")):
            path = os.path.join(SOUND_DIR, file)
            sounds.append(pygame.mixer.Sound(path))
    return sounds


SOUNDS = _load_sounds()


def _apply_volume(sound):
    """Apply volume 0-100 (mapped to 0.0-1.0) from settings.json."""
    vol_percent = get_volume()            # 0–100
    vol = max(0.0, min(1.0, vol_percent / 100.0))
    sound.set_volume(vol)


def play_sound(idx):
    """Play a sound by index in a loop until stop_sound() is called."""
    global _running, _play_thread, _current_channel

    stop_sound()  # stop anything currently playing

    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return

    _running = True
    sound = SOUNDS[idx]

    # Set volume RIGHT BEFORE playing
    _apply_volume(sound)

    def _loop():
        global _running, _current_channel

        # loop forever until stop_sound()
        _current_channel = sound.play(loops=-1)

        while _running:
            time.sleep(0.1)

        # cleanup when stopping
        if _current_channel:
            _current_channel.stop()
            _current_channel = None

    _play_thread = threading.Thread(target=_loop, daemon=True)
    _play_thread.start()


def stop_sound():
    """Stop any playing sound."""
    global _running, _current_channel
    _running = False

    if _current_channel:
        _current_channel.stop()
        _current_channel = None

