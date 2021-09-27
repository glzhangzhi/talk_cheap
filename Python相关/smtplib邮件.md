https://zhuanlan.zhihu.com/p/24180606
主要根据这个教程来学习如何使用python发送邮件
首先在邮箱处开启SMTP服务，我没找到outlook的在哪里开启，所以只能使用126邮箱作为发件人

```python
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.126.com'  
#163用户名
mail_user = '159*****02'  
#密码(部分邮箱为授权码) 
mail_pass = '7******x'   
#邮件发送方邮箱地址
sender = '159*****02@126.com'  
#邮件接受方邮箱地址，注意需要[]包裹，多个收件人时，在‘’内使用，隔开
receivers = ['59*****02@outlook.com']  

#设置email信息
#邮件内容设置
message = MIMEText('我的天，你收到我这封邮件了吗','plain','utf-8') #注意这里，如果不把content内容改掉，很可能被126认为是垃圾邮件，不允许发送
#邮件主题       
message['Subject'] = '今儿天气真的好啊' #同内容，这里需要注意的是，标题最好不要是test，针对126邮箱的话最好不要是英文，否则可能会被认为是垃圾邮件
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
```
这样应该就能正确收到一封邮件
下面是发送一封复合内容的邮件
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置登录及服务器信息
mail_host = 'smtp.163.com'
mail_user = '159*****02'
mail_pass = '7******x'
sender = '159*****02@163.com'
receivers = ['7******0@qq.com']

#设置eamil信息
#添加一个MIMEmultipart类，处理正文及附件
message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'title'
#推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
with open('abc.html','r') as f:
    content = f.read()
#设置html格式参数
part1 = MIMEText(content,'html','utf-8')
#添加一个txt文本附件
with open('abc.txt','r')as h:
    content2 = h.read()
#设置txt参数
part2 = MIMEText(content2,'plain','utf-8')
#附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
#添加照片附件
with open('1.png','rb')as fp:
    picture = MIMEImage(fp.read())
    #与txt文件设置相似
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="1.png"'
#将内容附加到邮件主体中
message.attach(part1)
message.attach(part2)
message.attach(picture)

#登录并发送
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)
```
目前纯文本已经很能满足我发送提醒邮件的需求，所以复合类型的邮件以后再研究