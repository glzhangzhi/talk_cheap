# 一般功能

```python
import pyautogui

pyautogui.position()

pyautogui.size()
```

# 安全模式

```python
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True
```

# 鼠标功能

```python
pyautogui.moveTo(x, y, duration=num_seconds)
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

pyautogui.dragTo(x, y, duration=num_seconds)
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)

pyautogui.click(x=moveToX, y=moveToY, clicks=num_clicks, interval=secs_between_clicks, button='middle')
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY) # 正数向上滚，负数向下滚

pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
```

# 键盘功能

```python
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
# 可在pyautogui.KEYBOARD_KEYS

pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)
```

# 消息窗口

```python
pyautogui.alert('This displays some text with an OK button')
pyautogui.confirm('This displays text nd has an OK and Cancel button')
pyautogui.prompt('This lets the user typein a string and press OK')
```

# 截屏功能

```python
# 在linux系统中需要单独安装依赖
# sudo apt-get install scrot

pyautogui.screenshot()
pyautogui.screenshot('goo.png')
pyautogui.screenshot(region=(0,0,300,400))

loc = pyautogui.locateOnScreen('lookslikethis.png')
cen = pyautogui.center(loc)

for i in pyautogui.locateAllOnScreen('looklikethis.png'):
    print(i)
    
pyautogui.locateCenterOnScreen('looklikethis.png')
# grayscale=True
# confidence=0.9

im = pyautogui.screenshot()
im.getpixel((100, 200))
# 获得某像素点的RGB值
```



