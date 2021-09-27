安装
sudo apt-get install git-all

创建版本库
git config --global user.name 'UserName'
git config --global user.email 'email'
git init

查看当前库的状态
git status

加入新文件
git add test.py
git add .

提交改变
git commit -m 'comment'

连接在线版本库
git remote add arigin https://github.com/xxx/xxx.git

推送修改
git push -u origin master