如果记得之前安装时输入的密码，可以linux命令行输入

passwd

按照提示输入现在的密码和新密码即可。

如果忘记了之前设置的密码，可按如下步骤设置新密码：

1. 打开powershell，使用命令 wsl -d Ubuntu -u root

    可以将Ubuntu换成已安装的分发版

2. 接着，输入passwd <WSLUsernme>，其中<WSLUsernme>是忘记了密码的用户名

3. 系统将提示输入新的UNIX密码，然后确认密码。

