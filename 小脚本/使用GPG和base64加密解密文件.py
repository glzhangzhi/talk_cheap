import base64

# 解密
'''
1. 下载encrypted.asc文件
2. gpg --decrypt encrypted.asc > descrpted.txt
3. 从其中拆分出各个文件对应的加密段，并放到单独的txt文件中
4. open and read直接读取文件内容
5. a = base64.b64decode(读取的内容)
6. open(对应的文件名) wb f.write(a)
'''

with open("C:/Users/Administrator/Desktop/flowed.txt" , 'r') as f:
    content = f.read()
    
b64d = base64.b64decode(content)

with open("C:/Users/Administrator/Desktop/flowed.txt", 'wb') as f:
    f.write(b64d)


# 加密
'''
1. 模仿他的格式建立一个encrypted.txt文件模板
2. open(要加密的pdf) rb a = f.read()
3. b = base64.b64encode(a)
4. open(content.txt, w) f.write(b)
5. 复制对应的字符段到模板文件的对应位置
6. 用别人的公钥对encryped.txt文件进行加密，生成encrypted.asc
7. 发送encrypted.asc
'''

with open('C:/Users/Administrator/Desktop/EEG_Project.pdf', 'rb') as f:
    a = f.read()


b = base64.b64encode(a)

c = b.decode()

ind = 72

s = ''
for i in range(int(len(c) / 72) + 1):
    s = s + c[i * ind:(i + 1) * ind] + '\n'
print(s)

with open('content.txt', 'w') as f:
    f.write(s)

with open('content.txt', 'r') as f:
    t1 = f.read()

t2 = base64.b64decode(t1)

with open('t3.pdf', 'wb') as f:
    f.write(t2)