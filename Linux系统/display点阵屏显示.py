from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

#需要先安装luma.core库和luma.oled库
#本函数是将要显示的字符串和要显示的时间传入函数内，并进行字符串的切割，
#使其能满足128*32屏幕的显示要求

def dis_show(cc,t):
	print(cc,t)
	serial = i2c(port=1, address=0x3c)
	device = ssd1306(serial,height=32)
	# cc = '1234567890123456789012345678901234567890'

	X = cc
	O=[]
	if len(X)>84 :
		X = X[:84]
	print(X)

	while len(X)>21 :
		O.append(X[0:21])
		X = X[21:]
	print(O,X)

	O.append(X)

	print(O)

	with canvas(device) as draw:
		n=0
		for c in O :
			draw.text((0,n*7), c, fill='white')
			n=n+1

	time.sleep(t)