# firmware/audio/sound.py

import pygame
import os
from firmware.globals import get_volume

# Path to the single audio file
BEEP_PATH = "firmware/audio/beep.wav"

# -----------------------------
#  MIXER INITIALIZATION
# -----------------------------

pygame.mixer.pre_init(44100, -16, 2, 1024)  # safer buffer size for Raspberry Pi
pygame.mixer.init()

pygame.mixer.set_num_channels(16)

# Use high-numbered channels so nothing else interferes
LOOP_CHANNEL = pygame.mixer.Channel(10)
ONCE_CHANNEL = pygame.mixer.Channel(11)

# -----------------------------
#  LOAD SOUND
# -----------------------------

if not os.path.exists(BEEP_PATH):
    raise FileNotFoundError(f"Beep sound not found at: {BEEP_PATH}")

BEEP_SOUND = pygame.mixer.Sound(BEEP_PATH)


# -----------------------------
#  VOLUME HANDLING
# -----------------------------

def _apply_volume(sound):
    """Apply volume from settings.json (0–100 → 0.0–1.0)."""
    vol_percent = get_volume()
    vol = max(0.0, min(1.0, vol_percent / 100.0))
    sound.set_volume(vol)


# -----------------------------
#  PUBLIC FUNCTIONS
# -----------------------------

def play_sound_once():
    """Play the beep sound once (non-blocking)."""
    _apply_volume(BEEP_SOUND)
    ONCE_CHANNEL.play(BEEP_SOUND, loops=0)


def play_sound_loop():
    """Loop the beep sound forever until stop_sound() is called."""
    _apply_volume(BEEP_SOUND)
    LOOP_CHANNEL.stop()  # clear previous playback
    LOOP_CHANNEL.play(BEEP_SOUND, loops=-1)


def stop_sound():
    """Stop the looping beep sound."""
    LOOP_CHANNEL.stop()
