[TOC]

# 表单

在web页面中，我们需要编写一些表单来获取用户输入。一个典型的例子如下

```
<form method="post">  <!-- 指定提交方法为 POST -->
    <label for="name">名字</label>
    <input type="text" name="name" id="name"><br>  <!-- 文本输入框 -->
    <label for="occupation">职业</label>
    <input type="text" name="occupation" id="occupation"><br>  <!-- 文本输入框 -->
    <input type="submit" name="submit" value="登录">  <!-- 提交按钮 -->
</form>
```

在编写表单的时候有以下需要注意的地方：

1. 在`<form>`标签李使用method属性将提交表单数据的HTTP请求方法指定为POST。如果不指定，会默认使用GET方法，这会将表单数据通过URL提交，容易导致数据泄漏，而且也不适用于包含大量数据的情况。
2. `<input>`元素必须要指定name属性，否则无法提交数据，在服务器端，我们也需要通过这个name属性值来获取对应字段的数据。
3. 填写输入框标签文字的`<label>`元素不是必须的，只是为了辅助鼠标用户。当使用鼠标点击标签文字时，会自动激活对应的输入框，这对于复选框比较有用。for属性填入要绑定的`<input>`元素的id属性值。

# 创建新的电影条目

创建电影条目这件事我们可以放到一个新的页面，也可以放在主页中进行。这次我们使用后者。在主页模板中添加一个表单。

```
<p>{{ movies|length }} Titles</p>
<form method="post">
    Name <input type="text" name="title" autocomplete="off" required>
    Year <input type="text" name="year" autocomplete="off" required>
    <input class="btn" type="submit" name="submit" value="Add">
</form>
```

将文本输入框的autocomplete属性设为off，可以在输入时不弹出输入历史。另外设置了required的话，如果该项没有被填写，则无法提交。

两个输入框和提交按钮的CSS定义如下

```
/* 覆盖某些浏览器对 input 元素定义的字体 */
input[type=submit] {
    font-family: inherit;
}

input[type=text] {
    border: 1px solid #ddd;
}

input[name=year] {
    width: 50px;
}

.btn {
    font-size: 12px;
    padding: 3px 5px;
    text-decoration: none;
    cursor: pointer;
    background-color: white;
    color: black;
    border: 1px solid #555555;
    border-radius: 5px;
}

.btn:hover {
    text-decoration: none;
    background-color: black;
    color: white;
    border: 1px solid black;
}
```

# 接收并处理表单数据

默认情况下，当表单中的提交按钮被按下，浏览器会创建一个新的请求，默认发往当前URL。（在`<form>`元素中使用action属性可以自定义目标URL）

因为我们在模板里为表单定义了POST方法，当你输入数据并按下提交按钮，一个携带输入信息的POST请求会发往根地址。接着你会收到一个405错误，这是因为处理根地质请求的index视图函数默认只接收GET请求。

```
@app.route('/', methods=['GET', 'POST'])
```

因为同一个函数处理不同的请求，GET是返回渲染后的页面，POST是读取并保存数据，因此需要在视图函数中对当前处理的请求使用request.method值进行判断。（其实我觉得还是分成两个视图函数来写比较好，不知道能不能分别编写对于同一个URL不同请求方法的视图函数）

```
from flask import request, url_for, redirect, flash

# ...

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
        # 保存表单数据到数据库
        movie = Movie(title=title, year=year)  # 创建记录
        db.session.add(movie)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index'))  # 重定向回主页

    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
```

# 请求对象

因为我们现在需要对请求的内容进行处理，而Flask会把请求触发后的请求信息放到request对象里，因此需要导入它。

因为这个对象只有在请求发生后才包含有内容，因此只能在视图函数内使用它。它包含请求相关的所有信息，比如请求的路径request.path，请求的方法request.method，表单数据request.form，查询字符串request.args等等

其中request.form是一个特殊的字典，你可以通过相应字段来获取用户输入的对应数据，这个对应在模板中的name="xxx"

# flash消息

一般在用户执行某些动作后，通常我们会在页面上显示一个提示消息。最简单的实现就是在视图函数里定义一个包含消息内容的变量，传入模板，然后在模板里渲染显示它。因为这个需求很常用，flask内置了相关的函数。其中flash()函数用来在视图函数里向模板传递提示消息，get_flashed_messages()函数则用来在模板中获取提示的消息。

需要在使用flash前导入它，然后在视图函数里调用时直接传入要显示的消息

```
flash('Item Created')
```

flash函数在内部会把消息储存到flask提供的session对象里。session用来在请求之间储存数据，它会把数据签名后储存在浏览器的cookie中，所以我们需要设置签名所需的密钥

```
app.config['SECRET_KEY'] = 'dev'  # 等同于app.secret_key = 'dev'
```

要注意的是，这个密钥的值在开发时可以随便设置，但是在部署时应该设为一个随机的字符串，且不应该写在明文代码里。

下面在base.html模板文件中获取从视图函数中传来的提示信息并显示

```
<!-- 插入到页面标题上方 -->
{% for message in get_flashed_messages() %}
    <div class="alert">{{ message }}</div>
{% endfor %}
<h2>...</h2>
```

并为alert类添加CSS样式

```
.alert {
    position: relative;
    padding: 7px;
    margin: 7px 0;
    border: 1px solid transparent;
    color: #004085;
    background-color: #cce5ff;
    border-color: #b8daff;
    border-radius: 5px;
}
```

此外还可以注意到，我们除了在模板中添加required以外，还在主程序中使用了一些判断语句来对输入数据进行进一步验证。

# 重定向响应

重定向响应是一类特殊的响应，它会返回一个新的URL，浏览器在接收到这样的响应后会向这个新的URL再次发起一个新的请求。flask提供了redirect函数来快捷生成这种响应，传入重定向的目标URL作为参数。我们在这里的处理是根据验证情况，发送不同的消息，之后都将页面重定向到主页。

# 编辑条目

与创建电影条目类似，我们先创建一个用于显示编辑的页面和处理编辑表单提交请求的视图函数

```
@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))  # 重定向回对应的编辑页面

        movie.title = title  # 更新标题
        movie.year = year  # 更新年份
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页

    return render_template('edit.html', movie=movie)  # 传入被编辑的电影记录
```

这个视图函数的URL应用了一些规则，用于将对应页面的id转换成数字，方便后续的条目查找。同样，当我们生成这个视图的URL时，也要在对应的部分传入数字，比如`url_for('edit', movie_id=2)`

之后建立编辑电影条目的页面

```
{% extends 'base.html' %}

{% block content %}
<h3>Edit item</h3>
<form method="post">
    Name <input type="text" name="title" autocomplete="off" required value="{{ movie.title }}">
    Year <input type="text" name="year" autocomplete="off" required value="{{ movie.year }}">
    <input class="btn" type="submit" name="submit" value="Update">
</form>
{% endblock %}
```

最后在主页的模板中，在每个条目后都添加一个编辑按钮，指向对应的编辑页面。这里注意要生成正确的URL

```
<span class="float-right">
    <a class="btn" href="{{ url_for('edit', movie_id=movie.id) }}">Edit</a>
    ...
</span>
```

# 删除条目

删除动作并不涉及数据的传递，因此在处理上会更加简单。首先建立一个视图函数来处理删除操作。

```
@app.route('/movie/delete/<int:movie_id>', methods=['POST'])  # 限定只接受 POST 请求
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)  # 获取电影记录
    db.session.delete(movie)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index'))  # 重定向回主页
```

一般出于安全考虑，我们会使用表单创建一个POST请求来进行删除操作，而不是直接使用一个链接指向删除操作，这样可以防止用户使用URL来指定删除内容，而且可以在删除前对操作进行进一步的确认。下面是在主页模板中删除的对应表单代码。

```
<span class="float-right">
    ...
    <form class="inline-form" method="post" action="{{ url_for('delete', movie_id=movie.id) }}">
        <input class="btn" type="submit" name="delete" value="Delete" onclick="return confirm('Are you sure?')">
    </form>
    ...
</span>
```

为了让表单中的删除按钮和旁边的其他按钮排成一行，我们为表单的CSS添加以下定义

```
.inline-form {
    display: inline;
}
```

# 其他

首先我们可以看到，自己验证表单数据十分麻烦且不可靠，对于复杂的程序，我们一般会使用集成了WTForms的扩展Flask-WTF来简化表单处理。通过编写表单类，定义表单字段和验证器，它可以自动生成表单对应的HTML代码，并在表单提交时验证数据，返回对应的错误信息。更重要的是，它还提供了CSRF（跨站请求伪造）保护功能。

CSRF是一种常见的攻击手段。以我们的删除表单为例，某恶意网站的页面中内嵌了一段代码，当用户访问时会自动发送一个删除某个电影条目的POST请求到我们的程序，而我们的程序无法分辨请求发送来自哪里，只知道来自于浏览器，因此将其理解为正常的删除请求，从而导致服务器中的数据被删除。而解决办法是在表单里添加一个包含随即字符串的隐藏字段，同时在cookie中也创建一个同样的字段，在提交删除请求时，对比两个字符串的值是否一致，以此判断是否为用户自己发送的删除请求。