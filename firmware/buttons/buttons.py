from gpiozero import Button
from signal import pause
from firmware import globals

btn3 = Button(25, pull_up=False, bounce_time=0.05) #display mode
btn2 = Button(18, pull_up=False, bounce_time=0.05) #volume switch
btn1 = Button(11, pull_up=False, bounce_time=0.05) #alarm toggle

def handle_btn1():
    print("alarm on/off")
    globals.turn_off_alarm()

def handle_btn2():
    print("volume toggle")

def handle_btn3():
    print("display cycle")
    globals.next_layer()

def init_buttons():
    print("Buttons active.")
    btn1.when_pressed = handle_btn1
    btn2.when_pressed = handle_btn2
    btn3.when_pressed = handle_btn3

