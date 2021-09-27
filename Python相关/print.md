```python
print(1)
print('a')
print(b)
print('i am %s and i am %d years old' %(Ginie, 18))
```
常用字符串格式化符号
```
%c #字符和ASCII码
%s #字符串
%d #整型
%o #八进制
%x #十六进制
%f #浮点型
```
常用格式化辅助符
```
m.n. #定义输出宽度和精度
* #代替宽度和精度
0 #用0填补前部空缺
- #左对齐
```
格式化输出浮点数
```python
pi = 3.141592653
print('%10.3f' %pi) #宽度10，精度3
print('%.*f' %(3, pi)) #在后方读取宽度
print('%-10.3f' %pi) #左对齐
```
打印时的换行符和分隔符控制
```python
for i in range(6)
    print(i, sep=',', end=' ') #分隔符为逗号，换行符为空格，即实现不换行
```