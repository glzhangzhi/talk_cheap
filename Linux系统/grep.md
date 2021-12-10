[TOC]

# grep

## 什么是grep

linux中的grep全称是Global Regular Expression Print，是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来（对应命令红标红的部分）。

其工作原理是从文件或者Pipe中读取文本，使用定义的字符串模板进行搜索，将搜索到的匹配结果默认传递到标准输出。

## 使用grep

### 命令格式

```bash
grep [option] pattern file
```

### option参数

|参数命令|含义|
|-|-|
|模式选择与解释||
|-E --extended-regexp|扩展正则表达式（ERE）|
|-F --fixed-string|字符串|
|-G --basic-regexp|基本正则表达式（BRE）|
|-P --perl-regexp|Perl正则表达式|
|-e --regexp=<模式>|使用指定模式来进行匹配|
|-f --file=<文件>|从指定文件中取得模式|
|**-i --ignore-case  --no-ignore-case**|**忽略/（默认）不忽略大小写**|
|**-w --word-regexp**|**强制完全匹配单词**|
|-x --line-regexp|强制完全匹配整行|
|-z --num-data|数据行以一个0字节结束，而非换行符|
|其他||
|-s --no-messages|不现实错误信息|
|**-v --invert-math**|**选中不匹配的行**|
|-V --version|显示版本信息|
|--help|显示帮助信息|
|输出控制||
|**-m --max-count=<次数>**|**得到给定次数的匹配后停止**|
|-b --byte-offset|输出的同时打印字节漂移|
|**-n --line-number**|**输出的同时打印行号**|
|--line-buffered|每行输出后刷新输出缓冲区|
|-H --with-filename|为输出行打印文件名|
|-h  --no-filename|输出时不现实文件名前缀|
|--label=<标签>|将给定标签作为标准输出文件名前缀|
|-o  --only-matching|只显示行中非空匹配部分|
|**-q --quiet, --silent**|**不显示所有常规输出**|
|--binary-file=TYPE|TYPE=binary, text, without-match  设定二进制文件的类型|
|-a --text|等同于上面的TYPE=text|
|-I|等同于上面的TYPE=without-match|
|-d --directories=ACTION|ACTION=read, recurse, skip  目录的读取方式|
|-D --devices=ACTION|ACTION=read, skip  设备的读取方式|
|-r --recursive|等同于 -d --directories=recurse|
|-R --dereference-recursive|同上，但遍历所有符号链接|
|--include=GLOB|只查找匹配GLOB文件模式的文件|
|--exclude=GLOB|跳过匹配GLOB的文件|
|--exclude-from=FILE|跳过所有匹配给定文件内容中人任意模式的文件|
|--exclude-dir=GLOB|跳过所有匹配GLOB的目录|
|-L --files-without-match|只打印没有匹配上的文件的名称|
|-l  --files-with-matches|只打印有匹配的文件的名称|
|**-c --count**|**只打印每个文件中匹配行的数目**|
|-T --initial-tab|行首制表符对齐|
|-Z --null|在文件名最后打印空字符|
|文件控制||
|**-B  --before-context=NUM**|**打印文本及其前面NUM行**|
|**-A  --after-context=NUM**|**打印文本以及后面NUM行**|
|**-C  --context=NUM**|**打印NUM行输出文本**|
|-NUM|等同于 -C NUM|
|--color[=WHEN]  --colour[=WHEN]|WHEN=always, never, auto  使用标记高亮匹配字符串|
|-U --binary|不要清除行为的CR字符|
