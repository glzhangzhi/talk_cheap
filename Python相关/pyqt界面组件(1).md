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

# 标准输入对话框

```python
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser)
import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,500,500,550)
        self.setWindowTitle('关注微信公众号：学点编程吧--标准输入对话框')

        self.lb1 = QLabel('姓名：',self)
        self.lb1.move(20,20)
        self.lb2 = QLabel('年龄：',self)
        self.lb2.move(20,80)
        self.lb3 = QLabel('性别：',self)
        self.lb3.move(20,140)
        self.lb4 = QLabel('身高（cm）：',self)
        self.lb4.move(20,200)
        self.lb5 = QLabel('基本信息：',self)
        self.lb5.move(20,260)
        self.lb6 = QLabel('学点编程',self)
        self.lb6.move(80,20)
        self.lb7 = QLabel('18',self)
        self.lb7.move(80,80)
        self.lb8 = QLabel('男',self)
        self.lb8.move(80,140)
        self.lb9 = QLabel('175',self)
        self.lb9.move(120,200)

        self.tb = QTextBrowser(self)  # 一个大的文本框，用于显示文本
        self.tb.move(20,320)

        self.bt1 = QPushButton('修改姓名',self)
        self.bt1.move(200,20)
        self.bt2 = QPushButton('修改年龄',self)
        self.bt2.move(200,80)        
        self.bt3 = QPushButton('修改性别',self)
        self.bt3.move(200,140)        
        self.bt4 = QPushButton('修改身高',self)
        self.bt4.move(200,200)        
        self.bt5 = QPushButton('修改信息',self)
        self.bt5.move(200,260)

        self.show()

        # 将每个按钮的按下和弹出对话框相关联
        self.bt1.clicked.connect(self.showDialog)  
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        self.bt4.clicked.connect(self.showDialog)
        self.bt5.clicked.connect(self.showDialog)
    
    # 重写弹出对话框方法
    def showDialog(self):
        sender = self.sender()  # 获取事件来源
        sex = ['男','女']
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '修改姓名', '请输入姓名：')  # 单行文本输入框
            if ok:
                self.lb6.setText(text) 
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self, '修改年龄', '请输入年龄：', min = 1)  # 整数输入框，可用箭头调整
            # 可设置最大值max，最小值min，步长step
            if ok:
                self.lb7.setText(str(text))
        elif sender == self.bt3:
            text, ok = QInputDialog.getItem(self, '修改性别', '请选择性别：', sex)  # 下拉框
            if ok:
                self.lb8.setText(text)        
        elif sender == self.bt4:
            text, ok = QInputDialog.getDouble(self, '修改身高', '请输入身高：', min = 1.0)  # 浮点数输入框，可用箭头调整
            # 可设置最大值max，最小值min，步长step
            if ok:
                self.lb9.setText(str(text))
        elif sender == self.bt5:
            text, ok = QInputDialog.getMultiLineText(self, '修改信息', '请输入个人信息：')  # 多行文本输入框
            if ok:
                self.tb.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 字体，颜色和打开文件对话框

```python
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--记得好看点')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()
    
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')  # 参数分别为窗口名称，默认路径，返回包含文件名的元组，第一个是文件名的列表
        # 使用QFileDialog.getOpenFileNames可以打开多个文件
        # fname = QFileDialog.getOpenFileName(self, '打开文件','./',("Images (*.png *.xpm *.jpg)"))  # 可以这样设置文件类型过滤
        if fname[0]:
            with open(fname[0], 'r',encoding='gb18030', errors='ignore') as f:
                self.tx.setText(f.read()) 
    
    def choicefont(self):
        font, ok = QFontDialog.getFont()  # 打开字体选取对话框
        if ok:
            self.tx.setCurrentFont(font)  # 设置某个文本的字体
    
    def choicecolor(self):
        col = QColorDialog.getColor()  # 打开颜色选取对话框
        if col.isValid():
            self.tx.setTextColor(col)  # 设置某个文本的颜色

# 注意，上面的修改颜色和字体，对于一个大的文本输入框来说，只能更改选中的文本
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 保存文件和打印

```python
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('关注微信公众号：学点编程吧--保存、打印文件')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('打开多个文件',self)
        self.bt2.move(350,70)
        self.bt5 = QPushButton('保存文件',self)
        self.bt5.move(350,220)
        self.bt6 = QPushButton('页面设置',self)
        self.bt6.move(350,270)
        self.bt7 = QPushButton('打印文档',self)
        self.bt7.move(350,320)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.openfiles)
        self.bt5.clicked.connect(self.savefile)
        self.bt6.clicked.connect(self.pagesettings)
        self.bt7.clicked.connect(self.printdialog)

        self.show()
    
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '学点编程吧:打开文件','./')
            if fname[0]:
                with open(fname[0], 'r',encoding='gb18030',errors='ignore') as f:
                    self.tx.setText(f.read())
    
    def openfiles(self):
        fnames = QFileDialog.getOpenFileNames(self, '学点编程吧:打开多个文件','./')  # 这个可以打开多个文件
            if fnames[0]: 
                for fname in fnames[0]:
                    with open(fname, 'r',encoding='gb18030',errors='ignore') as f:
                        self.tx.append(f.read())  # 注意这里使用的是append方法，不会覆盖文本框里已有的内容
    
    def savefile(self):
        fileName = QFileDialog.getSaveFileName(self, '学点编程吧:保存文件','./',"Text files (*.txt)")  # 保存文件对话框，设定默认格式，返回文件名
            if fileName[0]:
                with open(fileName[0], 'w',encoding='gb18030',errors='ignore') as f:
                    f.write(self.tx.toPlainText())  # 将文本转换为纯文本
    
    def pagesettings(self):
        printsetdialog = QPageSetupDialog(self.printer,self)
        printsetdialog.exec_()
    
    def printdialog(self):
        printdialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 各种消息对话框

```python
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--消息对话框')

        self.la = QLabel('这里将会显示我们选择的按钮信息', self)
        self.la.move(20, 20)
        self.bt1 = QPushButton('提示', self)
        self.bt1.move(20, 70)
        self.bt2 = QPushButton('询问', self)
        self.bt2.move(120, 70)
        self.bt3 = QPushButton('警告', self)
        self.bt3.move(220, 70)
        self.bt4 = QPushButton('错误', self)
        self.bt4.move(20, 140)
        self.bt5 = QPushButton('关于', self)
        self.bt5.move(120, 140)
        self.bt6 = QPushButton('关于Qt', self)
        self.bt6.move(220, 140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(
            self, '提示', '这是一个消息提示对话框!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        # 提示消息对话框，只有按钮
        if reply == QMessageBox.Ok:
            self.la.setText('你选择了Ok！')
        else:
            self.la.setText('你选择了Close！')

    def question(self):
        reply = QMessageBox.question(self, '询问', '这是一个询问消息对话框，默认是No',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        # 提问对话框，也只有按钮
        if reply == QMessageBox.Yes:
            self.la.setText('你选择了Yes！')
        elif reply == QMessageBox.No:
            self.la.setText('你选择了No！')
        else:
            self.la.setText('你选择了Cancel！')

    def warning(self):
        # reply = QMessageBox.warning(self,'警告','这是一个警告消息对话框', QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        # 上面这个是基于静态方法，按钮只能调用预设按钮，所以按钮上的问题与功能都制衡使用预设的，所以只能显示文本，按钮
        
        # 以下是基于对象的，可以自己从基本元素开始构建对话框，虽然繁琐，但自定义程度高，可以自己添加想要的元素和功能
        msgBox = QMessageBox()
        msgBox.setWindowTitle('警告')  # 设置标题
        msgBox.setIcon(QMessageBox.Warning)  # 设置图标
        msgBox.setText('这是一个警告消息对话框')  # 设置提示文本
        msgBox.setInformativeText('出现更改愿意保存吗?')  # 设置提示文本下的信息文本
        Save = msgBox.addButton('保存', QMessageBox.AcceptRole)  # 添加按钮，可以设定文本和功能
        NoSave = msgBox.addButton('取消', QMessageBox.RejectRole)
        Cancel = msgBox.addButton('不保存', QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(Save)  # 设定默认按钮
        cb = QCheckBox('所有文档都按此操作')  # 这里是一个在界面上的勾选框
        cb.stateChanged.connect(self.check)  # 将单选框的状态改变连接至另一个函数
        msgBox.setCheckBox(cb)  # 添加单选框
        reply = msgBox.exec()  # 每一个对话框都会返回用户选择的按钮，可用户后续的判断
        
        if reply == QMessageBox.AcceptRole:
            self.la.setText('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            self.la.setText('你选择了取消！')
        else:
            self.la.setText('你选择了不保存！')

    def critical(self):
        # reply = QMessageBox.critical(self, '错误', '这是一个错误消息对话框', QMessageBox.Retry |
        #                              QMessageBox.Abort | QMessageBox.Ignore, QMessageBox.Retry)
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(
            QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)  # 在使用对象的方法下添加默认按钮
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')  # 添加详细信息按钮，并设置文本，只有在该字符串被设置后，才会出现按钮，不需要单独添加按钮
        reply = msgBox.exec()  # 注意，基于对象的自定义消息框，都需要在定义完成后执行一下，以显示对话框

        if reply == QMessageBox.Retry:
            self.la.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.la.setText('你选择了Abort！')
        else:
            self.la.setText('你选择了Ignore！')

    def about(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '不要意淫了，早点洗洗睡吧!')
        msgBox.setIconPixmap(QPixmap("beauty.png"))  # 添加自定义图标，需要使用QPixmap进行图标类型的映射
        msgBox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self, '关于Qt')

    def check(self):
        if self.sender().isChecked():  # 读取事件来源，也就是单选框的状态
            self.la.setText('你打勾了哦')
        else:
            self.la.setText('怎么又不打了啊')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

# 自定义对话框

```python
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator


class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：", self)

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)  # 安装事件过滤器

        self.bt1 = QPushButton("确定", self)
        self.bt2 = QPushButton("取消", self)

        # 怎么布局在布局篇介绍过，这里代码省略...

        self.edit.setContextMenuPolicy(
            Qt.NoContextMenu)  # 设定该控件的上下文菜单策略，此处为忽略上下文菜单
        # 设定灰色占位文本，用户输入后消失，不需要自己全选删除，推荐在文本输入框中使用
        self.edit.setPlaceholderText("密码6-15位，只能有数字和字母，必须以字母开头")
        self.edit.setEchoMode(QLineEdit.Password)  # 设定文本显示方式
        # QLineEdit.Normal  直接显示输入的字符
        # QLineEdit.NoEcho  不要显示任何字符(like in Unix)
        # QLineEdit.Password  用掩码字符代替原本输入字符显示，如小圆点或星号
        # QLineEdit.PasswordEchoOnEdit  只在编辑时显示字符，点击其他控件会替换成掩码

        # 创建正则匹配，构造验证器并设置文本框只接收符合条件的文本
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)

        object = QObject()

    # 配置事件过滤器
    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True  # 返回True意味着忽略该次事件
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)  # 如果如果没有忽略任何事件，就继续监视事件

    def Ok(self):
        '''配置一些基本的密码长度检测
        '''
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)          # 结束对话框返回1

    def Cancel(self):
        self.done(0)  # 结束对话框返回0
```

# 进度条对话框

```python
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox,
                             QProgressDialog, QPushButton, QWidget)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("微信公众号：学点编程吧--进度对话框")

        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)

        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)
        self.bt1.clicked.connect(self.showDialog)

        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)

        self.show()

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)  # 创建一个进度条对话框
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)  # 设置进度条对话框出现的最低时间，只有超过这个时间，进度条才显示
        # 还可以使用setMinimum()和setMaxmun()来设置进度条总进度区间
        progress.setWindowModality(Qt.WindowModal)  # 此属性保留由模态小部件阻止的窗口，TODO这个需要进一步研究
        progress.setRange(100, num)  # 相当于setMinimun()和setMaxmun()
        for i in range(num):
            progress.setValue(i)  # 每一步都更新进度条显示的值
            if progress.wasCanceled():  # 如果按下取消键，这里是默认关联到进度条对话框的取消按钮
                QMessageBox.warning(self, "提示", "操作失败")
                break
            if i == num - 1:
                progress.setValue(num)  # 这个是进度条对话框的退出条件，当其等于设置的最大值时，对话框退出
                # 对话框自动在操作结束时重置并隐藏自身，使用setAutoReset()和setAutoClose()来更改此行为。
                QMessageBox.information(self, "提示", "操作成功")
                break
        
        # 以下是对象化的创建
        # progress = QProgressDialog(self)
        # progress.setWindowTitle("请稍等")  
        # progress.setLabelText("正在操作...")
        # progress.setCancelButtonText("取消")
        # progress.setMinimumDuration(5)
        # progress.setWindowModality(Qt.WindowModal)
        # progress.setRange(0,num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

# 单选/复选框

```python
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.cb1 = QCheckBox('全选', self)
        self.cb2 = QCheckBox('你是', self)
        self.cb3 = QCheckBox('我的', self)
        self.cb4 = QCheckBox('宝贝', self)
        self.bt = QPushButton('提交', self)

       # 为减少行数，部分非重要代码省略....

        self.cb1.stateChanged.connect(self.changecb1)  # 当第一个复选框状态改变时，触发函数
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        self.bt.clicked.connect(self.go)

        self.show()

    def go(self):
        '''通过判断多个复选框的状态来改变文本的内容
        '''
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self, 'I Love U', '你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '宝贝！')
        else:
            QMessageBox.information(self, 'I Love U', '貌似你没有勾选啊！')

    def changecb1(self):
        '''编辑第一个全选复选框的逻辑，即用全选复选框的状态改变下面多个复选框的状态
           \n注意cb.checkState(), Qt.Checked, Qt.Unchecked, setChecked(T/F)的使用
        '''
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)

    def changecb2(self):
        # 如果三个复选框全部被选中，则将此复选框选中
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        # 如果部分被选中，则将此复选框的状态改为部分选中
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate()  # 设置该复选框为三态复选框，即可以被部分选中
            self.cb1.setCheckState(Qt.PartiallyChecked)
        # 若全部都没选中，则设置该复选框为未选中
        else:
            self.cb1.setTristate(False)
            self.cb1.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

# 单选按钮

```python
from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QPushButton, QMessageBox, QButtonGroup
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.rb11 = QRadioButton('你是', self)
        self.rb12 = QRadioButton('我是', self)
        self.rb13 = QRadioButton('他是', self)
        self.rb21 = QRadioButton('大美女', self)
        self.rb22 = QRadioButton('大帅哥', self)
        self.rb23 = QRadioButton('小屁孩', self)

        bt1 = QPushButton('提交', self)

        # 为节省行数，部分非重要代码省略...

        # 按钮加入一个ButtonGroup，可以实现同组内单选互斥
        # 如果不加入分组，则所有单选按钮之前默认互斥
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rb11, 11)  
        # 将按钮加入按键组以后，设定一个触发信号，每当该按钮被按下，则返回该信号值，后面可以通过这个信号值判断是哪个按键被触发
        # 如果不设置，默认按顺序-2, -3, -4 ...
        self.bg1.addButton(self.rb12, 12)
        self.bg1.addButton(self.rb13, 13)

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.rb21, 21)
        self.bg2.addButton(self.rb22, 22)
        self.bg2.addButton(self.rb23, 23)

        self.info1 = ''
        self.info2 = ''

        # 然后将按键组的选择连接到对应函数
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        
        bt1.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.info1 == '' or self.info2 == '':
            QMessageBox.information(self, 'What?', '貌似有没有选的啊，快去选一个吧！')
        else:
            QMessageBox.information(self, 'What?', self.info1+self.info2)

    def rbclicked(self):
        # 通过判断事件来源，选择对应行为
        sender = self.sender()
        if sender == self.bg1:
            if self.bg1.checkedId() == 11:  
            # 检查按键组内的触发ID
            # 如果某按键没有被按下，则发送信号-1
                self.info1 = '你是'
            elif self.bg1.checkedId() == 12:
                self.info1 = '我是'
            elif self.bg1.checkedId() == 13:
                self.info1 = '他是'
            else:
                self.info1 = ''
        else:
            if self.bg2.checkedId() == 21:
                self.info2 = '大美女'
            elif self.bg2.checkedId() == 22:
                self.info2 = '大帅哥'
            elif self.bg2.checkedId() == 23:
                self.info2 = '小屁孩'
            else:
                self.info2 = ''


if __name__ == '__main__':
    # 常规代码，省略...
    pass
```

# 普通按钮

```python
class Example(QWidget):
    def initUI(self):


        self.bt2 = QPushButton('发送验证码',self)
        self.bt2.clicked.connect(self.Action)
        
        menu = QMenu(self)  # 这里新建了一个菜单
        menu.addAction('我是')
        menu.addSeparator()
        menu.addAction('世界上')
        menu.addSeparator()
        menu.addAction('最帅的')
        
        self.bt1 = QPushButton("这是什么",self)
        self.bt1.setMenu(menu)  # 然后将这个菜单附加到按钮上

        self.count = 10

        self.time = QTimer(self)  # 计时器部件
        self.time.setInterval(1000)  # 设置每一次时间变化的间隔
        self.time.timeout.connect(self.Refresh)  # 倒计时结束后触发Refresh

        self.show()

    def Action(self):
        if self.bt2.isEnabled():  # 当第二个按钮可以按了
            self.time.start()  # 开始计时器
            self.bt2.setEnabled(False)  # 将此按钮算作不可按
    
    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count)+'秒后重发')  # 试试改变bt2按钮的文字
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10
```

# 工具按钮

```python
class Example(QWidget):
    def initUI(self):

        tb = QToolButton(self)  # 新建一个工具按钮
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # 设置工具按钮的样式，一般图标在文字旁边的是常用的
        # ToolButtonTextOnly  只显示文字
        # tb.setArrowType(Qt.DownArrow)  
        # 这个会在将按钮的图标设置为一个向下的箭头，提示用户这是一个工具按钮，但是比较丑陋
        tb.setToolTip('选择适合你的支付方式')
        tb.setPopupMode(QToolButton.MenuButtonPopup)
        # 工具按钮的弹出方式
        # QToolButton.DelayedPopup  按住一段时间以后弹出
        # QToolButton.MenuButtonPopup  在按钮右方有个箭头
        # QToolButton.InstantPopup  点击按钮本身，所以本身的点击不会触发其他事件

        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        tb.setAutoRaise(True)
        # 当鼠标滑过时，按钮是否会有一个升起的效果

        menu = QMenu(self)
        # 把不同动作抽象成QAction，方便将其绑定到不同的地方，比如菜单栏，工具栏，上下文菜单或者任何按钮
        # self.alipayAct = QAction()
        # self.alipayAct.setText('abc')
        # self.alipayAct.triggered.connect(self.some_function)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'),'支付宝支付', self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'),'微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'),'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'),'万事达卡支付', self)

        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)

        tb.setMenu(menu)
        self.show()

        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)
        
    def on_click(self):
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))
```

# 抽象按钮

```python
# 上述按钮，都继承了QAbstractButton的父类，拥有很多共同的方法
button.setText('some_text')
button.setIcon('icon.png')
# 都具有图标和标签，可以使用setText()和setIcon()来设置
# 都可以被禁用，禁用后会出现相应的视觉效果
button.setText('&Click')
button.setShortcut('alt+F7')
# 可以在文本中加入&字符，之后的字母会作为快捷键使用,&f = alt + f, 其实这里是当触发按键时，调用了animateClick()，也可以使用setShortcut('Alt+F7')自定义快捷键
button.setDefault()
# 可以使用setDefault()设定默认按钮
button.isDown()
button.isChecked()
button.isEnabled()
# 使用isDown(),isChecked(),isEnabled()查看按钮是否被按下、是否被选中、是否能被按下
bt.setAutoRepeat()
bt.autoRepeatDelay()
bt.autoRepeatInterval()
# 设置当按钮持续被按下时，是否有自动重复的行为，以及持续按键多久触发，和每次重复之间的间隔
bt.isDown()
bt.isCheck()
# 这两者的区别是Down指按下，指一个按钮被按下的瞬间及其一直保持被按下，Check指有个框在按钮周围，按空格键可以选中这个按钮
bt.pressed()  # 当按钮被按下时发出
bt.release()  # 当按钮被释放时发出
bt.clicked()  # 当按钮被按下然后被释放时发出
bt.toggle()  # 当开关按钮的状态发生变化是发出
# 按钮的四种信号

```

```python
class Example(QWidget):

    def initUI(self):

        self.resize(500,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--抽象按钮的学习1（QAbstractButton）')

        label1 = QLabel('密码输入区',self)
        label2 = QLabel('正确密码：麻',self)
        label3 = QLabel('你输入的密码：',self)

        self.label4 = QLabel('  ',self)

        bt1 = QPushButton('芝',self)
        bt2 = QPushButton('麻',self)
        bt3 = QPushButton('开',self)
        bt4 = QPushButton('门',self)

        bt1.setCheckable(True)  # 设置按钮为checkable状态，即点击后按钮下陷，需要在按一次才能弹起
        bt2.setCheckable(True)
        bt3.setCheckable(True)
        bt4.setCheckable(True)

        bt1.setAutoExclusive(True)  # 设置按钮的互斥
        bt2.setAutoExclusive(True)
        bt3.setAutoExclusive(True)
        bt4.setAutoExclusive(True)

        bt1.clicked.connect(self.setPassword)
        bt2.clicked.connect(self.setPassword)
        bt3.clicked.connect(self.setPassword)
        bt4.clicked.connect(self.setPassword)

    def setPassword(self):
        word = self.sender().text()
        self.label4.setText(word)
        if word == '麻':
            QMessageBox.information(self,'提示','恭喜，密码正确，可以进入！')
```

# 滑块

```python
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #部分非重要代码省略...

        self.sld1 = QSlider(Qt.Vertical,self)  # 初始化垂直滑块对象
        self.sld1.setGeometry(30,40,30,100)
        self.sld1.setMinimum(0)  # 设置最小值
        self.sld1.setMaximum(99)  # 设置最大值
        self.sld1.setTickPosition(QSlider.TicksLeft)  # 设置滑块刻度位置
        # TicksBothSides, TicksAbove, TicksBelow, TicksLeft, TicksRight
 
        self.sld2 = QSlider(Qt.Horizontal,self)  # 初始化水平滑块对象
        self.sld2.setGeometry(500,350,100,30)
        self.sld2.setMinimum(0)
        self.sld2.setMaximum(99)

        self.sld1.valueChanged[int].connect(self.changevalue)  # 将值传入函数，而不是将值改变的事件传入函数
        self.sld2.valueChanged[int].connect(self.changevalue)

        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('01.jpg'))
        self.label1.setGeometry(80,150,600,180)

        self.label2 = QLabel('滑动块1当前值: 0 ',self)
        self.label2.move(70,70)

        self.label3 = QLabel('滑动块2当前值: 0 ',self)
        self.label3.move(550,390)

        self.show()
    
    def changevalue(self,value):
        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)  # 通过数值改变滑块的位置
        else:
            self.sld1.setValue(value)
        self.label2.setText('滑动块1当前值:'+str(value))
        self.label3.setText('滑动块2当前值:'+str(value))
        if value == 0:
            self.label1.setPixmap(QPixmap('01.jpg'))
        elif value > 0 and value <= 30:
            self.label1.setPixmap(QPixmap('02.jpg'))
        elif value > 30 and value < 80:
            self.label1.setPixmap(QPixmap('03.jpg'))
        else:
            self.label1.setPixmap(QPixmap('04.jpg'))
        
if __name__ == '__main__':
    #常规代码省略...
```

# 进度条

```python
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()    def initUI(self):

        self.resize(600,480)
        self.setWindowTitle('关注微信公众号：学点编程吧--跑马灯（进度条）')

        self.pb11 = QProgressBar(self)  # 初始化进度条对象
        #self.pb12、self.pb13、self.pb14、self.pb21、self.pb22都这样创建的
        #代码省略...

        self.pb11.setOrientation(Qt.Horizontal)  # 设置进度条的方向
        self.pb12.setOrientation(Qt.Vertical)
        self.pb13.setOrientation(Qt.Horizontal)
        self.pb14.setOrientation(Qt.Vertical)
        #布局的代码省略...

        self.pb21.setFormat("%v")  # %p 已完成百分比 %m 总step数 %v 当前step数
        self.pb22.setInvertedAppearance(True)  # 进度条反向增长

        self.b1 = QPushButton('外圈跑马灯',self)
        self.b2 = QPushButton('内圈跑进度',self)

        self.show()

        self.timer = QBasicTimer()
        self.step = 0

        self.b1.clicked.connect(self.running)
        self.b2.clicked.connect(self.doaction)
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self,'提示','内圈收工了!')
            self.b2.setText('再来一次')
            self.step = 0
            return

        self.step = self.step + 1
        self.pb21.setValue(self.step)
        self.pb22.setValue(self.step)
    def doaction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.b2.setText('继续')
        else:
            self.timer.start(100, self)
            self.b2.setText('停止')
        
    def running(self):
        self.pb11.setMinimum(0)
        self.pb11.setMaximum(0)
        self.pb12.setInvertedAppearance(True)
        self.pb12.setMinimum(0)
        self.pb12.setMaximum(0)
        self.pb13.setInvertedAppearance(True)
        self.pb13.setMinimum(0)
        self.pb13.setMaximum(0)
        self.pb14.setMinimum(0)
        self.pb14.setMaximum(0)
    
if __name__ == '__main__':
    #常规代码省略...
```

# 数值调整框

```python
class HolyShitBox(QSpinBox):
    def valueFromText(self,str):
        regExp = QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")
        if regExp.exactMatch(str):
            return int(regExp.cap(1))
        else:
            return 0

    def textFromValue(self,num):
        return "{0} x {1}".format(num,num)
            
            
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(350,280)
        self.setWindowTitle('关注微信公众号：学点编程吧--微调框')

        lb1 = QLabel('普通微调框',self)
        lb2 = QLabel('加强微调框',self)
        lb3 = QLabel('超神微调框',self)

        self.sp1 = QSpinBox(self)  # 整数调整框
        self.sp2 = QSpinBox(self)
        self.sp3 = HolyShitBox(self)  # 自定义调整框

        self.sl = QSlider(Qt.Horizontal,self) 
    
        #布局代码省略...

        self.sp1.setRange(-10, 200)  # 设定数值范围
        self.sp1.setSingleStep(10)  # 设定步长
        self.sp1.setWrapping(True)  # 是否能循环调整
        self.sp1.setValue(-10)  # 设定当前调整框数值

        self.sp2.setRange(0, 100)
        self.sp2.setSingleStep(10)
        self.sp2.setValue(10)
        self.sp2.setPrefix("我的帅达到 ") # 设定调整框文字的前缀
        self.sp2.setSuffix(" %，正在充帅中...")  # 设定调整框文字的后缀

        self.sp3.setRange(10, 50)
        self.sp3.setValue(10)
        self.sp3.setWrapping(True)

        self.sl.setRange(-10, 200)
        self.sl.setValue(-10)

        self.sp1.valueChanged.connect(self.slider1_changevalue)
        self.sp2.valueChanged.connect(self.slider2_changevalue)
        self.sl.valueChanged.connect(self.spinbox_changevalue)
        self.show()
        
    def slider1_changevalue(self,value):
        self.sl.setValue(value)
    
    def slider2_changevalue(self,value):
        if self.sp2.value() == self.sp2.maximum():
            QMessageBox.information(self,'提示','你怎么还再充帅，你不知道你的帅已经引起了别人的嫉妒吗？')
            self.sp2.setSuffix(" %,我踏马太帅了！！")
        elif self.sp2.minimum()< self.sp2.value() < self.sp2.maximum():
            self.sp2.setSuffix(" %，正在充帅中...")
    
    def spinbox_changevalue(self,value):
        self.sp1.setValue(value)
```
