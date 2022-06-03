[TOC]

# 环境配置

推荐在一个新的虚拟环境中配置flask环境
```
conda create -n flask_learning python=3.7.11
conda activate flask_learning
conda install flask
```

# 最小网页-主页

在名为app.py的文件中输入以下内容

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Welcome to My Watchlist!"
```

之后，激活对应的虚拟环境并cd到当前目录，执行以下命令

```
flask run
```

在命令行中会显示一些基本的运行信息，并给出一个网页端口号（例如http://127.0.0.1:5000）

通过浏览器打开上面这个网址或者这个网址（http://localhost:5000）即可打开我们渲染的主页，返回的字sour符串会以文本的形式显示在当前页面上。

app中的`@app.route()`是一个视图函数（view function），可以理解成请求处理函数。我们使用这个装饰器来将对某个URL的请求绑定在这个函数上。

web程序就是很多这样的视图函数的集合，对于不同的URL请求，调用不同的视图函数。

在这里的/表示根地址，即对localhost:5000/的请求，这个只需要填相对地址，不需要填写完整的地址。

整个请求过程如下：

1. 用户使用浏览器对这个URL地址发起请求http://localhost:5000
2. 服务器解析这个请求，发现请求URL匹配的规则是/，根据我们的装饰器配置，调用对应的hello()函数。
3. hello()函数返回一个值，经过处理后返回给客户端即用户的浏览器
4. 浏览器接受响应，并将其显示在窗口上

# 程序发现机制

flask默认会假设你总是将程序储存在app.py或wsgi.py文件中，如果你使用了其他文件名，例如index.py，程序会报错。如果你要使用其他文件名，可以通过设置环境变量来告诉flask你想通过哪个文件来启动

```
export FLASK_APP=index.py  # Linux
set FLASK_APP=index.py  # Windows cmd
$env:FLASK_APP = "index.py"  # Windows Powershell
```

也可以将这个环境变量值设为路径名，这样flask会自动到对应路径下寻找app.py或wsgi.py

# 开启调试模式

另一个可以通过设置环境变量来更改的选项是调试模式，在调试模式下，浏览器页面上会显示错误信息，且在代码更改后，页面会自动重载

```
export FLASK_ENV=development  # Linux
```

# 管理环境变量

为了不用每次打开新的终端都设置一次环境变量，我们可以安装一个第三方库来自动导入环境变量

```
conda install python-dotenv
touch .env .flaskenv
```

.flaskenv用来储存flask相关的公开环境变量，.env用来储存敏感数据，它不应该被提交到git仓库中，因此应该将它添加到git忽略名单中。

在.flaskenv中中添加要自动设置的环境变量

```
FLASK_APP = index.py
FLASK_ENV = development
```

# 修改视图函数返回值

响应函数返回的字符串默认会被浏览器作为HTML格式解析，因此可以给它添加HTML元素标记

```python
@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
```

# 修改URL响应规则

URL的响应规则可以自由更改，以改变URL到函数的映射关系，但要注意必须以根目录开头

```
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'
```

此时如果访问http://localhost:5000/home就会出现设定的页面，但是此时如果直接访问http://localhost:5000/，就会出现404页面，原因是并没有设定一个对于该地址的响应函数。

一个视图函数可以映射多个URL，可以通过将同一个函数绑定多个装饰器实现

```
@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'
```

# URL解析

装饰器还可以对输入的URL进行规则解析，实现能够从URL中解析出变量的功能

```
@app.route('/user/<name>')
def user_page(name):
    return 'User page'
```

这样，\<name>的部分会被解析成name变量，这个变量可以在响应函数中使用。在这样的配置下，无论是访问http://localhost:5000/user/peter，http://localhost:5000/user/eva还是http://localhost:5000/user/adam都可以看到这个用户页面。

URL解析还支持对变量进行预处理，例如`/user/<int:number>`会将number解析成整型

# 变量名转义

因为浏览器会自动解析URL中的代码，为了防止用户输入的URL中包含恶意代码，URL的响应返回并不能直接返回，需要使用flask提供的escape函数对其进行转义处理

```
from flask import escape

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)
```

# 生成URL地址

根据上面的URL解析规则，flask根据装饰器的绑定规则寻找对应的响应函数，因此响应函数的名字与URL并没有很强的相关性，只要其能够在阅读层面上能够体现其功能即可。flask提供了一个url_for函数来显示某个响应函数对应的URL地址。

```
from flask import url_for, escape

# ...

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
```

使用url_for查询hello函数，会返回/根地址，查询带参数解析的user_page会返回/user/peter等地址。如果输入的参数并不是函数所必须的，例如num之于test_url_for函数，则会作为查询字符串附加到URL后面，/test?num=2
