[TOC]

# 数据库

大部分的程序都不可避免的会使用数据库，而数据库管理系统也有很多成熟的框架选择，这里选择SQLite，它基于文件，不需要单独启动数据库服务器，数据库操作简单，适合在开发时使用。flask支持许多的数据库管理框架，通常改变不同的数据库管理模型只需要更改很少的代码。

# SQLAlchemy

这里使用这个python第三方库来操作SQLite数据库，而在flask中也有对应的Flask-SQLAlchemy扩展来继承该第三方库

```
pip install flask-sqlalchemy
```

大部分扩展都需要在web应用启动时进行初始化操作

```
from flask_sqlalchemy import SQLAlchemy

app = FLASK(__name__)
db = SQLAlchemy(app)
```

# 设置数据库URI

用使用数据库，不止需要对其插件进行初始化，还需要将插件链接到数据库文件上

```
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
```

一般，我们都将数据库文件放到主程序所在根目录下，而app.root_path属性内储存的是主程序所在的路径。

另外要注意，在windows系统上，前面的数据库管理系统标识符是`'sqlite:///'`。可以在主程序中加入一个运行环境检测，也更好的兼容在不同平台运行的需求。

```
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
# 关闭对模型修改的监控
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
```

# 创建数据库模型

在我们的观影名单程序中，有两种类型的数据要保存，分别是用户信息和电影条目信息，下面分别在主程序创建两个模型来表示这两张表

```
class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字

class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份
```

在创建模型类的时候有一点要注意的点：

1. 模型类要继承db.Model

2. 每一个类属性要实例化db.Column，传入的参数为字段的类型，以下是常用的字段类型

字段类型| 说明                            
---|---
db.Intege| 整型                            
db.String(max_size)|字符串，max_size为最大长度
db.Text|长文本
db.DateTime|日期时间，为python datetime对象
db.Float|浮点数
db.Boolean|布尔值

3. 在db.Column实例化的时候，可以传入额外的参数对字段进行设置，比如primary_key=True设置是否为主键，nullable设置是否允许空值，index设置是否设置索引，unique设置是否允许重复值，default设置默认值、

# 创建数据库表

创建好了模型类以后，还不能对立即对模型进行操作，因为还没有创建数据库对应的文件，需要在命令行中生成包含数据库模型类的数据库文件

```
flask shell
>>> from app import db
>>> db.create_all()
```

之后会生成对应的数据库文件。建议将此文件加入git忽略列表。

如果之后对模型类进行了改动，需要重新生成数据库文件，那么可以将数据库文件清空后重新生成。

```
>>> db.drop_all()
>>> db.create_all()
```

注意上面并不是直接运行的python命令行，而是通过`flask shell`进入命令行，通过这种方式会自动激活一些上下文关系，包含一些特殊的环境变量，之后如不特殊说明，所有的python shell均是以此方式打开。

# 使用脚本初始化数据库

```
import click

@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息
```

上面有两个新的知识点

1. 使用`@app.cli.command()`将某个函数名注册为命令行的命令，例如上面这个函数，只需要命令行运行`flask initdb`或`flask initdb --drop`
2. 这里的click是一个python库，已经被python官方收编，专注于提升python的命令行使用体验，目前这是仅有的一个适用于flask的命令行工具
3. 使用click.option()来创建一个参数解析器，其工作方式与argparse差不多

# 数据库的创建，读取，更新，删除

## 创建

```
>>> from app import User, Movie
>>> user1 = User(name='Zhang')
>>> m1 = Movie(title='Leon', year='1994')
>>> m2 = Movie(title='Mahjong', year='1996')
>>> db.session.add(user1)
>>> db.sesseion.add(m1)
>>> db.sesseion.add(m2)
>>> db.sesseion.commit()
```

## 读取

通过对模型类的query属性调用可选的过滤方法和查询方法，就可以获得对应的单个或多个记录，格式如下

`<模型类>.query.<过滤方法(可选)>.<查询方法>`

以下是常用的过滤方法

| 过滤方法    | 说明                                       |
| ----------- | ------------------------------------------ |
| filter()    | 使用指定规则过滤记录                       |
| filter_by() | 使用以关键字表达式的形式定义的规则过滤记录 |
| order_by()  | 根据指定条件对记录进行排序                 |
| group_by()  | 根据指定条件对记录进行分组                 |

以下是常用的查询方法

| 查询方法       | 说明                                                   |
| -------------- | ------------------------------------------------------ |
| all()          | 返回包含所有查询记录的列表                             |
| first()        | 查询查询到的第一条记录，如果未找到，则返回None         |
| get(id)        | 传入主键值作为参数，返回指定主键值的记录，否则返回None |
| count()        | 返回查询结果的数量                                     |
| first_or_404() | 与first()方法相同，但若未找到，返回404响应             |
| get_or_404()   | 与get()方法相同，但若未找到，返回404响应               |
| paginate()     | 返回一个Pagination对象，可以对记录进行分页处理         |

以下是一个从数据库文件中读取记录并进行简单查询的例子

```
>>> from app import Movie
>>> movie = Movie.quert.first()
>>> movie.title
‘Leon'
>>> movie.year
'1994'
>>> Movie.query.all()
[<Movie 1>, <Movie 2>]
>>> Movie.query.count()
2
>>> Movie.query.get(1)
[<Movie 1>]
>>> Movie.query.filter_by(title='Mahjong').first()
[<Movie 2>]
>>> Movie.query.filter(Movie.title='Mahjong').first()
[<Movie 2>]
```

## 更新

```
>>> movie = Movie.query.get(2)
>>> movie.title = 'WALL-E'
>>> movie.year = '2008'
>>> db.session.commit()
```

## 删除

```
>>> movie = Movie.query.get(1)
>>> db.session.delete(movie)
>>> db.session.commit
```

# 在主程序中对数据库进行操作

使用相同的语句，你可以在主程序脚本中对数据库进行相同的操作，例如在渲染主页时，使用数据库中读取出来的数据，而不是使用fake的数据

```
@app.route('/')
def index():
	user = User.query.first()
	movies = Movie.query.all()
	return render_template('index.html', user=user, movies=movies)
```

相应地，在模板文件中，也需要将直接读取user字符串变成读取user.name

与此同时，也可以写一个命令，将之前写的fake数据写入新建的数据库文件中并保存

```
import click

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Zhang'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')
```

现在执行`flask forge`就可以使用虚构的数据创建数据库