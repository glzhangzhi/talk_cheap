# 安装

```pip install keyboard```

# 例子

```python
import keyboard

keyboard.press_and_release('shift+s, space')
# 单击shift+s组合键和空格键

keyboard.write('The quick brown fox jumps over the lazy dog')
# 输入文本

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
# 当检测到按下c+s+a时，执行函数print，输出参数为args内容

keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
# 按下上下翻页键来输入文本

keyboard.wait('esc')
# 阻塞直到按下esc

recorded = keyboard.recond(until='ecs')
# 录制事件直到按下esc

keyboard.play(recorded, speed_factor=3)
# 播放所录制的事件，三倍速

keyboard.add_abbreviation('@@', 'my.long.email@example.com')
# 输入@@，之后按空格，来将@@替换成文本

keyboard.wait()
# 一直阻塞，类似于while True
```

# 常见模式和错误

## 防止程序关闭
错误：
```python
while True:
    some function
```

正确：
```python
some function
keyboard.wait()
```

## 等待直到某个事件发生
错误：
```python
while True:
    if keyboard.is_pressed('space'):
        print('space was pressed')
```

正确：
```python
while True:
    keyboard.wait('space')
    print('space was pressed')
```

或者：
```python
keyboard.add_hotkey('space', lambda:print('space was pressed'))
```

## 发生某事件时执行函数
错误：
```python
keyboard.add_hotkey('space', print('space was pressed'))
```

正确：
```python
keyboard.add_hotkey('space', lambda: print('space was pressed'))
```

或者：
```python
def on_space():
    print('space was pressed')
keyboard.add_hotkey('space', on_space)
```

## 按任意键继续
错误：
```python
print('press any key to continue')
keyboard.get_event()
```

正确：
```python
input('press any key to continue')
```