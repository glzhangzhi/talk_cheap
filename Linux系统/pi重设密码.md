1. pi关机，取出sd卡，用读卡器插入电脑，在boot盘里找到文件cmdline.txt, 在第一行末尾添加以下内容：
init=/bin/sh
保存后退出

2. 将sd卡插入pi，启动后会自动进入命令行模式，输入以下内容：
mount -o remount, rw /
passwd pi
以后会被提示输入两遍新密码

3. 输入以下内容执行同步：
sync
exec /sbin/init
之后会自动重启

4. 重启完毕后关机，取出sd卡插入电脑，将第一布所做的更改删除，保存退出