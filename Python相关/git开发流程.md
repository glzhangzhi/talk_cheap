############ 项目主持者

```bash
# 首先在本地新建一个项目，切换到项目文件夹
git init
# 之后到github上新建一个仓库，并记录仓库的地址git@github...A...git
git remove add origin git@github...A....git  # 将仓库的远程地址与本地仓库相连接
git push origin master  # 将本地内容推送到远程仓库上
# 至此，完成项目的建立
```

############ 合作开发者

```bash
# 首先，到github上，folk相应的项目到自己的账户中，并记录自己账户的项目地址git@github...B...git
git clone git@github...B...git  # 将自己仓库的远程项目克隆到本地
git checkout -b new_function  # 新建并切换到一个开发新功能的分支
# 在本地项目的开发分支中进行开发和测试
git add .;git commit -m 'add new function'  # 添加并提交修改
git push origin new_function  # 将本地项目推送到远程仓库对应的开发分支
# 到github上提交pull request，要求合并A的master和自己的new_function分支
```

############ 项目主持者

```bash
# 收到github上的pull request通知之后
git remove add B_new_function git@github...B...git  # 新建到开发者B的开发分支的指针
git fetch B_new_function  # 获取开发分支的所有更新
git checkout -b test  # 新建测试分支
git merge B_new_function/new_function  # 将开发者提交的新版本合并到测试分支
# 在测试分支中进行测试，在确认旧功能没有受影响且新功能开发成功后
git checkout master  # 切换到主分支
git merge test  # 合并测试分支上的内容
git branch -D test  # 删除测试分支
git push origin master  # 将更改推送到主分支
```

############ 合作开发者

```bash
# 如果合作开发者还想继续共享该项目，首先应该获取该项目的最新更新
git branch -D new_function  # 在本地删除自己的新功能开发分支
git push origin :new_function  # 在远程删除新功能开发分支
git remove add upstream git@github...A...git  # 获取项目的上游指针
git checkout master
git pull upstream master  # fetch+merge上游分支到主分支
```

