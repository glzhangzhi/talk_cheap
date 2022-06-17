# 组织代码

目前我们把所有的代码都放在一个脚本文件app.py中，随着代码量的增多，会使后来的开发和维护变得十分困难。虽然flask没有对项目结构有硬性要求，但是在代码的可读性上还要推荐使用更好的结构来管理代码。

静态模板和资源文件的位置保持不变，我们首先要整理的就是app.py中的代码。分为5个部分：

| 模块名称   | 作用 |
| ---------- | ---- |
| \_\_init\_\_.py | 包构造文件，创建程序实例 |
| views.py | 视图函数 |
| errors.py | 错误处理函数 |
| models.py | 模型类 |
| commands.py | 命令函数 |

将程序初始化的代码放到init中，例如

```
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ...

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
# 注意更新这里的路径，把 app.root_path 添加到 os.path.dirname() 中
# 以便把文件定位到项目根目录
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'

@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)

from watchlist import views, errors, commands
```

为了让视图函数、错误处理函数和命令函数注册到程序实例上，我们需要导入这几个模块，但是这几个模块也需要导入init文件中的程序实例，为了避免循环依赖，我们把导入的语句放到构造文件的结尾。

其他文件也是按照相同的逻辑放置到对应的文件中，要注意要从正确的文件中导入需要用到的模块和变量。

# 组织模板

同样的道理，我们可以将所有处理错误的静态模板都移动到static下errors文件夹内，但要记得更改对应的视图函数中的引用地址。

# 组织单元测试

我们也可以将测试文件拆分成多个模块，创建一个tests包来储存这些模块。
