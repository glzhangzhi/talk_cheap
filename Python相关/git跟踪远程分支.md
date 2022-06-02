[TOC]



# 克隆时自动跟踪

```git
git clone git@github...A...git
# 在初次将远程仓库git@github...A...git映射到origin指针上
# 将远程仓库上的origin/master分支映射到本地的master分支上
```

# 创建分支时指定跟踪

```git
git checkout -b dev origin/develop
```

# 推送时指定跟踪

```git
git push -u origin/the_branch branch_name
```

# 手动设定某分支的上游分支

```git
git branch --set-upstream-to origin/the_branch branch_name
```

# 更改当前分支的上游分支

```git
git branch -u origin/another_branch
```

# 查看本地分支的跟踪关系

```git
git branch -vv
```

# 查看该版本库所有分支

```git
git branch  # 查看本地分支
git branch -r  # 查看远程分支
git branch -a  # 查看搜友分支
```



