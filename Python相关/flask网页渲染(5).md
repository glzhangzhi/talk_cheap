[TOC]

# 模板优化

在使用过程中，当用户向一个不存在的页面发起请求时，会返回一个404页面，但默认的404十分简陋，因此我们可以写一个针对404页面的模板命名为404.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ user.name }}'s Watchlist</title>
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css">
</head>
<body>
    <h2>
        <img alt="Avatar" class="avatar" src="{{ url_for('static', filename='images/avatar.png') }}">
        {{ user.name }}'s Watchlist
    </h2>
    <ul class="movie-list">
        <li>
            Page Not Found - 404
            <span class="float-right">
                <a href="{{ url_for('index') }}">Go Back</a>
            </span>
        </li>
    </ul>
    <footer>
        <small>&copy; 2018 <a href="http://helloflask.com/tutorial">HelloFlask</a></small>
    </footer>
</body>
</html>
```

接着使用一个装饰器在主程序中注册一个错误处理函数，当404错误发生时，这个函数会被出发，返回值会作为响应函数的主题返回给客户端

```
@app.errorhandler(404)
def page_not_found(e):
	user = User.query.first()
	return render.template('404.html', user=user), 404
```

普通的视图函数并不将状态码作为第二个参数返回，因为会默认返回200

# 模板上下文处理函数

通过观察错误页面和主页的模板文件可以发现，这两个模板文件存在这大量的重复内容，比如head标签，页首的标题，页脚信息等。这种重复不仅会增加工作量，也会导致后期更改的困难。而且，这两个模板文件都需要在响应函数中通过查询获取user的信息。

故明显有更加优雅的方式来解决这种重复。

首先，对于多个模版内都需要使用的变量，我们可以在主程序中使用`app.context_processor`装饰器注册一个模版上下文处理函数。

```
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)
```

flask会自动将这个字典对里的值作为上下文注入到每个模版环境中，可以理解成定义成公共变量，从而使每个模版都可以使用这里面的值。

有了这个注入函数后，我们就可以删除其他响应函数中获取user的语句，而且也不需要将user作为参数传入任何函数中来渲染模版。

# 使用模版继承组织模版

对于模版内容重复的问题，Jinja2提供了模版继承的功能，类似于python的父类继承，我们可以定义一个父模版，在这里称为基模版（base template）。在这个基模版中包含完整的HTML结构和导航栏，页首，页脚等通用部分。在子模版中，我们可以使用extends标签来声明继承于某个基模版。

而基模版中需要在实际的子模版中追加或重写的部分可以定义成块，通过在子模版中定义一个同样名称的块，可以实现对基模版内容的追加或重写。

# 编写基础模版

下面是放置在模版文件夹下的base.html文件

```

```

在这个基模版中我们定义了两个块，一个是head，一个是content，在实际的项目中可以定义非常多的块，以提供该父模版的灵活性。

第二，我们添加了一个meta元素来设置页面的viewport，它可以使网页根据设备的分辨率自动缩放页面，从而让移动设备也拥有更好的浏览体验。

第三，添加了一个导航栏，其对应的CSS代码如下：

```

```

# 编写子模版

以下是继承了基模版的主页模版

```

```

第一行声明了扩展自哪个模版文件，之后我们通过定义content块，来实现子类重写，可以把这个块理解成一个变量，定义完成后就放到基模版中渲染
