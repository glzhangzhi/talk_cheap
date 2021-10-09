[TOC]

# 基本窗口

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 每个PyQt5应用程序必须创建一个应用程序对象
    w = QWidget()  # QWidget小部件是PyQt5中所有用户界面对象的基类
    w.resize(100, 100)  # resize（）方法调整窗口小部件的大小
    w.move(300, 300)  # move（）方法将小部件移动到屏幕上x = 300，y = 300坐标处的位置，屏幕左上角为(0, 0)，x轴向左，y轴向下
    w.setWindowTitle("Demo")  # 设置窗口的标题
    w.show()  # 在屏幕上显示窗口小部件。 一个小部件首先在内存中创建，然后在屏幕上显示
    sys.exit(app.exec())  # sys.exit（）方法确保一个干净的退出
```

# 面向对象编写并设置图标

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Ico(QWidget):

    def __init__(self):
        super().__init__()  # 自定义类初始化方法，但继承父类初始化方法的参数
        self.initUI()  # 创建GUI界面

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)  # 窗口X，Y，宽度，高度
        # 其实就是结合了resize和move，设定了窗口出现的位置和大小
        self.setWindowTitle('学点编程吧出品')
        self.setWindowIcon(QIcon('xdbcb8.ico'))  # 设定程序图标
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
```

# 增加关闭按钮

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧出品')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        qbtn = QPushButton('退出', self)  # 创建一个按钮，名字为退出
        qbtn.clicked.connect(QCoreApplication.instance().quit)  # 将此按钮的被点击事件与主程序退出相关联
        qbtn.resize(70, 30)
        qbtn.move(50, 50)  # 设定窗口的大小和位置

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()  
    sys.exit(app.exec_())

```

# 猜数字小程序

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        # self.num = randint(1, 100)  # 初始化窗口的时候就产生随机数
        self.num = 2

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        # self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.setToolTip('点击这里猜数字')
        # 这里不用富文本形式也是可以的
        self.bt1.clicked.connect(self.showMessage)
        # 当点击按钮时，调用showMessage方法

        self.text = QLineEdit(self)  # 创建文本输入框对象，参数时默认填入文本
        self.text.setToolTip('在这里输入数字')
        self.text.selectAll()  # 默认全选所有预设文本
        self.text.setFocus()  # 默认将输入焦点置于文本处
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):

        guessnumber = int(self.text.text())  # 读入之前文本块里的内容，并转化类型
        print(self.num)

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            # 弹出一个提示框，只有标题文本和内置文本，和一个ok按钮
            self.text.setFocus()
            # 之后将焦点重新设置回文本框处
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            # self.num = randint(1, 100)  # 重新设置随机数
            self.num = 2
            self.text.clear()  # 清除文本框内容
            self.text.setFocus()

    def closeEvent(self, event):
        # 重新定义窗口关闭事件
        reply = QMessageBox.question(
            self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 弹出单选对话框，对话框标题，对话框文本，按钮布局，默认按钮
        # 会直接返回点击的按钮
        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()  # 忽略关闭事件
		# 在弹出对话框类QMessageBox中，除了about，还有question，critical,warning,information，这几个除了图标不同外，其他没什么不同。

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

# 事件与信号处理

当调用`exec_()`方法后，应用程序进入主循环，主循环获取事件并将其发送到对象。

在事件模型中，有三个参与者：

- 事件来源，是状态更改的对象，来源生成事件
- 事件对象，将状态更改封装在事件来源之中
- 事件目标，是要通知的对象

事件来源将处理事件的任务为委托给事件目标。

一个简单的事件连接小程序。

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)  # LCD数字显示部件
        Receiver = QDial(self)  # 模拟信号输入部件
		# Receiver = QSlider(self)  # 也可以使用其他的数值输入部件

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        lcd.setGeometry(100,50,150,60)
        dial.setGeometry(120,120,100,100)

        Receiver.valueChanged.connect(lcd.display)  # 将模拟信号输入数值的改变连接到LCD数字显示

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        self.lab = QLabel('方向',self)

        self.lab.setGeometry(150,100,50,50)

        self.show()

    def keyPressEvent(self, e):
    # 重新构建按键事件

        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

```python
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)  
        # 默认情况下，部件并不会跟踪鼠标移动事件
        # 如果不设置，则只会在鼠标按键按下时移动才会触发鼠标移动事件
    
    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('学点编程吧')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):  # 这样就可以重写鼠标移动事件
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)  # event.x event.y 代表鼠标坐标
        self.label.setText('坐标: ( x: %d ,y: %d )' % (event.x(), event.y()) + " 离中心点距离: " + str(distance_from_center))       
        self.pos = event.pos()  # event.pos代表鼠标位置坐标对
        self.update()  # 注意每一帧绘图都要更新

    def paintEvent(self, event):  # 重写绘图事件
        if self.pos:
            q = QPainter(self)  # 绘图器
            q.drawLine(0, 0, self.pos.x(), self.pos.y())  # 画直线，起点坐标，终点坐标

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 获取事件发送者

```python
import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton)
from random import randint

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀',self)
        bt1.setGeometry(30,180,50,50)

        bt2 = QPushButton('石头',self)
        bt2.setGeometry(100,180,50,50)

        bt3 = QPushButton('布',self)
        bt3.setGeometry(170,180,50,50)

        bt1.clicked.connect(self.buttonclicked)  # 将按钮的点击事件与函数相关联
        bt2.clicked.connect(self.buttonclicked)
        bt3.clicked.connect(self.buttonclicked)

        self.show()

    def buttonclicked(self):
        computer = randint(1,3)
        player = 0
        sender = self.sender()  # 获取事件的发送者
        if sender.text() == '剪刀':  # 获取发送者的文本信息
            player = 1
        elif sender.text() == '石头':
            player = 2
        else:
            player = 3

        if player == computer:
            QMessageBox.about(self, '结果', '平手')
        elif player == 1 and computer == 2:
            QMessageBox.about(self, '结果', '电脑：石头，电脑赢了！')
        elif player == 2 and computer == 3:
            QMessageBox.about(self, '结果', '电脑：布，电脑赢了！')
        elif player == 3 and computer == 1:
            QMessageBox.about(self,'结果','电脑：剪刀，电脑赢了！')
        elif computer == 1 and player == 2:
            QMessageBox.about(self,'结果','电脑：剪刀，玩家赢了！')
        elif computer == 2 and player == 3:
            QMessageBox.about(self,'结果','电脑：石头，玩家赢了！')
        elif computer == 3 and player == 1:
            QMessageBox.about(self,'结果','电脑：布，玩家赢了！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 发出自定义信号

```python
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)

class Signal(QObject):
    showmouse = pyqtSignal()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')

        self.s = Signal()
        self.s.showmouse.connect(self.about)

        self.show()
    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    def mousePressEvent(self, e):
        self.s.showmouse.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 绝对定位

```python
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀',self)
        bt1.move(50,250)  # 绝对定位，零点相对于窗口左上角，改变窗口大小并不会使部件移动

        bt2 = QPushButton('石头',self)
        bt2.move(150,250)

        bt3 = QPushButton('布',self)
        bt3.move(250,250)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
```

# 箱式布局

```python
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        hbox = QHBoxLayout()  # 设置一个水平布局
        hbox.addStretch(1)  # 添加一个弹簧因子
        # 1代表比例为1，即将所有按钮防止后，此处占总空白空间的1/n
        # 左右各设置一个，比例因子相同，可实现将按钮放在中间
        hbox.addWidget(bt1)  # 添加第一个按钮
        hbox.addWidget(bt2)  # 第二个按钮
        hbox.addWidget(bt3)  # 第三个按钮
        # 效果：
        #  || (弹簧，可伸缩空间) 按钮一 按纽二 按钮三 ||

        vbox = QVBoxLayout()  # 设置一个竖直布局
        vbox.addStretch(1)  # 添加一个弹簧因子
        vbox.addLayout(hbox)  # 水平布局框
		# 效果：
        # ----
        # （弹簧，可伸缩空间）
        # 水平布局
        # ----
        self.setLayout(vbox)  # 布局放置

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
```

# 网格布局

```python
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        grid = QGridLayout()  # 创建栅格布局
        self.setLayout(grid)  # 放置布局

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧-计算器')

        self.lcd =  QLCDNumber()
        grid.addWidget(self.lcd,0, 0)
        # addWidget(Widget, row, column, width, height)
        grid.setSpacing(10)  # 设置每个单元格之间的间距

        names = ['Cls', 'Bc', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(4,9) for j in range(0,4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
```

# 表单布局

```python
from os import name
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('学点编程吧')

        formlayout = QFormLayout()  # 创建表单布局
        nameLabel = QLabel("姓名")  # 文本
        nameLineEdit = QLineEdit("")  # 输入框（单行）
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")  # 输入框（多行）

        formlayout.addRow(nameLabel,nameLineEdit)  # 第一行放置
        formlayout.addRow(introductionLabel,introductionLineEdit)  # 第二行放置
        self.setLayout(formlayout)  # 放置布局

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
```

# 状态栏和菜单栏

```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--简单的菜单')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)  # 设置一个工具栏工具的图标，名称（带快捷键）
        exitAct.setShortcut('Ctrl+Q')  # 设定该功能的快捷键
        exitAct.setStatusTip('退出程序')  # 设定该工具的悬停提示
        exitAct.triggered.connect(qApp.quit)  # 将该功能和程序退出绑定

        menubar = self.menuBar()  # 设置菜单栏
        fileMenu = menubar.addMenu('文件(&F)')  # 添加第一级菜单，并设定快捷方式
        fileMenu.addAction(exitAct)  # 在第一级菜单下添加工具
        # c = fileMenu.addMenu('c')  # 添加二级菜单

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
# 上下文菜单

```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')

        # 退出功能
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        
        # 保存功能
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        
        # 另存为功能
        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        
        # 创建子菜单并加入之前的功能
        saveMenu = QMenu('保存方式(&S)', self)
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        # 新建功能
        newAct = QAction(QIcon('new.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('文件(&F)')  # 在菜单栏上添加菜单
        fileMenu.addAction(newAct)  # 在一级菜单里增加功能和二级菜单
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()  # 注意分隔符的使用
        fileMenu.addAction(exitAct)

        self.show()

    def contextMenuEvent(self, event):  # 重写上下文菜单事件

        cmenu = QMenu(self)  # 创建上下文菜单对象

        newAct = cmenu.addAction("新建")  # 添加功能动作
        opnAct = cmenu.addAction("保存")
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        quitAct = cmenu.addAction(exitAct)

        cmenu.exec_(self.mapToGlobal(event.pos()))  # 在鼠标位置执行上下文菜单
        # 这里必须要进行的一个操作是将事件在窗口的坐标映射都全局，不然定位会出现问题


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 工具栏

```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')
        
        # 退出功能
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        # 保存功能
        saveAct = QAction(QIcon('save.png'),'保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        
        # 另存为功能
        saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')

        # 新建功能
        newAct = QAction(QIcon('new.png'),'新建(&N)',self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        # 保存方式菜单
        saveMenu = QMenu('保存方式(&S)', self)
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('工具栏')  # 添加工具栏
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

