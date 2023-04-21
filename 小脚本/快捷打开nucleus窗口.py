import pynput
from pynput.keyboard import Key
from pynput.mouse import Button
from time import sleep

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

sleep(2)

init_position = (107, 16)

current_position = mouse.position

keyboard.press(Key.ctrl)

X = [current_position[0] + 270 * i for i in range(5)]
Y = [current_position[1] + 200 * i for i in range(4)]
# print(X)
# print(Y)

for y in Y:
    for x in X:
        mouse.position = (x, y)
        mouse.click(Button.left)
        sleep(0.5)
        mouse.position = init_position
        mouse.click(Button.left)
        sleep(0.5)

keyboard.release(Key.ctrl)
exit()