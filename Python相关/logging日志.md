# 日志的定义

日志是对软件执行时所发生事件的一种追踪方式。软件开发人员对他们的代码添加日志调用，借此来指示某事件的发生。一个事件通过一些包含变量数据的描述信息来描述（比如：每个事件发生时的数据都是不同的）。开发者还会区分事件的重要性，重要性也被称为 等级 或 严重性

# 日志级别

|级别|何时使用|
|----|----|
|DEBUG|细节信息，仅当诊断问题时使用|
|INFO||
|WARNING||
|ERROR||
|CRITICAL||

默认的追踪级别是WARNING

# 简单例子

```python
import logging
# 如果不进行配置，默认打印到控制台
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
```

```python
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, filemode='w')
# 可以配置日志输出文件，编码形式，打印级别，日志文件记录方式
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

另外，可以在命令行中传入参数`--log=INFO`来控制记录等级

# 更改消息的格式

```python
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

import logging
logging.basicConfig(format='%(asctime)s %(message)s')  # 显示日期和时间
logging.warning('is when this event was logged.')

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  # 订制日期和时间的显示格式
logging.warning('is when this event was logged.')
```

# 日志记录的构成

一个日志记录行为由以下四个组件构成：

+ 记录器Logger，暴露了应用程序代码能直接使用的接口
+ 处理器Handler，将Logger产生的日志记录发送至合适的目的地
+ 过滤器Filter，提供更高的粒度控制，决定输出哪些日志记录
+ 格式化器Formatter，指定最终输出中日志记录的格式



# 创建针对不同模块的记录器

如果没有显式的创建记录器，会默认创建名为root的记录器，默认级别为WARN，输出到标准输出上，使用默认格式。

可用以下方法创建自定义记录器并进行配置

```python
logger = logging.getLogger(logger_name)
logger.setLevel(logging.ERROR)
logger.addHandler(handler_name)
logger.removeHandler(handle_name)
```

# 处理器Handler

常用的处理器有三种，streamHandler, FileHandler, NullHandler，可以通过以下方法创建处理器，配置日志级别，添加格式化器和过滤器

```python
sh = logging.StreamHandler(stream=None)
fh = logging.FileHandler(filename, mode='w', encoding=None, delay=False)

sh.setLevel(logging.WARN)
sh.setFormatter(formatter_name)
sh.addFilter(filter_name)
sh.removeFilter(filter_name)
```

# 格式化器Formatter

格式化器设置日志信息的显示规则、结构和内容

```python
fm = logging.Formatter(fmt=None, datefmt=None)
```

# 过滤器Filter

过滤器可以完成比默认级别更加精细的过滤

```python
fl = logging.Filter(name='')
```

# 配置方式

- 使用basicConfig()函数在程序中进行配置
- 使用fileConfig()函数读取配置文件
- 使用dictConfig()读取字典信息配置
- 使用listen()函数听取网络信息

# basicConfig关键字参数

|关键字|描述|
|-|-|
|filename|创建一个FileHandler，使用指定的文件名|
|filemode|指明文件的打开模式，如果没有指定文件名，默认为'a'|
|format|格式化字符串|
|datefmt|日期时间格式|
|level|显示日志的jibie|

# 常用format格式

|格式|描述|
|-|-|
|%(levelno)s|打印日志级别的数值|
|%(levelname)s|日志级别的名称|
|%(pathname)s|当前执行程序的路径|
|%(filename)s|执行程序的名字|
|%(funcName)s|当前函数|
|%(lineno)d|当前行号|
|%(asctime)s|时间|
|%(thread)d|线程ID|
|%(threadName)s|线程名称|
|%(process)d|进程ID|
|%(message)s|日志信息|

# 常用时间格式化字符串

| 格式 | 描述     |
| ---- | -------- |
| %a   | 星期缩写 |
| %b   | 月份缩写 |
| %d   | 日       |
| %H   | 24制小时 |
| %I   | 12制小时 |
| %m   | 月       |
| %M   | 分钟     |
| %p   | AM or PM |
| %S   | 秒       |
| %y   | 年后两位 |
| %Y   | 年份完整 |

# 参考程序

```python
# -*- encoding:utf-8 -*-
import logging

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create file handler
log_path = "./log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
# 先把格式化器加入处理器，再把处理器加入记录器
fh.setFormatter(formatter)
logger.addHandler(fh)

# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')```

##### 文件配置
配置文件logging.conf如下:
```[loggers]
keys=root,example01

[logger_root]
level=DEBUG
handlers=hand01,hand02

[logger_example01]
handlers=hand01,hand02
qualname=example01
propagate=0

[handlers]
keys=hand01,hand02

[handler_hand01]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stderr,)

[handler_hand02]
class=FileHandler
level=DEBUG
formatter=form01
args=('log.log', 'a')

[formatters]
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s```

使用程序logger.py如下:
```#!/usr/bin/python
# -*- encoding:utf-8 -*-
import logging
import logging.config

logging.config.fileConfig("./logging.conf")

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')```
```

