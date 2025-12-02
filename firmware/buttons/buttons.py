from gpiozero import Button
from signal import pause

btn1 = Button(25, pull_up=False, bounce_time=0.05) #alarm toggle
btn2 = Button(18, pull_up=False, bounce_time=0.05) #volume switch
btn3 = Button(11, pull_up=False, bounce_time=0.05) #display mode

def handle_btn1():
    print("alarm on/off")

def handle_btn2():
    print("volume toggle")

def handle_btn3():
    print("display mode")


def init_buttons():
    print("Buttons active.")
    btn1.when_pressed = handle_btn1
    btn2.when_pressed = handle_btn2
    btn3.when_pressed = handle_btn3

