```python
from wxpy import *
bot = Bot()
myself = bot.self
bot.file_helper.send('Hello from wxpy')
```
Bot的主要参数
cache_path 设置当前会话的缓存路径，默认None为关闭，True时开启，可避免短时间内重复扫码，默认路径为wxpy.pkl
console_qr 默认False，开启时会在终端显示二维码，需要安装pilow
qr_path 保存二维码的路径

```python
bot.enable_puid('wxpy.pkl')
my_friend = bot.friends().search('aa')[0]
print(my_friend.puid)
```
读取缓存的会话，并显示aa的puid，这个是该库独有的属性，稳定唯一且一直可获取

```python
Bot.self  # 自己
Bot.file_helper  # 文件传输助手
Bot.friends()  # 所有好友
Bot.groups()  # 所有群聊
Bot.mps()  # 所有公众号
```
获取聊天对象

```python
found = bot.friends().search('游否', sex=MALE, city='深圳')
youfou = ensure_one(found)
# 查找好友名字带有游否，性别为男，所在城市为深圳，并确保结果唯一
wxpy_groups = bot.groups().search('wxpy', [youfou])
group = wxpy_groups[0]
found = group.search(province='浙江')
# 查找群聊名字带有wxpy，群成员中youfou，进一步查找群成员中省份为浙江的
found = bot.search('wxpy')
# 查找所有聊天对象中带有wxpy
```
查找聊天对象
```python
Bot.add_friend(user, verify_content='')
Bot.add_mp(user)
Bot.accept_friend(user, verify_content='')
```
添加好友、公众号，接受好友申请
```python
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'wxpy' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')
```
```python
Bot.user_details(user_or_users, chunk_size= 50)
# 获取单个或批量获取多个用户的详细信息
Bot.upload_file(path)
# 上传图片、表情、视频、文件
Bot.logout()
# 登出当前账号
bot1 = Bot()
bot2 = Bot()
# 多开
```

```python
# 发送文本
my_friend.send('Hello, WeChat!')
# 发送图片
my_friend.send_image('my_picture.png')
# 发送视频
my_friend.send_video('my_video.mov')
# 发送文件
my_friend.send_file('my_file.zip')
```

聊天对象

Chat 基本聊天对象
puid
nick_name  昵称
name  按顺序从备注名称、群聊显示名称、昵称、微信号中选择第一个可用的
send(content=None, media_id=None)  发送消息
send_msg()  发送文本消息
send_image(path, media_id=None)  发送图片
send_file(path, media_id=None)  发送文件
send_video(path=None, media_id=None)  发送视频
mark_as_read()  标记为已读
pin()  置顶
unpin() 取消置顶
get_avatar(save_path=None)  获取头像

User 单个聊天对象
remark_name  备注名
set_remark_name(remark_name)  更改备注名
sex  性别
province  省份
city  城市
signature  签名
is_friend  是否为好友
add(verify_content='')   添加好友
accept(verify_content='')  接受好友

Friend 好友

Group 群聊
members  成员
search(keywords=None, **attributes)  搜索
owner  获取群主
is_owner  判断是否为群主
update_group(members_details=False)  更新群信息
add_members(users, use_invitation=False)  添加群成员
remove_members(members)  移除群成员
rename_group(name)  更改群名

Member 群成员
display_name  群聊显示名称
remove()  移除
name  获取名字

bot.friends().stats_text()  统计信息

消息处理
每一个从微信接收到的消息都会保存在Bot.messages中
Message基本属性
type  消息类型
text  消息文本内容
get_file(save_path=None)  获取文件
file_name  文件名
file_size  文件大小
sender  消息发送者
is_at  是否为@的消息
create_time  消息创建时间
url  分享类消息的网页url
articles  公众号推送的文章列表
location  地理位置信息
img_height  图片高度
img_width  图片宽度
play_length  视频长度
voice_length  语音长度
reply()  回复
forward(chat, prefix=None, suffix=None, raise_for_unsupported=False)  转发消息

wxpy.embed(local=None, banner='', shell=None)  保持程序监听并弹出命令行便于调试
Bot.join()  保持程序监听

wxpy.get_wecaht_logger(receiver=None, name=None, level=30)