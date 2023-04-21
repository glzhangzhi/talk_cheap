# LCD1602 + HD44780

GND --> GND

VCC --> 5v

SDA --> SDA1

SCL  -->  SCL1



sudo pip install PRLCD

sudo apt-get install python3-smbus

sudo raspi-config

lsmod

sudo nano /etc/modules

i2c-bcm2708

i2c-dev

sudo apt-get install i2c-tools

i2cdetect -y 1

i2cdump -y 1 0x27

i2cset -y 1 0x68 0x00 0x13

i2cget -y 1 0x68 0x00




```python
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)            
# Initialisiere LCD Modul 
#'PFC8574' ->Chip des Treibers  
# #0x27 -> I2C Adresse 
lcd.cursor_pos = (0,0)                
# Setze Cursor auf Zeile 0 und Spalte 0
lcd.write_string('Raspberry Pi HD44780')
lcd.cursor_pos = (1, 0)
lcd.write_string('https://github.com/\n\rdbrgn/RPLCD')
```

```python
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, auto_linebreaks = False)

def scroll_text(text, digits, lcd):
    
    for shifts in range(1,digits+1,1):
        lcd.clear()
        print('here')
        lcd.cursor_pos = (0,(digits-shifts))
        print(lcd.cursor_pos)
        lcd.write_string(text[:shifts])
        time.sleep(0.4)
               
        
    for outshift in range(1,len(text)+1,1):
        lcd.clear()
        print('here2')
        lcd.cursor_pos = (0, (digits-shifts))
        lcd.write_string(text[outshift:len(text)])
        time.sleep(0.4)
        
        
scroll_text("abcasdf Laufschrift", 16, lcd)
```

https://rplcd.readthedocs.io/en/latest/index.html

https://blog.csdn.net/zh_666888/article/details/87875877



# 3.5 inch LCD

https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(A)



修改时区

sudo dpkg-reconfigure tzdata

# push

pushplus.push
