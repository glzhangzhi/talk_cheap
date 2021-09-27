<<<<<<< HEAD
```python
import gpiozero
button = gpiozero.Button(2)
```
将引脚2定义为按钮，并赋值给button变量

![引脚图](https://upload-images.jianshu.io/upload_images/16191347-96c47d515e52e390.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

该库使用的是自定义的引脚序号，如上图，而不是官方定义的引脚序号，如圈内所示

```python
from gpiozero import LED
from signal import pause
red = LED(17)
while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
```
或者
```python
red.blink()
pause()
```
单个LED灯闪烁程序
加入pause是因为程序运行到此处，会停止运行，需要加入一个指令，使程序保持激活状态，直到被人为用ctrl+C终止。同理可以用在一些需要等待按钮被检测的程序中：
```python
def hello():
    print("Hello")
button = Button(2)
button.when_pressed = hello
pause()
```
```python
from gpiozero import PWMLED
led = PWMLED(17)
while True:
    led.value = 0  # 亮度最低
    sleep(1)
    led.value = 0.5  # 一半亮度
    sleep(1)
    led.value = 1  # 最大亮度
    sleep(1)
```
LED灯亮度调节
```python
led = PWMLED(17)
led.pulse()
pause()
```
单个呼吸灯
```python
from gpiozero import Button
button = Button(2)
while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
```
检查按钮是否被按下
```python
from gpiozero import Button
button = Button(2)
button.wait_for_press()
print("Button was pressed")
```
键盘按下再继续运行程序
```python
from gpiozero import Button
from signal import pause
def say_hello():
    print("Hello!")
button = Button(2)
button.when_pressed = say_hello
#注意没有括号，并不是将函数的返回值赋予，而是it creates a reference to the function to be called when the button is pressed
pause()
```
当键盘按下时，执行某程序
```python
from gpiozero import Button
from signal import pause
def say_hello():
    print("Hello!")
def say_goodbye():
    print("Goodbye!")
button = Button(2)
button.when_pressed = say_hello
button.when_released = say_goodbye
pause()
```
当按钮弹起时执行某程序
```python
from gpiozero import LED, Button
from signal import pause
led = LED(17)
button = Button(2)
button.when_pressed = led.on
button.when_released = led.off
pause()
```
或者
```python
led.source = button.values
```
用按钮来控制LED灯
```python
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
button = Button(2)
camera = PiCamera()
def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)
button.when_pressed = capture
pause()
```
用按钮控制相机快门
```python
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
left_button = Button(2)
right_button = Button(3)
camera = PiCamera()
def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)
left_button.when_pressed = camera.start_preview
left_button.when_released = camera.stop_preview
right_button.when_pressed = capture
pause()
```
用一个按钮控制相机预览，一个控制快门
```python
from gpiozero import Button
from subprocess import check_call
from signal import pause
def shutdown():
    check_call(['sudo', 'poweroff'])
shutdown_btn = Button(17, hold_time=2)
shutdown_btn.when_held = shutdown
pause()
```
关机
```python
from gpiozero import LEDBoard
from time import sleep
from signal import pause
leds = LEDBoard(5, 6, 13, 19, 26)
leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1, 0, 1)
sleep(1)
leds.blink()
pause()
```
LED板
```python
from gpiozero import LEDBoard
from signal import pause
leds = LEDBoard(5, 6, 13, 19, 26, pwm=True)
leds.value = (0.2, 0.4, 0.6, 0.8, 1.0)
pause()
```
控制LED板的亮度
```python
from gpiozero import LEDBarGraph
from time import sleep
graph = LEDBarGraph(5, 6, 13, 19, 26, pwm=True)
graph.value = 1/10  # (0.5, 0, 0, 0, 0)
sleep(1)
graph.value = 3/10  # (1, 0.5, 0, 0, 0)
sleep(1)
graph.value = -3/10  # (0, 0, 0, 0.5, 1)
sleep(1)
graph.value = 9/10  # (1, 1, 1, 1, 0.5)
sleep(1)
graph.value = 95/100  # (1, 1, 1, 1, 0.75)
sleep(1)
```
LED条的开关和亮度
```python
from gpiozero import TrafficLights
from time import sleep
lights = TrafficLights(2, 3, 4)
lights.green.on()
while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.amber.on()
    sleep(1)
    lights.green.on()
    lights.amber.off()
    lights.red.off()
```
```python
from gpiozero import TrafficLights
from time import sleep
from signal import pause
lights = TrafficLights(2, 3, 4)
def traffic_light_sequence():
    while True:
        yield (0, 0, 1) # green
        sleep(10)
        yield (0, 1, 0) # amber
        sleep(1)
        yield (1, 0, 0) # red
        sleep(10)
        yield (1, 1, 0) # red+amber
        sleep(1)
lights.source = traffic_light_sequence()
pause()
```
```python
from gpiozero import LED
from time import sleep
red = LED(2)
amber = LED(3)
green = LED(4)
green.on()
amber.off()
red.off()
while True:
    sleep(10)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(10)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()
```
使用三种方法制作交通灯信号
```python
from gpiozero import Button
from picamera import PiCamera
button = Button(2)
camera = PiCamera()
camera.start_preview()
frame = 1
while True:
    button.wait_for_press()
    camera.capture('/home/pi/frame%03d.jpg' % frame)
    frame += 1
```
每按一次按钮，拍一张照片
```python
from gpiozero import LED, Button
from time import sleep
from random import uniform
led = LED(4)
right_button = Button(15)
left_button = Button(14)
led.on()
sleep(uniform(5, 10))
led.off()
def pressed(button):
	print(str(button.pin.number) + ' won the game')
right_button.when_pressed = pressed
left_button.when_pressed = pressed
```
