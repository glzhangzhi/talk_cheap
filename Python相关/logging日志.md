[TOC]

这里找到一个关于写日志的自带库[logging](https://docs.python.org/2/library/logging.html)

```python
import logging
```

# 基础用法
```python
logging.DEBUG('1')
logging.INFO('2')
logging.WARNING('3')
logging.ERROR('4')
logging.CRITICAL('5')
```
默认的提示等级是warning，所以只有3 4 5能显示出来

# 更改默认提示等级和日志文件名
```python
logging.basicConfig(filename='example.log',level=logging.ERROR)
logging.DEBUG('1')
logging.INFO('2')
logging.WARNING('3')
logging.ERROR('4')
logging.CRITICAL('5')
```
这里是产生日志文件，设置提示等级是ERRER，所以只有4 5能被记录到日志里

# 显示日志时间
```python
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
```

# 设置具体时间格式
```python
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
logging.warning('is when this event was logged.')
```