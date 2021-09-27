[http://www.pyinstaller.org/](http://www.pyinstaller.org/)
具体用到一个py的第三方库pyinstaller，能够用在2.7和3.4-3.7版本上

安装很简单
```
pip install pyinstaller
```
具体就这么用，先要使用命令行cd到文件所在的目录，然后
```
pyinstaller -F yourprogram.py
```
然后在你文件所在目录下，就会找到一个dist文件夹，其下有个yourprogram的文件夹，里面找个yourprogram.exe
搞定

-F 将所有文件打包成一个exe，否则会生成一个目录

-w 不显示控制台

如果出现错误RecursionError: maximum recursion depth exceeded：

先按正常流程执行一遍pyinstaller xxx.py，会生成xxx.spec，打开这个文件，在文件第二行加上

import sys

sys.setrecursionlimit(5000)

然后执行pyinstaller xxx.spec