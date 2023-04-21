from time import sleep
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key

def on_press(key):
    if key == Key.esc:
        return False
    elif key == Key.up:
        save()
    else:
        pass
    
def on_release(key):
    pass

mouse = pynput.mouse.Controller()

position = (1467, 1031)

def save():
    mouse.position = position
    mouse.click(Button.left)
    sleep(1)

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# sleep(3)
# print(mouse.position)