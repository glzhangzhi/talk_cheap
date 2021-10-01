from pynput.mouse import Controller
from keyboard import add_hotkey, wait
from pyautogui import click as Click
from time import sleep

# mouse = Controller()
# while 1:
#     print(mouse.position)

# that's for little monitor
firstRow_Y = 899
secondRow_Y = 956
Position = {
    '-300': (1364, firstRow_Y),
    '-30': (1433, firstRow_Y),
    '-5': (1492, firstRow_Y),
    '-1': (1550, firstRow_Y),
    '+1': (1615, firstRow_Y),
    '+5': (1669, firstRow_Y),
    '+30': (1737, firstRow_Y),
    '+300': (1832, firstRow_Y),
    'pre': (1447, secondRow_Y),
    'start': (1538, secondRow_Y),
    'end': (1653, secondRow_Y),
    'next': (1736, secondRow_Y)
}


# that's for company big LG monitor
# firstRow_Y = 916
# secondRow_Y = 971
# Position = {
#     '-300': (966, firstRow_Y),
#     '-30': (1034, firstRow_Y),
#     '-5': (1095, firstRow_Y),
#     '-1': (1152, firstRow_Y),
#     '+1': (1212, firstRow_Y),
#     '+5': (1274, firstRow_Y),
#     '+30': (1339, firstRow_Y),
#     '+300': (1416, firstRow_Y),
#     'pre': (1047, secondRow_Y),
#     'start': (1133, secondRow_Y),
#     'end': (1253, secondRow_Y),
#     'next': (1335, secondRow_Y)
# }


time_interval = 0.05


def click(button):
    p = Position[button]
    Click(p)
    sleep(time_interval)


# add_hotkey('h', click, args=('-1', ))
# add_hotkey('j', click, args=('+1', ))
add_hotkey('a', click, args=('-5', ))
add_hotkey('d', click, args=('+5', ))
add_hotkey('s', click, args=('-30', ))
add_hotkey('w', click, args=('+30', ))
add_hotkey('j', click, args=('start', ))
add_hotkey('k', click, args=('end', ))
# add_hotkey('r', click, args=('pre', ))
add_hotkey('o', click, args=('next', ))
# add_hotkey('g', click, args=('-300', ))
# add_hotkey('k', click, args=('+300', ))
wait('q')
