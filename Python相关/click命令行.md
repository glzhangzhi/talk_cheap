# 总览

click是一个利用很少的代码创造优雅命令行工具接口的python库

click的三个特性：
- 任意嵌套命令
- 自动生成帮助页面
- 支持在运行时延迟加载子命令

一个简单例子
```
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='the person to greet')

def hello(count, name):
'''simple program taht greets NAME for a total of COUNT times'''
	for x in range(count):
		click.echo(f'Hello {name}!')

if __name__ == '__main__':
	hello()
```

从上面这个例子可以看出，click到目前为止只是充当一个命令行参数解析器的作用

# 嵌套命令

命令可以附加到其他Group类型的命令中。这允许任意嵌套脚本。例如下面这个管理数据库的例子

```python
@click.group()
def cli():
	pass

@click.command()
def initdb():
    click.echo('initialized the database')

@click.command()
def dropdb():
    click.echo('dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
```

也可以用以下这种方式来将命令添加到组中

```
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
```

# 添加参数

使用option()和argument()装饰器来添加参数

```
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
```

