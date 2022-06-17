# 部署上线

我们使用云平台PythonAnywhere来部署这个web程序

# 部署前的准备

首先我们生成一个运行的依赖列表，方便直接在部署环境里安装。使用下面的命令到处目前的依赖列表。

```
pip freeze > requirements.txt
```

其次，我们在程序中使用的一些配置变量值最好从环境变量中读取，这样我们能够通过直接配置环境变量来更改程序的运行。

```
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
```

os.getenv的用法为从环境变量SECRET_KEY中读取值，如果这个环境变量不存在，则使用dev这个值。同样，对于密钥这种敏感信息，保存在环境变量中要比直接hardcode在代码中要好很多。

同时我们之前写入.env中的环境变量并不能通过服务器中的部署环境自动读取，因此我们需要写一个wsgi.py脚本来加载这些环境变量

```
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
	load_dotenv(dotenv_path)

from watchlist import app
```

接着配置一些生产环境使用的环境变量

```
$ python3
>>> import uuid
>>> uuid.uuid4().hex
'749387582901abaa092890859'
>>> exit()
$ vi .env
SECRET_KEY=749387582901abaa092890859
DATABASE_FILE=data-prod.db
```

最后安装依赖并执行初始化命令

```
$ pip install -r requirements.txt
$ flask initdb
$ flask admin
```

同时需要在PythonAnywhere上配置相关项目文件的路径。将Source code和Working directory都设置为项目所在路径，WSGI configuration file的内容编辑为如下

```
import sys

path = '/home/greyli/watchlist'  # 路径规则为 /home/你的用户名/项目文件夹名
if path not in sys.path:
    sys.path.append(path)

from wsgi import app as application
```

# 配置虚拟环境地址

如果要在项目中使用虚拟环境，还需要额外配置虚拟环境的地址，就是对应的.venv或者env地址

# 配置静态文件

可以在web配置静态文件的位置