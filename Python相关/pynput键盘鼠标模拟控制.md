[TOC]

# 控制鼠标

```python
from pynput.mouse import Button, Controller

mouse = Controller()

print(f'the current pointer position is {mouse.position}')
# 读取鼠标位置

mouse.position = (10, 20)
print(f'now we have moved it to {mouse.position}')
# 用目的地坐标的方式改变鼠标位置

mouse.move(5, -5)
# 用相对距离的方式改变鼠标位置

mouse.press(Button.left)
mouse.release(Button.left)
# 按下放开左键

mouse.click(Botton.left, 2)
# 单击左键两次

mouse.scroll(0, 2)
# 向下滚动鼠标滚轮两次
```

# 监控鼠标

```python
from pynput import mouse

def on_move(x, y):
    print(f'pointer move to {(x, y)}')

def on_click(x, y, button, pressed):
    print(f'{"pressed" if pressed else "released"} at {(x, y)}')
	if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print(f'scrolled {"down" if dy < 0 else "up"} at {(x, y)}')
   
with mouse.Listener(
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll) as listener:
    listener.join()
# ...or, in a non-blocking faction:
#listener = mouse.Listener(
#    on_move=on_move,
#    on_click=on_click,
#    on_scroll=on_scroll)
#listener.start()
```

# 控制键盘

```python
from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.space)
keyboard.release(Key.space)

keyboard.press('a')
keyboard.release('a')
# keyboard.tap('a')

keyboard.press('A')
keyboard.press('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
    
keyboard.type('Hello World')
```

# 监控键盘

```python
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fuction:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
```

