tmux是一个终端复用器terminal multiplexer，主要功能有以下：

tmux是一个终端复用器terminal multiplexer，主要功能有以下：

1. 让会话与终端分离，即使ssh连接断开，也不会终止会话
2. 窗口拆分

# 基础

## 安装

sudo apt-get instatll tmux

## 启动 tmux

tmux

## 退出 c-d

c-d 或者 exit

# 会话管理

## 新建会话

tmux new -s session-name

## 分离会话 c-b d

c-b d 或者 tmux detach

## 查看会话列表 c-b s

c-b s 或者 tmux ls

以下所有的session都可以用ls命令查到的窗口编号代替

## 接入会话

tmux attach -t session-name

## 杀死会话

tmux kill-session -t session-name

## 切换会话

tmux switch -t session-name

## 重命名会话 c-b $

c-b $ 或者 tmux rename-session -t 0 session-new-name

# 窗格操作

## 划分窗格 c-b " c-b %

c-b " 或者 tmux split-window
上下划分
c-b % tmux split-window -h
左右划分

## 调整窗格大小 c-b c-arrow

c-b c-arrow key

## 移动光标 c-b arrow

c-b 方向键

## 移动窗格

tmux swap-pane -U
当前窗格向上移动
tmux swap-pane -D
当前窗格向下移动

## 显示窗格编号 c-b q

c-b q

## 将当前窗格独立 c-b !

c-b !

## 关闭窗格 c-b x

c-b x

# 其他快捷键

## 查看终端历史输出 c-b [

c-b [


