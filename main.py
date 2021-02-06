from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as Controller
from time import sleep as s
boole = False
mouse = MouseController()
controller  = Controller()
def right():
    mouse.click(Button.left)
    s(.3)
    mouse.release(Button.left)
import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('|'): 
           # if key 'q' is pressed 
           boole = True
           while boole == True:
                if keyboard.is_pressed('-'):
                    boole = False  
                else:
                    right()
           print("pressed")
        """
        if keyboard.is_pressed('/'):
            controller.type("sethome \n")
        """
    except:
        print("not pressed")
