```python
f = open('/User/michael/test/txt','r') #用读的方式打开此路径下的一个文件
f.read() #一次性读取文件所有内容，返回的是str类型
f.close() #关闭文件，节省系统资源
```
```python
try:
	f = open('/User/michael/test/txt','r')
	print(f.read())
finally:
	if f:
		f.close()
```
```python
with open('/User/michael/test/txt','r') as f:
	print(f.read())
```
为保证文件能在被成功打开的情况下进行之后的操作并在操作完成后关闭，建议采用上面两种方式打开文件
```python
f = open('/Users/michael/test.jpg', 'rb') #二进制格式读取文件，如图片，视频
```

```python
f = open('/Users/michael/gbk.txt', 'rb') #用二进制打开并用gbk解码
u = f.read().decode('gbk')

f = open('utf-8.txt', 'rb')
u = f.read().decode('utf-8')  # 使用这个流程，可以解决大部分中英文混合的txt文件读取问题

import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() 
```
```python
with open('t.txt','a') as f: #参数为a意思是在文件末尾添加
    f.write(str + '/n')
```
```python
f = open('/Users/michael/test.txt', 'w') #参数为wb时为二进制写入
f.write('Hello, world!')
f.close()
```
```python
with open('/Users/michael/test.txt', 'w', encoding='utf-8') as f: #如果不带编码参数写入，系统会自动建立gbk编码的文件，会引起后续的写入和保存过程中的错误
	f.write('Hello, world!')
```
```python
import codecs
with codecs.open('/Users/michael/gbk.txt', 'wb', 'gbk') as f: #自动转码的写法
    f.write('Hello, world!')
```
```python
fh = open('c:\\autoexec.bat','r')         
for line in fh.readlines():   #常用的按行读入的操作                   
	print(line)
```
```python
f = open("sxl.txt")
lines = f.read() #一次读取所有文件内容，并保存到一个str中
print lines 
f.close()
```
```python
f = open("sxl.txt")
line = f.readline() #只读取一行
while line:             #直到读不到内容为止
    print (line)
    line = f.readline() #再读取一行
f.close()
```
```python
f = open("sxl.txt")
lines = f.readlines() #按行读取，并形成一个list
for line in lines:    #逐行调用list
    print (line)
f.close()
```