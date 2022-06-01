## 一个简单的例子

```python
import pyautogui #读取模块
screenWidth, screenHeight = pyautogui.size() #读取屏幕长宽
pyautogui.moveTo(screenWidth / 2, screenHeight / 2) #将鼠标移动到屏幕中间
```
## 鼠标相关API

```python
currentMouseX, currentMouseY = pyautogui.position() #读取鼠标当前位置
#左上角为坐标原点，X轴向右，Y轴向下

pyautogui.moveTo(100, 150) #移动到坐标100，150
pyautogui.moveRel(None, 10)  #鼠标向下移动10
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # 使用tweening/easing函数，设置duration参数使移动持续2秒，如果不设置，就是鼠标闪现到目标点（mac不支持闪现操作
pyautogui.dragTo(x, y, duration=num_seconds)  # 拖拽操作

pyautogui.click() #点击
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left') #在xy目标点，点击次数num_of_clicks，间隔interval，左键left（中middle，右right）
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

pyautogui.mouseDown(x=moveToX, y=moveToY, button='left') #在指定位置按下鼠标
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left') #在指定位置放开鼠标

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY) #滚动屏幕，可以设定鼠标点和滚动距离，正上负下
```
## 键盘相关API
```python
pyautogui.typewrite('Hello world!', interval=0.25)  #输入hello world，每个字符间隔0.25秒
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

pyautogui.press('esc') #按esc键
pyautogui.keyDown('shift') #按下shift键
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left']) #按左箭头键6次
pyautogui.keyUp('shift') #弹起shift键
pyautogui.hotkey('ctrl', 'c') #组合键ctrl+c
```
## 弹出提示框相关API
```python
pyautogui.alert('This displays some text with an OK button.') #弹出提示框，只有一个确定按钮
pyautogui.confirm('This displays text and has an OK and Cancel button.') #选择框，返回'ok'或'cancel'字符串
pyautogui.prompt('This lets the user type in a string and press OK.') #输入框，返回输入的字符串

```
## 可用的一些键盘按键
```python
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

## 紧急中断功能

介于本库是用于控制鼠标和键盘操作的，所以当程序卡死或者运行错误，中断程序就会变得有些困难。因此该库会默认开启安全功能。当需要紧急退出时，只需要将鼠标移动到屏幕的左上角，因此你需要做的就是，在鼠标被控制的前提下，疯狂将鼠标向左上角移动即可，这也给了程序设计者一点提示，就是在设计鼠标动作的时候，特别是在循环里的鼠标动作，不要将时序填充得过满，不然会导致程序无法中断的尴尬情况。程序中默认每个动作执行的间隔是0.1秒，可以使用PAUSE参数调整，避免执行过快导致一些问题。

```python
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 2.5 
```

## 截屏与找图
```python
im = pyautogui.screenshot('foo.png', region=(0, 0, 300, 300)) #截图并保存为文件，设定截图区域，在linux系统中需要安装scrot来启用截图功能。截图功能依赖Pillow库
loc = pyautogui.locateOnScreen('foo.png'，confidence=0.9) #找图并返回位置信息，confidence可选参数定义精确度
#可以传入region参数定义搜索区域，grayscale参数设定灰度搜索
#此处返回的信息为图片的left, top, width, height
#left值可分别用loc.left和loc[1]取出
#在1920*1080的分辨率下，截屏大概要花费1~2秒的时间
loc_center = pyautogui.center(loc) #将此组信息传递给center函数，可以算出图片的中心位置
loc_center = pyautogui.locateCenterOnScreen('foo.png') #定位和取中心的结合
#返回的值为中心的XY左边，可用loc_center[1]和loc_center.x取出
pyautogui.click('foo.png') #click方法可以直接将图片作为参数，直接点击图片的中心，如果图片找到的话
pyautogui.locateAllOnScreen('foo.png') #返回所有找到对应图片的位置的List
im.pixel(x,y) #得到截图指定点的RGB信息
```