[TOC]

https://docs.python.org/zh-cn/3/howto/argparse.html#id1

# 创建参数解析器

```
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```

# 添加位置参数add_argument

```
parser.add_argument('echo')
args = parser.parse_args()
print(args.echo)
```

# 添加参数帮助信息help

```
parser.add_argument('echo', help='echo the string you use here')
args = parser.parse_args()
print(args.echo)
```

# 指定传入参数的类型type

默认的传入类型为字符串，如果指定了类型，会尝试在接收到参数时进行转换

```
parser.add_argument('square', help='display a sqaure of a given number', type=int)
args = parser.parse_args()
print(args.square ** 2)
```

# 添加可选参数--

如果参数名前面带了-或者--，则意味着它是可选参数，在不传入时不会引发错误。同时，在之后引用该参数名，会返回None

```
parser.add_argument('--verbosity', help='increase output verbosity')
args = parser.parse_args()
if args.verbosity:
	print('verbosity turn on')
```

# 将参数设置为开关标志action

开关标志的意思时，如果该参数有，则该变量为True，用法例如`foo.py --verbose`

```
parser.add_argument('--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()
if args.verbose:
	print('verbosity turn on')
```

# 设置参数的短选项

```
parser.add_argument('-v', '--verbose', help='increase output verbosity', 
					action='store_true')
```

# 限制参数的取值范围choices

```
parser.add_argument("-v", "--verbosity", type=int, 
					choices=[0, 1, 2], help="increase output verbosity")
```

# 允许参数多次出现count

在参数verbose中储存的是该参数出现的次数

```
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
# -v -v == -vv == --verbose --verbose
```

# 指定参数的默认值default

```
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
```

# 指定相互矛盾的一组参数add_mutually_exclusive_group

互相矛盾的一组参数中，只能出现一个

```
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
```

# 添加脚本描述信息description

```
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
```

