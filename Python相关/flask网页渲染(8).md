# 测试

目前我们每次给程序添加新功能，都要在浏览器中访问程序进行测试。除了测试新功能，还要保证以前的功能也能正常运作。在大型的程序中，这会产生大量的工作量，而且手工测试的可靠性也不能保证，因此，自动化测试变得非常重要。

在实际的项目开发中，我们应该在编写完每一个功能后立即编写对应的测试，在保证测试通过的情况下再开发下一个功能。

# 单元测试

单元测试指对程序中的函数或类等独立的单元编写测试，它是自动化测试最主要的形式，我们在这里使用python中自带的unittest框架来编写单元测试。（这里留个疑问，能否使用pytest进行测试？如果要使用，需要进行那些改动？）首先我们从一个简单的例子来了解单元测试的基本概念。例如我们编写了以下这个函数，并保存到了hello.py文件中。

```
def sayhello(to=None):
    if to:
        return 'Hello, %s!' % to
    return 'Hello!'
```

接下来我们为这个函数编写对应的单元测试代码，并保存到另一个文件test_sayhello.py中。

```
import unittest

from hello import sayhello


class SayHelloTestCase(unittest.TestCase):  # 测试用例

    def setUp(self):  # 测试固件
        pass

    def tearDown(self):  # 测试固件
        pass

    def test_sayhello(self):  # 第 1 个测试
        rv = sayhello()
        self.assertEqual(rv, 'Hello!')

    def test_sayhello_to_somebody(self):  # 第 2 个测试
        rv = sayhello(to='Grey')
        self.assertEqual(rv, 'Hello, Grey!')


if __name__ == '__main__':
    unittest.main()
```

关于这个测试代码，有以下几点说明：

- 测试用例要继承unittest.TestCase类，只有这样在其中创建的以test_开头的方法才会被视为测试方法
- setUp和tearDown是测试固件方法，用以执行一些特殊操作。setUp方法会在每个测试方法执行前被调用，而tearDown方法会在每个测试方法执行后被调用。
- 每一个测试方法对应一个要测试的函数/功能/使用场景。即一个测试文件代表对于一个函数的所有测试，而一个测试函数代表对于该函数的某一个使用情况进行测试。
- 一般，测试的目的是使用断言assert来判断在该使用情况下，程序的功能是否正常执行。

常用的断言方法如下：

- assertEqual(a, b)
- assertNotEqual(a, b)
- assertTrue(x)
- assertFalse(x)
- assertIs(a, b)
- assertisNot(a, b)
- assertisNone(x)
- assertisNotNone(x)
- assertIn(a, b)
- assertNotIn(a, b)

之后通过执行python test_sayhello.py即可执行所有测试，并输出测试的结果，通过情况，总耗时等信息。

# 测试flask程序

首先我们编写一个对于固件的测试脚本test_watchlist.py

```
import unittest

from app import app, db, Movie, User


class WatchlistTestCase(unittest.TestCase):

    def setUp(self):
        # 更新配置
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        # 创建数据库和表
        db.create_all()
        # 创建测试数据，一个用户，一个电影条目
        user = User(name='Test', username='test')
        user.set_password('123')
        movie = Movie(title='Test Movie Title', year='2019')
        # 使用 add_all() 方法一次添加多个模型类实例，传入列表
        db.session.add_all([user, movie])
        db.session.commit()

        self.client = app.test_client()  # 创建测试客户端
        self.runner = app.test_cli_runner()  # 创建测试命令运行器

    def tearDown(self):
        db.session.remove()  # 清除数据库会话
        db.drop_all()  # 删除数据库表

    # 测试程序实例是否存在
    def test_app_exist(self):
        self.assertIsNotNone(app)

    # 测试程序是否处于测试模式
    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])
```

在进行测试的时候，我们一般不希望测试中产生的数据与开发数据相互干扰。

在初始化阶段，首先我们将web程序中的TESTING项更新为True，这样可以减少在出错时的多余信息。第二，我们将数据库的根地址设置到内存中，与开发用数据库隔离。当然你也可以使用位于其他地址或名称的数据库，但内存中的数据库读写速度更快。第三，我们调用create_all创建数据库和表，然后在其中加入了一些测试用的数据，并保存。最后，我们创建了两个用于测试的测试客户端和测试命令运行器，前者用于模拟客户端请求，后者用来触发自定义命令。

在清理阶段，我们调用db.session.remove来清除目前存在的数据库会话，并调用drop_all()删除数据库。

# 测试客户端

app.test_client()返回一个测试客户端对象，可以用来模拟客户端浏览器。我们创建类属性self.client来保存它。对它调用get方法就相当于浏览器向服务器发送GET请求，调用post方法则相当于向服务器发送POST请求。下面两个分别是用来测试404页面和主页的例子

```
class WatchlistTestCase(unittest.TestCase):
    # ...
    # 测试 404 页面
    def test_404_page(self):
        response = self.client.get('/nothing')  # 传入目标 URL
        data = response.get_data(as_text=True)
        self.assertIn('Page Not Found - 404', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)  # 判断响应状态码

    # 测试主页
    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Test\'s Watchlist', data)
        self.assertIn('Test Movie Title', data)
        self.assertEqual(response.status_code, 200)
```

通过对返回的响应使用get_data方法，并设置as_text为True，可以将返回的内容编委unicode字符串格式的响应，我们可以通过识别指定的内容是否存在与该字符串中来判断对于该响应是否正确，还可以通过识别响应宗的状态码来进一步判断。

接下来测试用户登陆的方法

```
class WatchlistTestCase(unittest.TestCase):
    # ...
    # 辅助方法，用于登入用户
    def login(self):
        self.client.post('/login', data=dict(
            username='test',
            password='123'
        ), follow_redirects=True)
```

我们需要向正确的页面发送POST请求，并在该请求中构造用户登陆数据。而将follow_redirects设为True将返回重定向后的响应。

下面是测试创建、更新和删除的方法。其中大部分断言都是在判断响应主体是否包含正确的提示消息和电影条目信息。

test_watchlist.py

```
class WatchlistTestCase(unittest.TestCase):
    # ...
    # 测试创建条目
    def test_create_item(self):
        self.login()

        # 测试创建条目操作
        response = self.client.post('/', data=dict(
            title='New Movie',
            year='2019'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Item created.', data)
        self.assertIn('New Movie', data)

        # 测试创建条目操作，但电影标题为空
        response = self.client.post('/', data=dict(
            title='',
            year='2019'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Item created.', data)
        self.assertIn('Invalid input.', data)

        # 测试创建条目操作，但电影年份为空
        response = self.client.post('/', data=dict(
            title='New Movie',
            year=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Item created.', data)
        self.assertIn('Invalid input.', data)

    # 测试更新条目
    def test_update_item(self):
        self.login()

        # 测试更新页面
        response = self.client.get('/movie/edit/1')
        data = response.get_data(as_text=True)
        self.assertIn('Edit item', data)
        self.assertIn('Test Movie Title', data)
        self.assertIn('2019', data)

        # 测试更新条目操作
        response = self.client.post('/movie/edit/1', data=dict(
            title='New Movie Edited',
            year='2019'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Item updated.', data)
        self.assertIn('New Movie Edited', data)

        # 测试更新条目操作，但电影标题为空
        response = self.client.post('/movie/edit/1', data=dict(
            title='',
            year='2019'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Item updated.', data)
        self.assertIn('Invalid input.', data)

        # 测试更新条目操作，但电影年份为空
        response = self.client.post('/movie/edit/1', data=dict(
            title='New Movie Edited Again',
            year=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Item updated.', data)
        self.assertNotIn('New Movie Edited Again', data)
        self.assertIn('Invalid input.', data)

    # 测试删除条目
    def test_delete_item(self):
        self.login()

        response = self.client.post('/movie/delete/1', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Item deleted.', data)
        self.assertNotIn('Test Movie Title', data)
```

下面是登陆、登出和认证保护的功能测试。

```
class WatchlistTestCase(unittest.TestCase):
    # ...
    # 测试登录保护
    def test_login_protect(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertNotIn('Logout', data)
        self.assertNotIn('Settings', data)
        self.assertNotIn('<form method="post">', data)
        self.assertNotIn('Delete', data)
        self.assertNotIn('Edit', data)

    # 测试登录
    def test_login(self):
        response = self.client.post('/login', data=dict(
            username='test',
            password='123'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Login success.', data)
        self.assertIn('Logout', data)
        self.assertIn('Settings', data)
        self.assertIn('Delete', data)
        self.assertIn('Edit', data)
        self.assertIn('<form method="post">', data)

        # 测试使用错误的密码登录
        response = self.client.post('/login', data=dict(
            username='test',
            password='456'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login success.', data)
        self.assertIn('Invalid username or password.', data)

        # 测试使用错误的用户名登录
        response = self.client.post('/login', data=dict(
            username='wrong',
            password='123'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login success.', data)
        self.assertIn('Invalid username or password.', data)

        # 测试使用空用户名登录
        response = self.client.post('/login', data=dict(
            username='',
            password='123'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login success.', data)
        self.assertIn('Invalid input.', data)

        # 测试使用空密码登录
        response = self.client.post('/login', data=dict(
            username='test',
            password=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login success.', data)
        self.assertIn('Invalid input.', data)

    # 测试登出
    def test_logout(self):
        self.login()

        response = self.client.get('/logout', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Goodbye.', data)
        self.assertNotIn('Logout', data)
        self.assertNotIn('Settings', data)
        self.assertNotIn('Delete', data)
        self.assertNotIn('Edit', data)
        self.assertNotIn('<form method="post">', data)

    # 测试设置
    def test_settings(self):
        self.login()

        # 测试设置页面
        response = self.client.get('/settings')
        data = response.get_data(as_text=True)
        self.assertIn('Settings', data)
        self.assertIn('Your Name', data)

        # 测试更新设置
        response = self.client.post('/settings', data=dict(
            name='Grey Li',
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Settings updated.', data)
        self.assertIn('Grey Li', data)

        # 测试更新设置，名称为空
        response = self.client.post('/settings', data=dict(
            name='',
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Settings updated.', data)
        self.assertIn('Invalid input.', data)
```

# 测试命令

 除了测试程序的各个视图函数，我们还需要测试自定义命令。app.test_cli_runner()方法返回一个命令运行器对象，我们创建类属性self.runner来保存它。通过调用它的invoke()方法可以执行命令，传入命令函数对象，或者使用args关键字直接给出命令参数列表。invoke()方法返回的命令执行结果对象，他的output属性返回命令的输出信息。下面是我们为各个自定义命令编写的测试方法。大部分的断言都是在检查执行命令后的数据库数据是否发生了正确的变化，或者判断命令行输出是否包含预期的字符。

test_watchlist.py

```
# 导入命令函数
from app import app, db, Movie, User, forge, initdb


class WatchlistTestCase(unittest.TestCase):
    # ...
    # 测试虚拟数据
    def test_forge_command(self):
        result = self.runner.invoke(forge)
        self.assertIn('Done.', result.output)
        self.assertNotEqual(Movie.query.count(), 0)

    # 测试初始化数据库
    def test_initdb_command(self):
        result = self.runner.invoke(initdb)
        self.assertIn('Initialized database.', result.output)

    # 测试生成管理员账户
    def test_admin_command(self):
        db.drop_all()
        db.create_all()
        result = self.runner.invoke(args=['admin', '--username', 'grey', '--password', '123'])
        self.assertIn('Creating user...', result.output)
        self.assertIn('Done.', result.output)
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().username, 'grey')
        self.assertTrue(User.query.first().validate_password('123'))

    # 测试更新管理员账户
    def test_admin_command_update(self):
        # 使用 args 参数给出完整的命令参数列表
        result = self.runner.invoke(args=['admin', '--username', 'peter', '--password', '456'])
        self.assertIn('Updating user...', result.output)
        self.assertIn('Done.', result.output)
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().username, 'peter')
        self.assertTrue(User.query.first().validate_password('456'))
```

# 运行测试

最后只需要在程序结尾添加下面的代码

```python
if __name__ == '__main__':
    	unittest.main()
```

然后在终端中执行测试

`python test_watchlist.py`

# 测试覆盖率

为了让程序更加强壮，我们需要让测试更加完善。一个方法就是检查测试的覆盖率，让尽可能多的代码被测试过程覆盖。可以通过coverage来检查覆盖率。

首先安装

`pip install coverage`

然后使用以下的命令执行测试并检查覆盖率

`coverage run --source=app test_watchlist.py`

其中，因为我们只是要检查程序脚本app.py的测试覆盖率，所以我们使用--source选项来指定要检查的模块和包。然后使用以下命令查看覆盖率报告

`coverage report`

或者使用以下命令生成一个html页面，来详细显示代码中那些地方没有被覆盖

`coverage html`

对于使用pytest的情况，可以安装一个pytest的插件`pytest-cov`， 然后在终端中执行`pytest --cov`来显示覆盖率，并使用`pytest --cov --cov-report=html`来生成html形式的报告，还可以通过`pytest --cov=src.app`来指定测试具体那个脚本。