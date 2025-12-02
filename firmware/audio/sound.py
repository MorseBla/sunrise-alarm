# sound.py
import pygame
import threading
import time
import os

SOUND_DIR = "firmware/sounds"

pygame.mixer.init()
_current_channel = None
_lock = threading.Lock()

def _load_sounds():
    sounds = []
    for file in sorted(os.listdir(SOUND_DIR)):
        if file.lower().endswith((".mp3", ".wav", ".ogg")):
            path = os.path.join(SOUND_DIR, file)
            sounds.append(pygame.mixer.Sound(path))
    return sounds

SOUNDS = _load_sounds()

_play_thread = None
_running = False


def play_sound(idx):
    """Play a sound by index in a loop until stop_sound() is called."""
    global _play_thread, _running, _current_channel

    stop_sound()  # stop any existing playback

    if idx < 0 or idx >= len(SOUNDS):
        print("Invalid sound index:", idx)
        return

    _running = True

    def _play_loop():
        global _running, _current_channel

        sound = SOUNDS[idx]
        _current_channel = sound.play(loops=-1)  # infinite loop

        while _running:
            time.sleep(0.1)

        # Stop when _running becomes False
        if _current_channel is not None:
            _current_channel.stop()
            _current_channel = None

    _play_thread = threading.Thread(target=_play_loop, daemon=True)
    _play_thread.start()


def stop_sound():
    """Stop any playing sound immediately."""
    global _running, _current_channel

    _running = False
    if _current_channel:
        _current_channel.stop()
        _current_channel = None

