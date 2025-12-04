import RPi.GPIO as GPIO
import time



def init():
    # --- GPIO Setup ---
    GPIO.setmode(GPIO.BCM)

    # PWM pins
    pins = [9, 10, 14, 15]
    red = 9
    green = 10
    blue = 15
    white = 14

    # Set all pins as outputs
    for p in pins:
        GPIO.setup(p, GPIO.OUT)

    # Setup pwm on separate channels corresponding to colors
    pwmRed =  GPIO.PWM(red, 1000)    # 1 kHz PWM
    pwmGreen = GPIO.PWM(green, 1000)  # 1 kHz PWM
    pwmBlue = GPIO.PWM(blue, 1000)  # 1 kHz PWM
    pwmWhite = GPIO.PWM(white, 1000)  # 1 kHz PWM

    # Start PWM with 0% duty (LED off)
    pwmRed.start(0)
    pwmGreen.start(0)
    pwmBlue.start(0)
    pwmWhite.start(0)

    return pwmRed, pwmGreen, pwmBlue, pwmWhite

