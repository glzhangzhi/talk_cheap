尽量将两个互相引用的文件放在同一个目录下
```python
from filename import funname #引用函数和类
funname（）
```
```python
import os
os.system('filename.py') #运行另一个python程序
```
```python
from sys import path
path.append(r'E:\sldjflsdjf\') #涉及到不同文件夹的话
import filename
```
尝试下来，发现如果直接放在同一个目录进行调用的话，在shell中运行会发生找不到被调用文件的情况
于是我最后采用的方法是：
依然将被调用文件放在同一个目录下，但是不是直接在一个文件里运行另一个文件，而是将被调用的功能打包成函数，然后在另一个文件里直接调用该函数

```python
import SendTheMail
SendTheMail.send_the_mail()
```
这里顺便说一下python里的相对路径和绝对路径
```python
open('test1.txt') #相对路径，在同一个文件夹下
open('/temp/test2.txt') #相对路径，在该文件夹的子文件夹里
open('D:\\user\\test3.txt') #绝对路径
open(r'D:\user\temp\test4.txt') #绝对路径
```
在python中，/表示相对路径，\表示绝对路径，第三句使用\\是使用了转义符，因为\在python里已经被占用了，用来表示转义字符，如\n表示换行, \r表示回车, \t表示tab，第四句前加r，表示后面的字符串没有任何转义的意思
python中可以获得当前目录的绝对路径或者当前目录父目录的绝对路径
```python
path1 = os,path.abspath('.')
path2 = os.path.abspath('..')
```
可以将某目录添加到系统搜索目录中
```python
sys,path.append(path1) #将目录路径添加到最后
sys.path.insert(0, path2) #将目录插入到搜索顺序的第一个
```
现在来总结归纳一下：
假设现在存在如下目录关系：
![目录关系](https://upload-images.jianshu.io/upload_images/16191347-5f73aff557e4ec1c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

同一目录下的导入：在c中导入d
```python
import d
```
子目录下的导入：在b中导入c
```python
在F2目录中建立一个名为_init_.py的空文件，然后
import F2.c
```
父目录下的导入：在c中导入b
```python
import sys
sys.path.append('..')
import b
```
平级目录的下的导入：在c中导入e
```python
在F3目录中建立一个名为_init_.py的空文件，然后
import sys
sys.path.append('..')
import F3.e
```