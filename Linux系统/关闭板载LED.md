将以下命令写入/etc/rc.local，没有的话可以新建一个，记得加上文件头#! /bin/sh -e 和文件结尾 exit 0

```
sudo sh -c 'echo none > /sys/class/leds/led0/trigger'
sudo sh -c 'echo none > /sys/class/leds/led1/trigger'
sudo sh -c 'echo 0 > /sys/class/leds/led0/brightness'
sudo sh -c 'echo 0 > /sys/class/leds/led1/brightness'
```

