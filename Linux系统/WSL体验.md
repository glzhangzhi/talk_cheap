# 在Windows中访问Linux的文件

在文件浏览器地址栏中输入\\\wsl$，可打开Linux文件位置，建议做个磁盘映射

# 在Linux中访问Windows文件

使用路径 //mnt/c 进入c盘，其他盘符同理



# 完全删除发行版

有时候在删除对应的发行版以后再安装，会提示“删除程序包先前已有的应用程序数据时出错”，这是由于之前的发行版并没有完全注销导致的。

在终端输入`wslconfig /list`，如果下面有显示发行版，就意味着仍有没注销的，通过`wslconfig /u Ubuntu-22.04`这样格式的命令来注销每一个发行版，直到运行`wslconfig /list`后显示没有安装任何发行版为止。



# 更改root密码

如果记得之前安装时输入的密码，可以linux命令行输入

passwd

按照提示输入现在的密码和新密码即可。

如果忘记了之前设置的密码，可按如下步骤设置新密码：

1. 打开powershell，使用命令 wsl -d Ubuntu -u root 可以将Ubuntu换成已安装的分发版

2. 接着，输入passwd <WSLUsernme>，其中<WSLUsernme>是忘记了密码的用户名

3. 系统将提示输入新的UNIX密码，然后确认密码。
