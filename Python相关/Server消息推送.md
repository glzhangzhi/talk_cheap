本来想研究一个树莓派开机以后发送ip地址到邮箱的脚本，没想到发现一个新世界。

Server酱，对我来说简单理解就是一个从服务器到微信的消息端口。

1. 用Github登陆网站sc.ftqq.com/?c=github&a=login，同时获得自己的SCkey

2. 点击微信推送，扫码关注以后完成绑定

3. 用
```python
    requests.post('https://sc.ftqq.com/SCKEY.send?text=消息内容')
```
即可向微信发送消息，注意将其中的SCKEY替换成自己的。同样的文本一分钟只能发送一次。

