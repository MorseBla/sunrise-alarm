from firmware import globals 
from firmware.buttons.buttons import init_buttons
    
def main():
    init_buttons() 
    globals.start(2)
if __name__ == "__main__":
    main()

