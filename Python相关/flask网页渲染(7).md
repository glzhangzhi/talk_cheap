[TOC]

# 用户认证

目前已经实现了程序的大部分功能，但还有一个很重要的功能没有实现，即用户认真保护。页面上的编辑和删除按钮是对所有用户公开的，任何人都可以对服务器里的数据库进行编辑和删除操作，这显然是不合理的。

这一章我们会为程序添加用户认证功能，把用户分成两类，一类是管理员，可以通过用户名和密码登陆，执行数据相关的操作。另一类是访客，只能浏览页面。

但是在实现这个功能前，我们应该先学习如何安全的储存密码等敏感信息在服务器中。

# 密码储存

直接明文储存密码显然是不行的，一旦黑客通过其他端口进入到服务器中，就可以读取到这些明文储存的密码，并获取整个服务器的控制权。更加保险的方式是对每个密码进行计算，生成一个独一无二的密码hash值，此时就算黑客拿到了这个hash值，也无法逆向获取原密码。

flask内置了依赖Werkzeug，用于生成和验证密码hash值的函数。werkzeug.security.generate_password_hash()用来给指定的密码生成hash值，而werkzeug.security.check_password_hash()用来检查给定的hash值和密码是否对应。以下是使用示例，

```python
from werkzeug.security import generate_password_hash, check_password_hash
pw_hash = generate_password_hash('dog')
print(pw_hash)
print(check_password_hash(pw_hash, 'dog'))
print(check_password_hash(pw_hash, 'cat'))
print('234kljfsdf', 'dog')
```

我们现在修改User类，给每个用户增加用户名和密码属性，并添加设置密码和验证密码的方法

```
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password): 
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
```

因为我们修改了数据库结构，我们需要清空数据库并重新生成

```
flask initdb --drop
```

# 生成管理员账户

因为生成管理员的功能不需要给每个用户提供，所以不需要编写一个页面来实现，而是可以通过命令行来实现。

```
import click

@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password) 
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password) 
        db.session.add(user)

    db.session.commit()  
    click.echo('Done.')
```

这里又有一些新知识

1. hide_input可以让密码在输入时隐藏
2. confirmation_prompt会要求用户二次输入确认

# 使用Flask-Login实现用户认证

扩展Flask-Login中提供了实现用户认证需要的各种功能函数，首先安装它

```
pip install flask-login
```

这个扩展的初始化与之前使用数据库时略有不同，需要创建一个用户回调函数，它接受用户ID作为参数，返回这个ID对应的用户对象。添加这个用户回调函数的目的在于，flask-login提供了一个current_user变量，它可以记录当前登陆的用户对象是什么。另一步是让储存用户的User类继承Flask-Login提供的UserMixin类，继承这个类后，会让User类拥有几个常用的用于判断状态的属性和方法，例如is_authenticated用于判断当前用户是否登陆

```
from flask_login import LoginManager, UserMixin

login_manager = LoginManager(app)

class User(db.Model, UserMixin)
	# ...

@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象
```

# 登陆

登陆使用Flask-Login提供的login_user()函数实现，需要传入用户类对象作为参数。首先创建用于处理登陆操作的视图函数。

```
from flask_login import login_user

# ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()
        # 验证用户名和密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登入用户
            flash('Login success.')
            return redirect(url_for('index'))  # 重定向到主页

        flash('Invalid username or password.')  # 如果验证失败，显示错误消息
        return redirect(url_for('login'))  # 重定向回登录页面

    return render_template('login.html')
```

下面是登陆表单的登陆页面login.html模板

```
{% extends 'base.html' %}

{% block content %}
<h3>Login</h3>
<form method="post">
    Username<br>
    <input type="text" name="username" required><br><br>
    Password<br>
    <!-- 密码输入框的 type 属性使用 password，会将输入值显示为圆点 -->
    <input type="password" name="password" required><br><br>
    <input class="btn" type="submit" name="submit" value="Submit">
</form>
{% endblock %}
```

# 登出

和登陆类似，登出操作需要调用logout_user()函数。

```
from flask_login import login_required, logout_user

# ...

@app.route('/logout')
@login_required  # 用于视图保护，后面会详细介绍
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index'))  # 重定向回首页
```

# 认证保护

在web程序中，有些URL是只对已登陆的用户开放的，这就是认证保护。

## 视图保护

有以下操作是只对登陆用户开放的：

- 编辑
- 设置
- 注销
- 删除
- 添加

对于那些受认证保护的视图函数，只需要加上@login_required装饰器即可，当未登录用户访问受认证保护的页面时，会把用户重定向到登陆页面，并显示一个错误信息。

```
@app.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required  # 登录保护
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))
```

为了让这个重定向操作正确执行，我们还需要把login_manager.login_view设置为登陆视图函数的名字，还可以通过设置login_manager.login_message来自定义错误提示信息。

```
login_manager.login_view = 'login'
```

