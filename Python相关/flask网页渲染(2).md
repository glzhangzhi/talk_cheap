[TOC]

# 模板

在一般的web程序中，访问一个地址通常会返回一个包含各种信息的HTML页面。因为我们的程序是动态的，页面中的信息需要根据不同的情况来动态进行调整，例如，对于已登录和未登录的用户显示的页面是不相同的。

我们把包含变量和逻辑晕眩的HTML文本叫做模板，执行这些变量替换和逻辑计算工作的过程称为渲染，这个工作由模板渲染引擎Jinja2来完成。

按照默认的设置，flask会从程序实例所在模块同级目录下的templates文件夹中寻找模板

# 模板基本语法

```
<h1>{{ username }}的个人主页</h1>
{% if bio %}
    <p>{{ bio }}</p>      {# 这里的缩进只是为了可读性，不是必须的 #}
{% else %}
    <p>自我介绍为空。</p>
{% endif %}               {# 大部分 Jinja 语句都需要声明关闭 #}
```

在模板中，需要添加特定的定界符将Jinja2语句和变量标记出来，以下是三种常用的定界符：

- `{{ ... }}`用于标记变量

- `{{% ... %}}`用于标记语句，例如if语句，for语句等

- `{{# ... #}}`用来写注释

# 编写主页模板

我们在模板文件夹中创建一个index.html文件，作为主页模板

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ name }}'s Watchlist</title>
</head>
<body>
    <h2>{{ name }}'s Watchlist</h2>
    <p>{{ movies|length }} Titles</p>                   {# 使用 length 过滤器获取 movies 变量的长度 #}
    <ul>
        {% for movie in movies %}                       {# 迭代 movies 变量 #}
        <li>{{ movie.title }} - {{ movie.year }}</li>   {# 等同于 movie['title'] #}
        {% endfor %}                                    {# 使用 endfor 标签结束 for 语句 #}
    </ul>
    <footer>
        <small>&copy; 2018 <a href="http://helloflask.com/tutorial">HelloFlask</a></small>
    </footer>
</body>
</html>
```

上面的主体就是HTML语法，有两个注意的点：

第一是对变量movies使用了过滤器length，它是一个Jinja2的builtin函数，类似python的len()。可以在这里查看所有Jinja2的builtin函数 https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters

第二是使用了字典的语法movie.title，其等同于movie['title']，还没有尝试是否能互换

# 为主页内容准备虚拟数据

在主程序中定义一些虚拟数据

```
name = 'CG'
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
```

# 渲染主页模板

使用flask的render_template函数来使用模板渲染web，这里模板的路径是相对于templates文件夹的位置，还需要传入在模板中使用的变量

```
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
```

