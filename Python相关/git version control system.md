[TOC]

# 背景知识

## 安装
sudo apt-get install git
WIndows系统可进入[官网](http://git-scm.com/download/win)下载

## Git与其他版本管理系统的本质区别

其他的版本管理系统是将文件的差异信息保存下来，储存每个版本与初始版本文件的差异。而Git是在每一次整个项目文件发生改变时，保存一次整个项目文件的快照。

## Git中的校验
Git中所有数据在储存前都用SHA-1计算校验和，以此来引用和索引。

## 使用前配置

Git有三个级别的的配置信息，存放在不同的地方。
`/etc/gitconfig`  包含系统上每一个用户及其仓库的通用配置，使用--system读写
`~/.gitconfig或~/.config/git/config`  只针对当前用户的配置，使用--global读写
`./.git/config`  当前仓库的配置，只针对当前仓库

## 配置用户名称和邮件地址
`git config --global user.name "glzhangzhi"`
`git config --global user.email "glzhangzhi@outlook.com"`

如果想针对不同项目，使用不用的用户名和密码，可以在那个项目目录下运行不带--global选项的命令来配置

## 查看配置文件
`git config --list`

# 初始化仓库

## 克隆现有的远程仓库
`git clone git@github.com:glzhangzhi/talk_cheap.git`
这个操作会在当前文件夹下载该项目的所有文件以及其所有版本，也可以使用下面的指令在指定名称的文件夹中克隆仓库
`git clone git@github.com:glzhangzhi/talk_cheap.git My_own_name`

## 在现有目录中初始化仓库
```
git init
git add some_file.py
git commit -m 'initial project version
```

可使用以下指令查看当前仓库的状态
`git status`
或简短版本
`git status -s`
??  新添加未跟踪
A     已跟踪
M_  已修改已暂存
_M  已修改未暂存

# 提交相关

## 添加新内容到下一次提交中

`git add mytext.txt`
如果该命令之后根目录名，则递归的跟踪该目录下所有文件和文件夹
`git add .`

## 忽略文件

可在.gitignore文件中列出要忽略的文件模式，其基本格式规范如下
- 所有空行或者以#开头的行都会被Git忽略
- 可以使用标准的glob模式匹配
- 匹配模式可以以/开头，指定当前目录下的文件，不进行递归
- 可以以/结尾，指定某个目录下的所有文件
- 可以在模式前加上！取反 

所谓glob模式是shell所使用的简化的正则表达式，规则如下：
- \* 匹配零个或多个字符
- [abc] 匹配任何一个列在方括号中的字符
- ？ 只匹配一个任意字符
- [3-9] 匹配3-9任意一个数字
- a/**/z 匹配任意中间目录 

[这个网址](https://github.com/github/gitignore)下有github提供的关于几十种项目和编程语言的ignore规范

## 查看已暂存和未暂存的修改

`git diff`显示未暂存的修改
`git diff --cached`显示已暂存的修改

## 提交更新

`git commit -m "some comment for this commit"`

这样先add后commit的方式虽然可以让你精心安排每一次提交的内容，但是对于一些简单的修改，这样显得太过繁琐，可以使用以下指令，跳过add步骤，直接commit所有modified的内容。
`git commit -a -m "this is a commit without add"`

## 移除文件

一共有以下几种删除情况：
- 同时删除版本库和本地的文件
	`git rm script_file.py`
- 删除了本地的文件
	此时需要commit一次，把本地的修改同步到仓库
- 修改了该文件，已add，但之后又删除了
	这样做会触发Git的安全特性，需要用强制删除选项-f
- 删除版本库的文件，但在本地保留该文件
	`git rm --cache mytext.txt`

## 文件重命名

`git mv file_from file_to`

## 查看提交历史

`git log`

使用-p选项查看每次提交的内容差异，用-2来仅显示最近2次提交
`git log -p -2`

使用--stat查看每次提交的统计信息
`git log --stat`

使用其他格式显示提交历史，可用的选项有oneline, short, full, fuller
`git log --pretty=oneline`

使用format定制输出格式，使用`git log --pretty=format`查看
`git log --pretty=format:"%h - %an, %ar : %s"`

使用--graph以类图形方式显示分支和合并历史
`git log --pretty=online --graph 或 git log --pretty=format:"%h %s" --graph`

## 重新提交

当提交一次以后，发现有些文件忘记提交了，或者提交信息写错了，可以使用--amend选项重新提交
`git commit --amend`
这样做会覆盖上一次提交的信息

## 取消暂存的文件

当将错误的文件提交到了暂存区里，使用reset指令可以取消暂存
`git reset HEAD some_file.py`

## 回退到之前的某次commit

git reset --hard commit_id

## 撤销对文件的修改

`git checkout -- somefile.py`

# 远程仓库相关

## 查看远程仓库

`git remote -v`

## 添加远程仓库

`git remote add short_name http://sdf/sdf/sdkfj.git`
之后可以通过short_name代替后面的url

## 抓取与拉取

`git fetch [remote-name]`
以上指令会访问远程仓库，从中拉取所有还没有的数据，执行完成后，会在本地拥有该远程仓库所有分支的引用，可以随时合并和查看。

在使用clone命令后，会自动为其添加远程仓库并默认以origin为简写，所以执行`git fetch origin`会抓取克隆后（或上一次抓取后）新推送的所有工作。注意它只会更新本地仓库的git信息，不会自动合并或修改当前工作区，需要手动合并。

如果已设置一个分支追踪一个远程分支，可以使用`git pull`命令来自动抓取和合并远程分支到当前分支。默认情况下，`git clone`命令会自动设置本地master分支跟踪克隆远程仓库的master分支。

## 推送到远程仓库

`git push [remote-name] [branch-name]`

通常，clone时会自动设置后origin对应的远程仓库和master对应的分支名称，因此，运行以下命令就可以备份到服务器

`git push origin master`
`git push orogin other_branch`

只有当你拥有克隆服务器的写入权限，且当前分支没有更新的推送时，这个push才有效。

## 查看远程仓库

可以使用`git remote show origin`查看更多远程仓库的信息，比如远程仓库的URL，本地分支，远程跟踪的分支。

## 远程仓库的移除和重命名

将gs重命名为newgs
`git remote rename gs newgs`

将newgs分支移除
`git remote rm newgs`

# 暂存工作区上的修改

`git stash`
这个可以用于我正在某个分支A工作，突然要切换到另一个分支B，但是又不想舍弃或者提交我在分支A上的工作，可以使用stach功能来暂时保存当前工作，保持分支A的干净，安全切换到分支B。

之后，使用`git stach list`查看暂存区里的工作，使用`git stach pop`恢复之前的工作。

# 分支管理

`git branch new_branch`
创建新分支

`git branch -a` 
查看现有分支

`git checkout new_branch`
切换分支

`git checkout -b new_branch_2`
创建并切换分支

`git branch -D new_branch_2`
删除分支

`git branch -m old_branch_name new_branch_new`
重命名分支

`git merge origin/new_branch`
合并分支

# Detail in branch merge and conflict handle
```bash
git merge -ff dev
# fast-forward merge
# if there is no commit in current branch comparing with dev branch

git merge -no-ff
# no fast forward merge
# if there are some commit in current branch and dev branch
```
```bash
git merge dev
# if there is some conflicts in this merge
vi file_with_conflict.py  # need to delete the conflict part manuelly
git add file_with_conflict.py
git commit -m 'merge...'  # commit this merge result manuelly
```

# development with multi-person

Project-Founder A

```bash
vim README
git add .
git commit
#################
edit
edit
git commit
#################
git remote add origin git@..A..git
git push origin master
```

Project-Contributor B

```bash
fork to get own repo git@..B..git
git clone git@..B..git
#################
git checkout -b add_logo
edit
edit
git commit
#################
git push origin add_logo
```

B requests a Pull Request to A

after A get the Pull Request from B

```bash
git remote add someB git@..B..git
git fetch someB
#################
git checkout -b test_someB
git merge someB/add_logo
#################
test
test
#################
git checkout master
git merge test_someB
git branch -D test_someB
git push origin master
```

after B receice the notification about closing the PR by A

```bash
git branch -D add_logo
git push origin :add_logo
git remote add upstream git@..A..git
git checkout master
git pull upstream master
```

