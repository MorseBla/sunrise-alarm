from gpiozero import Button
from signal import pause
from sound import play_sound, stop_sound

btn1 = Button(25, pull_up=True, bounce_time=0.05) #alarm toggle
btn2 = Button(8, pull_up=True, bounce_time=0.05) #volume switch
btn3 = Button(7, pull_up=True, bounce_time=0.05) #display mode

def handle_btn1():
    print("alarm on/off")

def handle_btn2():
    print("volume toggle")

def handle_btn3():
    print("display mode")

btn1.when_pressed = handle_btn1
btn2.when_pressed = handle_btnk
btn3.when_pressed = handle_btn3

def start_button_listener():
    print("Buttons active.")

