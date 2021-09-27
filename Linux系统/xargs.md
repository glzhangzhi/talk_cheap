[TOC]

# 简介

有一些命令可以接受标准输入作为参数，比如grep

cat /etc/passwd | grep root

相当于

grep root /etc/passwd

但是大多数命令都不接受标准输入作为参数，比如echo，只能接受命令行参数

echo "hello" | echo

xargs命令的作用就是将标准输入转为命令行参数

echo "hello" | xargs echo

xargs后面跟的默认命令是echo

# 常用参数

## -d 更改默认分隔符

echo -e "a\tb\tc" | xargs -d "\t" echo

## -p 打印要执行的命令，并逐一询问是否要执行

echo 'one two three' | xargs -p touch

## -t 打印要执行的命令，并直接执行

echo 'one two three' | xargs -t touch

