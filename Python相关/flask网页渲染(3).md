[TOC]

# 静态文件

与模板的概念相反，静态文件(static files)只内容不需要动态生成的文件，例如图片，css文件，js脚本等

在flask中，我们需要创建一个static文件夹来保存静态文件，它应位于主程序和templates文件夹同一级目录下

# 生成静态文件URL

在HTML文件中，使用这些静态文件需要给出文件所在的URL。为了更加灵活，这些文件的URL可以通过flask提供的url_for函数来生成。

之前我们使用这个函数来生成视图函数对应的URL，这里要使用它来生成静态文件的URL的话，应传入断点端点值static，并使用filename参数来指定文件相对于static文件夹的位置

例如可以在模板文件中使用以下语句来引用静态资源中的图片

```
<img src="{{ url_for('static', filename='foo.jpg') }}">
```

这里要注意的是，如果要在主程序python脚本中使用url_for函数，需要import，但是flask把一些常用函数和对象添加到了模板的上下文中，所以在模板中使用url_for不需要import

# 添加Favicon

Favicon（favourite icon）是显示在标签页和书签栏的网页头像，一般的格式为ICO，PNG或GIF的图片，大小为16x16，32x32或64x64像素，将它放到static目录中，并在模板文件中引用

```
<head>
    ...
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
</head>
```

# 在网页中添加图片

我们将我们想使用的图片资源也放在static中，为了方便管理，可以新建一个子文件夹images

```
<h2>
    <img alt="Avatar" src="{{ url_for('static', filename='images/avatar.png') }}">
    {{ name }}'s Watchlist
</h2>
...
<img alt="Walking Totoro" src="{{ url_for('static', filename='images/totoro.gif') }}">
```

# 在网页中添加CSS

同样，可以给网页添加一些格式样式，同样将其放在static文件夹中，命名为style.css

```
/* 页面整体 */
body {
    margin: auto;
    max-width: 580px;
    font-size: 14px;
    font-family: Helvetica, Arial, sans-serif;
}

/* 页脚 */
footer {
    color: #888;
    margin-top: 15px;
    text-align: center;
    padding: 10px;
}

/* 头像 */
.avatar {
    width: 40px;
}

/* 电影列表 */
.movie-list {
    list-style-type: none;
    padding: 0;
    margin-bottom: 10px;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}

.movie-list li {
    padding: 12px 24px;
    border-bottom: 1px solid #ddd;
}

.movie-list li:last-child {
    border-bottom:none;
}

.movie-list li:hover {
    background-color: #f8f9fa;
}

/* 龙猫图片 */
.totoro {
    display: block;
    margin: 0 auto;
    height: 100px;
}
```

并在模板文件中引用css文件

```
<head>
    ...
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css">
</head>
```

接下来对模板中的每个元素设置class，以便其根据其标签应用不同的css格式

```
<h2>
    <img alt="Avatar" class="avatar" src="{{ url_for('static', filename='images/avatar.png') }}">
    {{ name }}'s Watchlist
</h2>
...
<ul class="movie-list">
    ...
</ul>
<img alt="Walking Totoro" class="totoro" src="{{ url_for('static', filename='images/totoro.gif') }}">
```

有很多成熟的框架可以用来设计css页面样式，比如Bootstrap, Semantic-UI, Foundation等，同时，也可以使用Bootstrap-Flask扩展来简化在flask里使用Bootstrap的步骤