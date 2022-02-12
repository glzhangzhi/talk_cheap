在使用vscode的remote功能通过ssh连接公司电脑的时候一直出现问题，在linux下无法连接，但是使用win就可以。

在官网的指南中找到了解决办法：

第一种，尝试命令`Remote-SSH: Kill VS Code Server on Host`

第二种，在本地的json设置文件中添加

```
"remote.SSH.showLoginTerminal": true,
"remote.SSH.useLocalServer": false,
```

之后重新连接，问题就解决了。之后可以把这两行删掉。



我感觉应该是linux下我的某些remote设置导致一些东西无法在远程电脑上安装，而且这个设置还留在了默认设置里。上面这两句应该是重置了本地服务器。