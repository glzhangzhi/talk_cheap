<<<<<<< HEAD
我的屏幕是托人从国内某宝带来的，IIC接口，十几块钱，在拒绝了大型LED屏幕和蓝牙鼠标键盘的诱惑，还是觉得用ssh连接比较极客和硬核。

在网上搜索了一番，发现很多教程都是基于树莓派自己家的oled屏，采用6针脚的，已经把针脚集合了，使用起来很方便，不需要自己连线。我找到的能4针脚能用的库是 [luma.oled](https://github.com/rm-hull/luma.oled) ,亲测可以使用，只是安装过程有些复杂，不过按照步骤一步步来的话也不会太过困难。

1.硬件连接。这个小屏共有四个针脚，分别是sck,sda,vcc,gnd，只需要分别连接到树莓派的对应接口即可。
2.使能树莓派i2c功能。在终端中输入`sudo raspi-config`，进入Interfacing Options，进入I2C项目，选择YES使能，一路确认，最后重启树莓派后，输入`dmesg | grep i2c`检查i2c功能是否成功启用。
3.授予用户使用i2c功能权限，并安装i2c工具，安装完成后重启。
```
sudo usermod -a -G i2c pi
sudo apt-get install i2c-tools
```
4.读取i2c总线状态。`i2cdetect -y 1`，找到屏幕地址。
5.更新相关插件和安装库

```
sudo apt install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5
sudo install luma.core
sudo install luma.oled
```

接下来就可以开始使用屏幕了，我的需求比较简单：
1）将显示功能打包成一个函数，输入参数是要显示的文本内容，可能出现的情况是存在多行或者某一行过长，所以所要求的功能是能够检测到换行后在屏幕中换行，并且能够对于过长的文本进行滚动处理。
2）能够在开机后自动读取自己的IP地址，并通过邮件和屏幕的方式告知使用者。
3）动态显示。例如显示进度条，显示实时运行进度，显示实时系统信息CPU占用、温度等。

目前的学习进度是能够使屏幕正常显示，代码如下
```python
from luma.core.interfacde.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

serial = i2c(port=1, address=0x3c)
device = ssd1306(serial,height=32)

with canvas(device) as draw:
	draw.text((0,0), "1th line", fill='white')
	draw.text((0,7), '2th line', fill='white')
	draw.text((0,14), '3th line', fill='white')
	draw.text((0,21), '4th line', fill='white')

time.sleep(2)
```
横向能显示21个字符，纵向能显示4行，目前不能显示汉字。

为了能供自动分行，需要编写一个字符串自动分行的小函数，以及检测换行符数量并根据换行符自动分配文本。关于滚动和翻页还在研究中。