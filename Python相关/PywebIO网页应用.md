[TOC]

这个一个python的web应用库，主要作用是在不了解web知识的前提下，使用web作为python脚本的输入输出方式。

# 基础程序
```python
from pywebio.input import input, FLOAT
from pywebio.output import put_text

def add2(a, b):
    result = a + b
    return result

def main():
    a = input(type=FLOAT)
    b = input(type=FLOAT)
    result = add2(a, b)
    put_text(result)

if __name__ == '__main__':
    main()
```
运行以上程序，会自动打开一个网页，可以在文本框里输入，并将结果输出在网页上

# 作为后台web服务使用
```python
pywebio.start_server(main, port=8080)
```
若是将上面程序的最后一行换成这个，就可以将python脚本当作网页服务运行在后台，这样只要输入这个网址，就可以使用该服务 http://localhost:8080



# 不同的输入方式

```python
from pywebio.input import *

input("What's your name?")  # 文本输入
select('Select', ['A', 'B'])  # 下拉选择
checkbox("Checkbox", options=['Check me'])  # 多选
radio("Radio", options=['A', 'B', 'C'])  # 单选
textarea('Text', placeholder='Some text')  # 多行文本输入
file_upload("Select a file:")  # 文件上传
```

# 不同的输出方式
```python
from pywebio.output import *

put_text("Hello world!")# 输出文本
put_table([['Product', 'Price'],['Apple', '$5.5'],['Banner', '$7']])  # 输出表格
put_image(open('python-logo.png', 'rb').read())  # 输出图像
put_markdown('**Bold text**')  # 输出MarkDown
toast('Awesome PyWebIO!!')  # 输出通知消息
put_file('hello_word.txt', b'hello word!')  # 输出文件

with popup('Popup title'):  # 显示弹窗
  put_text("Hello world!")
  put_table([['Product', 'Price'],['Apple', '$5.5'],['Banner', '$7'],])

def on_click(btn):  # 输出可以点击的按钮
  put_markdown("You click `%s` button" % btn)
put_buttons(['A', 'B', 'C'], onclick=on_click)

import time  # 输出进度条
put_processbar('bar1');
for i in range(1, 11):
  set_processbar('bar1', i / 10) # 更新进度条
  time.sleep(0.1)
```