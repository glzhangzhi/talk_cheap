

[TOC]



# special matching rules

[ ]     单个包含的字符

.       任意单个字符

[^]    单个不包含的字符

^      字符位于行开头

\\<    字符位于单词开头

<      字符位于行结尾

$      字符位于单词结尾



# other special matching

[[:alnum:]]  大小写字母和数字

\w 大小写字母和数字和下划线

[[:alpha:]]  大小写字母

[[:space:]]  空格

[[:digit:]]  数字

[[:lower:]] 小写字母

[[:upper:]] 大写字母

[[:xdigit:]]  十六进制字符（0-9 A-F a-f）

# quantification

\?          零次或一次

\*      零次或更多

\\+          一次或更多

\\{m,n\\} m到n次

\\{m,\\}   m次或更多

\\{,n\\}    n次或更少

\\{m\\}   m次



# grouping and boolean

\\| gray\\|grey can match gray or grey

\\(\\) gray\\|grey and gr\\(a\\|e\\)y are equivalent

\\n match what the nth subexpression grouped, where n is a digit from 1 to 9  匹配上次组匹配分组的第一个子表达式



# grep

grep [OPTIONS] PATTERN [FILE...]

-v  vary 选择非匹配行

-l   list 只打印包含匹配项的文件名

-n  带行号输出

-i  忽略大小写

-r  递归的查找子文件夹

-c  输出每个文件中匹配出现的次数



# find

find [FLAG] PATH [EXPRESSION]

## tests

\-name pattern  匹配文件名

\-regex pattern 匹配正则表达式

\-type f/d  指定类型（文件或目录）

\-path pattern  指定路径

find -regex '.*\\.txt'                路径结尾是.txt

find  -regex '.\*/tmp/.*\\.txt'  路径结尾是.txt且中间包含tmp

find –regex ‘\\./tmp/.*\\.txt’    路径结尾是.txt且开头tmp

## actions

-delete  删除

-exec  执行命令，以 \\; 作为结束标志，用 {} 来指代当前文件名

-ls  给出列表

-print  打印（默认）

-prune 不进入子目录

## logical operation

\\( \\) 表达式分组

\\!  NOT

-a AND

-o OR

,  并列，两边都会执行
